from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pandas as pd
import time
import os

# Create directory for individual product pages
os.makedirs('data_of_everypage', exist_ok=True)

# Read the CSV file with links
df = pd.read_csv('acer_laptops_links1.csv')

driver = webdriver.Chrome()

# Visit each link and save the page
for index, row in df.iterrows():
    url = row['href']
    
    # Get the page
    driver.get(url)
    time.sleep(3)  # Wait for page load
    
    # Get page content
    page_content = driver.page_source
    
    # Create filename from URL
    filename = url.split('/')[-1] + '.html'
    
    # Save the page
    with open(f"data_of_everypage/{filename}", "w", encoding="utf-8") as f:
        f.write(page_content)
    
    print(f"Downloaded: {filename}")

driver.close()