import pandas as pd

# Load dataset
df = pd.read_csv('Dataset.csv')

# Clean whitespace
categorical_cols = ['type', 'country', 'rating', 'title', 'director']
for col in categorical_cols:
    df[col] = df[col].astype(str).str.strip()

# Standardize date format
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')

# Save cleaned output file directly to your computer
df.to_csv('cleaned_netflix_dataset.csv', index=False)
print("Success! 'cleaned_netflix_dataset.csv' saved in your current folder.")