# Data Setup

The raw Online Retail II dataset is intentionally not stored in this GitHub repository because the source file is large.

## Download

Use the official UCI Machine Learning Repository page:

https://archive.ics.uci.edu/dataset/502/online+retail+ii

Download `online_retail_II.xlsx` and place it in the working directory used by the Python script.

## Expected Workbook Sheets

The source workbook contains the two yearly worksheets used by the analysis:

- `Year 2009-2010`
- `Year 2010-2011`

The processing script combines both worksheets before cleaning and analysis.

## Reproducibility

The Python script in `../python/process_online_retail_II.py` reads the workbook, cleans the records and creates `processed_online_retail_II.csv`.
