# from bs4 import BeautifulSoup
# import os
# import pandas as pd
# d = {'title':[],'price':[],'link':[]}
# for file in os.listdir('data'):
#     try:
#         with open (f'data/{file}') as f:
#             html_doc = f.read()
#         soup = BeautifulSoup(html_doc, 'html.parser')
#         t = soup.find('h2')
#         title = t.get_text()
#         l = soup.find('a')
#         link = "https://amazon.in/"+l['href']
#         p = soup.find('span',attrs={'class':'a-price-whole'})
# # filip card calss class="slAVV4"
#         price=p.get_text()
#         print(link)
#         print(title)
#         print(price)

#         d['title'].append(title)
#         d['price'].append(price)
#         d['link'].append(link)
#     except Exception as e:
#         print(e)

# df =pd.DataFrame(d)
# df.to_csv('data.csv')




########################################
# from bs4 import BeautifulSoup
# import os
# import pandas as pd

# d = {
#     'title': [],
#     'price_first': [],
#     'price_second': [],
#     'image_link': [],
#     'product_link': []
# }

# with open('data/dell_laptops_page32.html', encoding='utf-8') as f:
#     html_doc = f.read()

# soup = BeautifulSoup(html_doc, 'html.parser')
# items = soup.find_all('div', class_='item col')

# for item in items:
#     # Get product title
#     title = item.find('a', title=True)['title']
    
#     # Get product and image links
#     product_link = item.find('a')['href']
#     image_link = item.find('img')['src']
    
#     # Get prices
#     price_first = item.find('span', class_='price price-first').text.strip()
#     price_second = item.find('span', class_='price price-second').text.strip()
    
#     # Add to dictionary
#     d['title'].append(title)
#     d['price_first'].append(price_first)
#     d['price_second'].append(price_second)
#     d['image_link'].append(image_link)
#     d['product_link'].append(product_link)

# # Create DataFrame and save to CSV
# df = pd.DataFrame(d)
# df.to_csv('dell_laptops_data.csv', index=False)


##################################################
from bs4 import BeautifulSoup
import os
import pandas as pd

d = {
    'href': [],
    
}

with open('data/dell_laptops_page32.html', encoding='utf-8') as f:
    html_doc = f.read()

soup = BeautifulSoup(html_doc, 'html.parser')
items = soup.find_all('div', class_='item col')

for item in items:
    # Get first href and src
    first_a = item.find('a')
   
    
    href = first_a['href'] if first_a else ''
   
    
    d['href'].append(href)
  

df = pd.DataFrame(d)
df.to_csv('dell_laptops_links.csv', index=False)