import pandas as pd

# Load hospital dataset
df = pd.read_csv("data_ingestion/cms_hospital_quality.csv")

print("=" * 60)
print("CMS Hospital Dataset Summary")
print("=" * 60)

# Shape
print(f"Rows    : {df.shape[0]}")
print(f"Columns : {df.shape[1]}")

print("\nColumn Names")
print(df.columns.tolist())

print("\nData Types")
print(df.dtypes)

print("\nMissing Values")
print(df.isnull().sum())

print("\nDuplicate Rows")
print(df.duplicated().sum())