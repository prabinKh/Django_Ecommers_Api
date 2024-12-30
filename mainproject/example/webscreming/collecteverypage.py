from bs4 import BeautifulSoup
import pandas as pd
import os

def extract_product_details(html_file):
    with open(f'data_of_everypage/{html_file}', 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
        
    data = {}
    
    # Extract images
    images_wrapper = soup.find('div', class_='product-images-wrapper')
    if images_wrapper:
        images = images_wrapper.find_all('img')
        for i, img in enumerate(images[:4], 1):
            data[f'image{i}'] = img.get('src', '')
            
    # Extract product title
    title = soup.find('h1', class_='product_title entry-title')
    data['product_title'] = title.text.strip() if title else ''
    
    # Extract short description with list items
    short_desc = soup.find('div', class_='woocommerce-product-details__short-description')
    if short_desc:
        main_text = ' '.join([p.text.strip() for p in short_desc.find_all('p')])
        list_items = ' '.join([li.text.strip() for li in short_desc.find_all('li')])
        data['short_description'] = f"{main_text} {list_items}".strip()
    else:
        data['short_description'] = ''
    
    # Extract prices
    price_elem = soup.find('p', class_='price')
    if price_elem:
        current_price = price_elem.find('ins')
        if current_price:
            current_price = current_price.text.strip().replace('Rs.', '').strip()
        
        original_price = price_elem.find('del')
        if original_price:
            original_price = original_price.text.strip().replace('Rs.', '').strip()
            
        data['price'] = f"Current Price: Rs.{current_price}, Original Price: Rs.{original_price}"
    else:
        data['price'] = ''
    
    # Extract specifications
    specs_panel = soup.find('div', class_='woocommerce-Tabs-panel--specification')
    if specs_panel:
        for row in specs_panel.find_all('tr'):
            cols = row.find_all('td')
            if len(cols) == 2:
                data[cols[0].text.strip()] = cols[1].text.strip()
    
    # Extract description
    desc_panel = soup.find('div', class_='woocommerce-Tabs-panel--description')
    if desc_panel:
        description = []
        for tag in desc_panel.find_all(['h2', 'h3', 'p']):
            description.append(tag.text.strip())
        data['description2'] = ' '.join(description)
    
    return data

# Process all files
all_data = []
for html_file in os.listdir('data_of_everypage'):
    if html_file.endswith('.html'):
        product_data = extract_product_details(html_file)
        all_data.append(product_data)

# Create DataFrame and save
df = pd.DataFrame(all_data)
df.to_csv('acer_16_32_64.csv', index=False)
