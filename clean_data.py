import pandas as pd
import numpy as np

# Load data
try:
    df = pd.read_csv('Morocco_Student_Data_Pool.csv', low_memory=False)
    print("Dataset loaded.")
except Exception as e:
    print(f"Error: {e}")
    exit()

# 1. Drop columns with 100% missing values
missing_percent = df.isnull().mean()
drop_cols = missing_percent[missing_percent == 1.0].index.tolist()
print(f"Dropping {len(drop_cols)} columns with 100% missing values: {drop_cols}")
df.drop(columns=drop_cols, inplace=True)

# 2. Handle specific columns
# Fill annees_redoublees with 0
if 'annees_redoublees' in df.columns:
    df['annees_redoublees'] = df['annees_redoublees'].fillna(0)

# Fill type_sport, type_art with 'Aucun'
cols_fill_aucun = ['type_sport', 'type_art', 'matieres_soutien']
for col in cols_fill_aucun:
    if col in df.columns:
        df[col] = df[col].fillna('Aucun')

# 3. Convert Dates
date_cols = ['date_naissance', 'date_collecte']
for col in date_cols:
    if col in df.columns:
        df[col] = pd.to_datetime(df[col], errors='coerce')

# 4. Standardize Numeric Columns (Grades)
# Identify columns that look like grades (0-20 scale)
# This is a bit heuristic, but we can look for "arabe_s1", "moyenne_s1", etc.
grade_cols = [c for c in df.columns if 's1' in c or 's2' in c or 'annuel' in c or 'note' in c]
for col in grade_cols:
    if col in df.columns:
         df[col] = pd.to_numeric(df[col], errors='coerce')


# Save cleaned data
output_file = 'Morocco_Student_Data_Cleaned.csv'
df.to_csv(output_file, index=False)
print(f"Cleaned data saved to {output_file}")
print(f"New Shape: {df.shape}")
