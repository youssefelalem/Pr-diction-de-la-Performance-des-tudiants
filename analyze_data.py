import pandas as pd
import sys

# Redirect output to a file
sys.stdout = open('analysis_report.txt', 'w', encoding='utf-8')

# Load the dataset
try:
    df = pd.read_csv('Morocco_Student_Data_Pool.csv', low_memory=False)
    print("Dataset loaded successfully.")
except Exception as e:
    print(f"Error loading dataset: {e}")
    exit()

# Basic Information
print("\n--- Basic Information ---")
print(f"Shape: {df.shape}")
print("\n--- Column Info ---")
print(df.info())

# Missing Values
print("\n--- Missing Values ---")
missing_values = df.isnull().sum()
print(missing_values[missing_values > 0])

# Duplicates
print("\n--- Duplicates ---")
duplicates = df.duplicated().sum()
print(f"Number of duplicate rows: {duplicates}")

# Unique values in categorical columns (sample)
print("\n--- Unique Values in Select Categorical Columns ---")
categorical_cols = ['sexe', 'region', 'type_etablissement', 'filiere']
for col in categorical_cols:
    if col in df.columns:
        print(f"\nUnique values in '{col}':")
        print(df[col].unique()[:10]) # Show first 10 unique values

# Summary Statistics for numerical columns
print("\n--- Summary Statistics ---")
print(df.describe())
