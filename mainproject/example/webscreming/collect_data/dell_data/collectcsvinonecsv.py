import pandas as pd

# Define the CSV files to combine
csv_files = [
    'dell_laptops_links16.csv',
    'dell_laptops_links_32.csv', 
    'dell_laptops_links64.csv'
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
combined_df.to_csv('dell_laptops_combined.csv', index=False)