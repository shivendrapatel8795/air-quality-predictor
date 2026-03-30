import pandas as pd

# file read karna
df = pd.read_csv("data/raw/aqi_raw.csv")

# first 5 rows print karna
print("Data preview:")
print(df.head())

# missing values remove
df = df.dropna()

# cleaned file save
df.to_csv("data/processed/aqi_cleaned.csv", index=False)

print("Cleaned data saved!")