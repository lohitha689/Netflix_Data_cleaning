import pandas as pd

# Load dataset
df = pd.read_csv('netflix_titles.csv')
print("Initial shape:", df.shape)

# Fill missing values (safe method without inplace)
df['director'] = df['director'].fillna('Unknown')
df['cast'] = df['cast'].fillna('Not Available')
df['country'] = df['country'].fillna('Unknown')
df.dropna(subset=['date_added'], inplace=True)

# Remove duplicates
df.drop_duplicates(inplace=True)

# Standardize text
df['type'] = df['type'].str.lower().str.strip()
df['rating'] = df['rating'].str.upper().str.strip()

# Convert date format (clean first)
df['date_added'] = df['date_added'].str.strip()
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')

# Rename columns
df.columns = df.columns.str.lower().str.replace(' ', '_')

# Export cleaned data
df.to_csv('netflix_cleaned.csv', index=False)

# Final status
print("Cleaned shape:", df.shape)
print("Sample rows:\n", df.head())
print("\n✅ Cleaned dataset saved as 'netflix_cleaned.csv'")

