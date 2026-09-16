import pandas as pd

# -----------------------------------
# 1. LOAD RAW DATA
# -----------------------------------

input_file = "data/raw/DataCoSupplyChainDataset.csv"
output_file = "data/cleaned/DataCoSupplyChainDataset_cleaned.csv"

df = pd.read_csv(input_file, encoding="latin1")


# -----------------------------------
# 2. REMOVE USELESS COLUMNS
# -----------------------------------

# Product Description is completely empty
df = df.drop(columns=["Product Description"])

# Order Zipcode is mostly missing and not useful for our analysis
df = df.drop(columns=["Order Zipcode"])


# -----------------------------------
# 3. HANDLE SMALL AMOUNTS OF MISSING DATA
# -----------------------------------

# Fill missing last names with "Unknown"
df["Customer Lname"] = df["Customer Lname"].fillna("Unknown")

# Fill missing customer zipcodes with 0
df["Customer Zipcode"] = df["Customer Zipcode"].fillna(0)


# -----------------------------------
# 4. CONVERT DATE COLUMNS
# -----------------------------------

df["order date (DateOrders)"] = pd.to_datetime(
    df["order date (DateOrders)"],
    errors="coerce"
)

df["shipping date (DateOrders)"] = pd.to_datetime(
    df["shipping date (DateOrders)"],
    errors="coerce"
)


# -----------------------------------
# 5. STANDARDIZE COLUMN NAMES
# -----------------------------------

df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
    .str.replace("(", "", regex=False)
    .str.replace(")", "", regex=False)
)


# -----------------------------------
# 6. CHECK CLEANED DATA
# -----------------------------------

print("\n===== CLEANED DATASET SHAPE =====")
print(df.shape)

print("\n===== REMAINING MISSING VALUES =====")
print(df.isnull().sum()[df.isnull().sum() > 0])

print("\n===== DUPLICATE ROWS =====")
print(df.duplicated().sum())


# -----------------------------------
# 7. EXPORT CLEANED DATASET
# -----------------------------------

df.to_csv(output_file, index=False)

print("\nCleaned dataset saved to:")
print(output_file)
