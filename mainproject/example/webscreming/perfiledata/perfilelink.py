from bs4 import BeautifulSoup
import os
import pandas as pd

# Process all HTML files in data directory
data_dir = 'data'
for filename in os.listdir(data_dir):
    if filename.endswith('.html'):
        # Initialize dictionary for links from this file
        file_links = {
            'href': [],
        }
        
        file_path = os.path.join(data_dir, filename)
        
        # Read HTML file
        with open(file_path, encoding='utf-8') as f:
            html_doc = f.read()
        
        # Parse HTML
        soup = BeautifulSoup(html_doc, 'html.parser')
        items = soup.find_all('div', class_='item col')
        
        # Extract links
        for item in items:
            first_a = item.find('a')
            href = first_a['href'] if first_a else ''
            file_links['href'].append(href)
        
        # Create output filename based on input HTML filename
        output_filename = filename.replace('.html', '_links.csv')
        
        # Create DataFrame and save to CSV
        df = pd.DataFrame(file_links)
        df.drop_duplicates(inplace=True)  # Remove duplicate links
        df.to_csv(os.path.join('data', output_filename), index=False)
        
        print(f"Processed {filename} - Extracted {len(df)} unique links to {output_filename}")

print("All files processed successfully!")
