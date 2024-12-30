from bs4 import BeautifulSoup
import pandas as pd

# Read the HTML file
with open('data/acer_laptops_page1.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

# Find all <a> tags and extract hrefs
links = []
for a_tag in soup.find_all('a'):
    href = a_tag.get('href')
    if href:
        links.append({'href': href})

# Create DataFrame and save to CSV
df = pd.DataFrame(links)
df.to_csv('all_nav_bar.csv', index=False)