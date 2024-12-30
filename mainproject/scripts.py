import django 
import os
os.environ["DJANGO_SETTINGS_MODULE"] = "mainproject.settings"
django.setup()
import pandas as pd
import csv
from allproduct.models import *
csv_file_path = os.path.join(os.path.dirname(__file__), "flipkart_com-ecommerce_sample.csv")
with open(csv_file_path, mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)  
    print(reader)
    for row in reader:
        product_name = row['product_name']
        product_image = eval(row['image'])[0]
        category_tree = eval(row["product_category_tree"])

        category = category_tree[0].split('>>')[0].strip('[]"')
        description = row['description']
        price = float(row["retail_price"]) if row['retail_price'] else 0.0

        print(
            product_name,
            product_image,
            category,
            description,
            price,
        )

        Product.objects.update_or_create(
            product_name = product_name,

            defaults={
                'product_image': product_image,
                'category': category,
                'description': description,
                'price': price,

            }
        )
print("product imported sucessfully !")





# from  sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.metrics.pairwise import cosine_similarity
# from allproduct.models import *

# def get_similar_products(product_id,top_n = 10):
#     vectorize = TfidfVectorizer(stop_words='english')
#     product_descriptions = Product.objects.all().values_list('description',flat=True)
#     tfid_matrix = vectorize.fit_transform(product_descriptions)
#     target_product = Product.objects.get(id = product_id)
#     all_product = list(Product.objects.all())
#     target_index = all_product.index(target_product)
#     cosine_sim = cosine_similarity(tfid_matrix[target_index],tfid_matrix).flatten()
#     similar_indices = cosine_sim.argsort()[:-top_n-1:-1][::-1]
#     # print(type(similar_indices))
#     # print((similar_indices))
#     similar_indices = [i for i in similar_indices if i != target_index]

#     similar_product = []
#     for idx in similar_indices:
#         similar_product.append(all_product[idx])
#     return similar_product

# print(get_similar_products(2616))