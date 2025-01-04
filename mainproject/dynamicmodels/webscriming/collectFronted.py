from bs4 import BeautifulSoup
import os
import pandas as pd

def process_folder(folder_path):
    folder_name = os.path.basename(folder_path)
    print(f"Processing folder: {folder_name}")
    
    data = {
        'title': [],
        'price_first': [],
        'price_second': [],
        'image_link': [],
        'product_link': [],
        'category': []
    }
    
    html_path = os.path.join(folder_path, 'all.html')
    if not os.path.exists(html_path):
        return
        
    with open(html_path, encoding='utf-8') as f:
        html_doc = f.read()
    
    soup = BeautifulSoup(html_doc, 'html.parser')
    items = soup.find_all('div', class_='item col')
    
    for item in items:
        try:
            title = item.find('h3', class_='product-title').a['title']
            product_link = item.find('a', class_='product-thumbnail')['href']
            image_link = item.find('img')['src']
            
            price_container = item.find('div', class_='product-prices')
            price_first = price_container.find('span', class_='price-first').text.strip()
            price_second = price_container.find('span', class_='price-second').text.strip()
            
            data['title'].append(title)
            data['price_first'].append(price_first)
            data['price_second'].append(price_second)
            data['image_link'].append(image_link)
            data['product_link'].append(product_link)
            data['category'].append(folder_name)
            
        except AttributeError:
            continue
    
    if data['title']:
        df = pd.DataFrame(data)
        csv_path = os.path.join(folder_path, 'all.csv')
        df.to_csv(csv_path, index=False, encoding='utf-8')
        print(f"Successfully saved CSV for {folder_name} at {csv_path}")

def main():
    base_dir = 'data_of_everypage'
    os.makedirs(base_dir, exist_ok=True)
    
    folders = [f for f in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, f))]
    print(f"Found {len(folders)} folders to process")
    
    for folder_name in folders:
        folder_path = os.path.join(base_dir, folder_name)
        process_folder(folder_path)
        print(f"Completed processing and saving for {folder_name}")
    
    print("All folders processed and CSV files saved successfully!")

if __name__ == "__main__":
    main()
