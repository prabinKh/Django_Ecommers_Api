from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import os

# Create data directory
os.makedirs('data', exist_ok=True)

driver = webdriver.Chrome()
query = 'laptop'
laptop_name = 'macbook'
file = 0

for i in range(1,5):
    # driver.get(f"https://www.amazon.in/s?k={query}+{laptop_name}&i=computers&page={i}&crid=18ZAB0S0IG7BR&qid=1735357839&sprefix=laptop+lenov%2Ccomputers%2C254&ref=sr_pg_{i}")
    driver.get(f'https://www.flipkart.com/search?q={query}+{laptop_name}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off&page={i}')
    elems = driver.find_elements(By.CLASS_NAME,'slAVV4')
    print(f'{len(elems)} it is the lenth of download data')
    
    for elem in elems:
        d = elem.get_attribute('outerHTML')
        with open(f"data/{query}_{file}.html","w",encoding="utf-8") as f:
            f.write(d)
            file +=1

    time.sleep(2)
    
driver.close()
