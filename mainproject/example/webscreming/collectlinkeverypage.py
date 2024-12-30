from bs4 import BeautifulSoup
import os
import pandas as pd

d = {
    'href': [],
    
}

with open('data/acer_laptops_page1.html', encoding='utf-8') as f:
    html_doc = f.read()

soup = BeautifulSoup(html_doc, 'html.parser')
items = soup.find_all('div', class_='item col')

for item in items:
    # Get first href and src
    first_a = item.find('a')
   
    
    href = first_a['href'] if first_a else ''
   
    
    d['href'].append(href)
  

df = pd.DataFrame(d)
df.to_csv('acer_laptops_links1.csv', index=False)