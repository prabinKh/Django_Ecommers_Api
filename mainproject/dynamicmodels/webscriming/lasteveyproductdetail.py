from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import pandas as pd
import time
import os

# Read the CSV file with links
df = pd.read_csv('all_nav_bar.csv')
driver = webdriver.Chrome()

def process_page(url, base_folder):
    all_content = []
    current_url = url
    
    while current_url:
        driver.get(current_url)
        time.sleep(3)  # Wait for page load
        
        # Get main content area
        try:
            content = driver.find_element(By.CLASS_NAME, "main-content").get_attribute('innerHTML')
            all_content.append(content)
        except NoSuchElementException:
            content = driver.page_source
            all_content.append(content)
            
        # Check for next page
        try:
            pagination = driver.find_element(By.CLASS_NAME, "woocommerce-pagination")
            next_button = pagination.find_element(By.CSS_SELECTOR, "a[rel='next']")
            current_url = next_button.get_attribute('href')
        except NoSuchElementException:
            current_url = None
    
    # Combine all content and save
    combined_html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Combined Pages</title>
    </head>
    <body>
    """ + "\n".join(all_content) + """
    </body>
    </html>
    """
    
    with open(f"{base_folder}/all.html", "w", encoding="utf-8") as f:
        f.write(combined_html)
    
    print(f"Downloaded all pages in {base_folder}/all.html")

# Visit each link and save the page
for index, row in df.iterrows():
    url = row['href']
    
    # Create folder name from URL's last segment
    folder_name = url.split('/')[-1]
    if not folder_name:  # If URL ends with /, take second last segment
        folder_name = url.rstrip('/').split('/')[-1]
    
    # Create directory for this category
    folder_path = f'data_of_everypage/{folder_name}'
    os.makedirs(folder_path, exist_ok=True)
    
    # Process main page and its pagination
    process_page(url, folder_path)

driver.close()
