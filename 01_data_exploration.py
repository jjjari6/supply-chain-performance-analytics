import pandas as pd

# -----------------------------------
# 1. LOAD THE RAW DATASET
# -----------------------------------

file_path = "data/raw/DataCoSupplyChainDataset.csv"

df = pd.read_csv(file_path, encoding="latin1")


# -----------------------------------
# 2. DATASET SIZE
# -----------------------------------

print("\n===== DATASET SHAPE =====")
print(f"Rows: {df.shape[0]:,}")
print(f"Columns: {df.shape[1]}")


# -----------------------------------
# 3. FIRST 5 ROWS
# -----------------------------------

print("\n===== FIRST 5 ROWS =====")
print(df.head())


# -----------------------------------
# 4. COLUMN NAMES
# -----------------------------------

print("\n===== COLUMN NAMES =====")

for i, column in enumerate(df.columns, start=1):
    print(f"{i}. {column}")


# -----------------------------------
# 5. DATA TYPES AND DATASET INFO
# -----------------------------------

print("\n===== DATASET INFORMATION =====")
df.info()


# -----------------------------------
# 6. MISSING VALUES
# -----------------------------------

print("\n===== MISSING VALUES =====")

missing_values = df.isnull().sum().sort_values(ascending=False)

print(missing_values[missing_values > 0])


# -----------------------------------
# 7. DUPLICATE ROWS
# -----------------------------------

print("\n===== DUPLICATE ROWS =====")

duplicate_rows = df.duplicated().sum()

print(f"Duplicate rows: {duplicate_rows:,}")


# -----------------------------------
# 8. BASIC NUMERICAL STATISTICS
# -----------------------------------

print("\n===== NUMERICAL SUMMARY =====")

print(df.describe())