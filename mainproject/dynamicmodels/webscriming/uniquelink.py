import pandas as pd

# Read the CSV file
df = pd.read_csv('all_nav_bar.csv')

# Drop duplicate links
df_unique = df.drop_duplicates(subset=['href'])

# Save unique links to new CSV
df_unique.to_csv('all_nav_bar_final_data.csv', index=False)