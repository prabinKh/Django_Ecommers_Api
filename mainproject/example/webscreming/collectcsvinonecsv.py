import pandas as pd

# Define the CSV files to combine
csv_files = [
    'asus_laptops_links1.csv',
    'asus_laptops_links2.csv', 

]

# Create empty list to store dataframes
dfs = []

# Read each CSV file
for csv_file in csv_files:
    df = pd.read_csv(csv_file)
    dfs.append(df)

# Concatenate all dataframes
combined_df = pd.concat(dfs, ignore_index=True)

# Save combined data
combined_df.to_csv('asus_laptops_combined.csv', index=False)