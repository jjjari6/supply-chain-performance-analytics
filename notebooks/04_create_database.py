import pandas as pd
import sqlite3
import os

# -----------------------------------
# 1. FILE PATHS
# -----------------------------------

csv_file = "data/cleaned/DataCoSupplyChainDataset_cleaned.csv"
database_file = "data/supply_chain.db"


# -----------------------------------
# 2. LOAD CLEANED DATA
# -----------------------------------

print("Loading cleaned dataset...")

df = pd.read_csv(csv_file)

print(f"Rows loaded: {len(df):,}")
print(f"Columns loaded: {len(df.columns)}")


# -----------------------------------
# 3. CREATE SQLITE DATABASE
# -----------------------------------

connection = sqlite3.connect(database_file)

print("\nCreating SQLite database...")


# -----------------------------------
# 4. LOAD DATA INTO SQL TABLE
# -----------------------------------

df.to_sql(
    "supply_chain",
    connection,
    if_exists="replace",
    index=False,
    chunksize=5000
)


# -----------------------------------
# 5. VERIFY DATABASE
# -----------------------------------

cursor = connection.cursor()

cursor.execute("SELECT COUNT(*) FROM supply_chain")

row_count = cursor.fetchone()[0]

print(f"Rows in SQL table: {row_count:,}")


# -----------------------------------
# 6. CLOSE CONNECTION
# -----------------------------------

connection.close()

print("\nDatabase created successfully:")
print(database_file)
