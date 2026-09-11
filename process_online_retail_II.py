import pandas as pd

FILE_PATH = "online_retail_II.xlsx"
df1 = pd.read_excel(FILE_PATH, sheet_name="Year 2009-2010")
df2 = pd.read_excel(FILE_PATH, sheet_name="Year 2010-2011")
df = pd.concat([df1, df2], ignore_index=True)

df.columns = ["InvoiceNo","StockCode","Description","Quantity",
              "InvoiceDate","Price","CustomerID","Country"]

df["Description"] = df["Description"].fillna("Unknown").astype(str).str.strip()
df["CustomerID"] = df["CustomerID"].fillna("Unknown")
df["Country"] = df["Country"].astype(str).str.strip()
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"], errors="coerce")
df = df.drop_duplicates()
df = df[df["Price"] > 0].copy()
df["SalesAmount"] = df["Quantity"] * df["Price"]
df.to_csv("processed_online_retail_II.csv", index=False)
print("Rows:", len(df))
print("Sales:", df["SalesAmount"].sum())
print("Transactions:", df["InvoiceNo"].nunique())
print("Products:", df["StockCode"].nunique())
print("Customers:", df.loc[df["CustomerID"] != "Unknown", "CustomerID"].nunique())
