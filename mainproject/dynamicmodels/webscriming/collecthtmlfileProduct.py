from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import pandas as pd
import time
import os

def download_product_page(url, save_path):
    driver.get(url)
    time.sleep(2)  # Wait for page load
    
    try:
        content = driver.find_element(By.CLASS_NAME, "main-content").get_attribute('innerHTML')
    except NoSuchElementException:
        content = driver.page_source
    
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head><title>Product Page</title></head>
    <body>
    {content}
    </body>
    </html>
    """
    
    with open(save_path, "w", encoding="utf-8") as f:
        f.write(html_content)
    
    print(f"Downloaded: {url} -> {save_path}")

def process_folder(folder_path):
    links_csv = os.path.join(folder_path, 'links.csv')
    if not os.path.exists(links_csv):
        print(f"No links.csv found in {folder_path}")
        return
    
    df = pd.read_csv(links_csv)
    products_folder = os.path.join(folder_path, 'products')
    os.makedirs(products_folder, exist_ok=True)
    
    for index, row in df.iterrows():
        url = row['href']
        product_name = url.split('/')[-1]
        save_path = os.path.join(products_folder, f"{product_name}.html")
        download_product_page(url, save_path)

def main():
    base_dir = 'data_of_everypage'
    folders = [f for f in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, f))]
    
    global driver
    driver = webdriver.Chrome()
    
    try:
        for folder_name in folders:
            folder_path = os.path.join(base_dir, folder_name)
            print(f"Processing folder: {folder_name}")
            process_folder(folder_path)
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
