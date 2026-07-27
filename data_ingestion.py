import pandas as pd
import os

raw_dir = os.path.join('data', 'raw')

if os.path.exists(raw_dir):
    files = [f for f in os.listdir(raw_dir) if f.endswith('.csv')]
    
    if files:
        for file in files:
            file_path = os.path.join(raw_dir, file)
            df = pd.read_csv(file_path)
            
            print(f"--- Dataset: {file} ---")
            print("Shape (Rows, Columns):", df.shape)
            print("\nData Types:\n", df.dtypes)
            print("\nFirst 5 Rows:\n", df.head())
            print("="*40)
    else:
        print("No CSV files found in 'data/raw' directory yet. Paste your CSVs there.")
else:
    print("'data/raw' directory does not exist.")