import pandas as pd

file_path = "1experience.csv"

df = pd.read_csv(file_path)

print("CSV File Content:")
print(df)

rows, columns = df.shape
print(f"\nTotal Rows: {rows}")
print(f"Total Columns: {columns}")

print(f"\nLength of the File: {rows} rows")

print("\nFirst 2 Rows:")
print(df.head(2))
