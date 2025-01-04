from bs4 import BeautifulSoup
import pandas as pd
import os

def extract_product_details(html_path):
    with open(html_path, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
        
    data = {}
    data['html_filename'] = os.path.basename(html_path)

    # Extract images
    images_wrapper = soup.find('div', class_='product-images-wrapper')
    if images_wrapper:
        images = images_wrapper.find_all('img')
        for i, img in enumerate(images[:4], 1):
            data[f'image{i}'] = img.get('src', '')
            
    # Extract product title
    title = soup.find('h1', class_='product_title entry-title')
    data['product_title'] = title.text.strip() if title else ''
    
    # Extract short description
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
    
    # Add label
    label_flag = soup.find('div', class_='product-flags discount-flag')
    data['label'] = label_flag.text.strip() if label_flag else ''

    # Extract description
    desc_panel = soup.find('div', class_='woocommerce-Tabs-panel--description')
    if desc_panel:
        description = []
        for tag in desc_panel.find_all(['h2', 'h3', 'p']):
            description.append(tag.text.strip())
        data['description2'] = ' '.join(description)
    
    return data

def process_category_folder(category_path):
    products_folder = os.path.join(category_path, 'products')
    if not os.path.exists(products_folder):
        return
        
    all_data = []
    for html_file in os.listdir(products_folder):
        if html_file.endswith('.html'):
            html_path = os.path.join(products_folder, html_file)
            product_data = extract_product_details(html_path)
            all_data.append(product_data)
    
    if all_data:
        df = pd.DataFrame(all_data)
        category_name = os.path.basename(category_path)
        csv_path = os.path.join(category_path, 'products.csv')
        df.to_csv(csv_path, index=False)
        print(f"Saved CSV for {category_name}")

def main():
    base_dir = 'data_of_everypage'
    categories = [f for f in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, f))]
    
    for category in categories:
        category_path = os.path.join(base_dir, category)
        process_category_folder(category_path)
    
    print("Processing complete!")

if __name__ == "__main__":
    main()
