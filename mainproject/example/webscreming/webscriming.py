from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import os

# Create data directory
# os.makedirs('data', exist_ok=True)

# driver = webdriver.Chrome()
# query = 'laptop'
# laptop_name = 'dell'
# file = 0

# for i in range(32):
#     # driver.get(f"https://www.amazon.in/s?k={query}+{laptop_name}&i=computers&page={i}&crid=18ZAB0S0IG7BR&qid=1735357839&sprefix=laptop+lenov%2Ccomputers%2C254&ref=sr_pg_{i}")
#     # driver.get(f'https://www.flipkart.com/search?q={query}+{laptop_name}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off&page={i}')
#     driver.get(f'https://www.neostore.com.np/product-category/{laptop_name}-{query}/{i}')
#     elems = driver.find_elements(By.CLASS_NAME,'item col')
#     print(f'{len(elems)} it is the lenth of download data')
    
#     for elem in elems:
#         d = elem.get_attribute('outerHTML')
#         with open(f"data/{query}_{file}.html","w",encoding="utf-8") as f:
#             f.write(d)
#             file +=1

#     time.sleep(2)
    
# driver.close()



#####################################################
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time
# import os

# # Create data directory
# os.makedirs('data', exist_ok=True)

# driver = webdriver.Chrome()
# file = 0

# # Target specific page
# url = 'https://www.neostore.com.np/'
# driver.get(url)

# # Wait for page load
# time.sleep(5)

# # Get the specific class content
# class_name = 'wpf-search-container'
# elem = driver.find_element(By.CLASS_NAME, class_name.replace(' ', '.'))
# content = elem.get_attribute('outerHTML')

# # Save the content
# with open(f"data/acer_laptops_page1.html", "w", encoding="utf-8") as f:
#     f.write(content)

# driver.close()




##################################################################
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time
import os
import csv
import urllib.parse

# Create data directory
os.makedirs('data', exist_ok=True)

driver = webdriver.Chrome()

# Read URLs from CSV file
with open('all_nav_bar_final_data.csv', 'r') as csvfile:
    csv_reader = csv.reader(csvfile)
    next(csv_reader, None)  # Skip header row if exists
    for row in csv_reader:
        if not row:  # Skip empty rows
            continue
            
        url = row[0].strip()  # Get URL and remove whitespace
        
        # Validate URL
        if not url or not url.startswith('http'):
            print(f"Skipping invalid URL: {url}")
            continue
        
        # Extract the last word from URL to use as filename
        path_parts = urllib.parse.urlparse(url).path.strip('/').split('/')
        filename = path_parts[-1] if path_parts else 'index'
        
        print(f"Processing URL: {url}")
        page = 1
        
        try:
            driver.get(url)
            
            while True:
                # Wait for page load
                time.sleep(5)
                
                # Get the specific class content
                class_name = 'wpf-search-container'
                try:
                    elem = driver.find_element(By.CLASS_NAME, class_name.replace(' ', '.'))
                    content = elem.get_attribute('outerHTML')
                    
                    # Save the content
                    with open(f"data/{filename}_page{page}.html", "w", encoding="utf-8") as f:
                        f.write(content)
                    
                    print(f"Saved page {page} for {filename}")
                    
                    # Find next page link
                    next_page = driver.find_element(By.CSS_SELECTOR, f'a[data-ci-pagination-page="{page + 1}"]')
                    next_url = next_page.get_attribute('href')
                    page += 1
                    driver.get(next_url)
                    
                except NoSuchElementException:
                    print(f"Reached last page for {filename}: {page}")
                    break
                    
        except Exception as e:
            print(f"Error processing {url}: {str(e)}")
            continue

driver.close()
