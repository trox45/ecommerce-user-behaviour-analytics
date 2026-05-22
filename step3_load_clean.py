import pandas as pd

# ── 1. Load only 500,000 rows to save memory ─────────────────────
df = pd.read_csv('2019-Oct.csv', nrows=500000)

print("Shape:", df.shape)
print("\nFirst 5 rows:")
print(df.head())

print("\nColumn names:")
print(df.columns.tolist())

print("\nData types:")
print(df.dtypes)

print("\nMissing values:")
print(df.isnull().sum())

# ── 2. Drop nulls ────────────────────────────────────────────────
df = df.dropna()
print("\nShape after dropping nulls:", df.shape)

# ── 3. Fix data types ────────────────────────────────────────────
df['event_time'] = pd.to_datetime(df['event_time'])
df['price'] = pd.to_numeric(df['price'], errors='coerce')

# ── 4. Parse dates ───────────────────────────────────────────────
df['date']  = df['event_time'].dt.date
df['year']  = df['event_time'].dt.year
df['month'] = df['event_time'].dt.month
df['hour']  = df['event_time'].dt.hour

# ── 5. Remove duplicates ─────────────────────────────────────────
print("\nDuplicates before:", df.duplicated().sum())
df = df.drop_duplicates()
print("Duplicates after:", df.duplicated().sum())

# ── 6. Reset index ───────────────────────────────────────────────
df = df.reset_index(drop=True)

print("\nFinal cleaned data shape:", df.shape)
print("\nSample of cleaned data:")
print(df.head())

# ── 7. Save cleaned data ─────────────────────────────────────────
df.to_csv('ecommerce_cleaned.csv', index=False)
print("\nCleaned data saved to ecommerce_cleaned.csv")
