from bs4 import BeautifulSoup
import os
import pandas as pd

def process_folder_links(folder_path):
    folder_name = os.path.basename(folder_path)
    print(f"Processing links from folder: {folder_name}")
    
    data = {
        'href': []
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
            first_a = item.find('a', class_='product-thumbnail')
            href = first_a['href'] if first_a else ''
            data['href'].append(href)
        except AttributeError:
            continue
    
    if data['href']:
        df = pd.DataFrame(data)
        links_csv_path = os.path.join(folder_path, 'links.csv')
        df.to_csv(links_csv_path, index=False, encoding='utf-8')
        print(f"Successfully saved links for {folder_name} at {links_csv_path}")

def main():
    base_dir = 'data_of_everypage'
    folders = [f for f in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, f))]
    print(f"Found {len(folders)} folders to process")
    
    for folder_name in folders:
        folder_path = os.path.join(base_dir, folder_name)
        process_folder_links(folder_path)
        print(f"Completed extracting links from {folder_name}")
    
    print("All links extracted and saved successfully!")

if __name__ == "__main__":
    main()
