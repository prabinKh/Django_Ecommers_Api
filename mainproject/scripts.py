# import django 
# import os
# os.environ["DJANGO_SETTINGS_MODULE"] = "mainproject.settings"
# django.setup()
# import pandas as pd
# import csv
# from allproduct.models import *
# csv_file_path = os.path.join(os.path.dirname(__file__), "flipkart_com-ecommerce_sample.csv")
# with open(csv_file_path, mode='r', encoding='utf-8') as file:
#     reader = csv.DictReader(file)  
#     print(reader)
#     for row in reader:
#         product_name = row['product_name']
#         product_image = eval(row['image'])[0]
#         category_tree = eval(row["product_category_tree"])

#         category = category_tree[0].split('>>')[0].strip('[]"')
#         description = row['description']
#         price = float(row["retail_price"]) if row['retail_price'] else 0.0

#         print(
#             product_name,
#             product_image,
#             category,
#             description,
#             price,
#         )

#         Product.objects.update_or_create(
#             product_name = product_name,

#             defaults={
#                 'product_image': product_image,
#                 'category': category,
#                 'description': description,
#                 'price': price,

#             }
#         )
# print("product imported sucessfully !")





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










################################

import django
import os
import uuid
import pandas as pd
from django.apps import apps

os.environ["DJANGO_SETTINGS_MODULE"] = "mainproject.settings"
django.setup()

def get_model_fields(model_name, app_name='allproduct'):
    model = apps.get_model(app_name, model_name)
    return [field.name for field in model._meta.fields]

def create_mapping_dict(csv_columns, model_fields):
    mapping = {}
    for csv_col in csv_columns:
        # Convert CSV column name to a format similar to model fields
        formatted_col = csv_col.lower().replace(' ', '_')
        if formatted_col in model_fields:
            mapping[csv_col] = formatted_col
    return mapping

def import_data_with_mapping(csv_file, model_name, app_name='allproduct'):
    # Read CSV
    df = pd.read_csv(csv_file)
    
    # Get model and its fields
    model = apps.get_model(app_name, model_name)
    model_fields = get_model_fields(model_name)
    
    # Create mapping
    mapping = create_mapping_dict(df.columns, model_fields)
    
    # Import data
    for _, row in df.iterrows():
        data_dict = {}
        for csv_col, model_field in mapping.items():
            data_dict[model_field] = row[csv_col]
            
        # Add slug if it exists in model
        if 'slug' in model_fields:
            data_dict['slug'] = f"{row.get('company_name', '')}-{row.get('product_name', '')}-{str(uuid.uuid4())[:8]}"
            
        model.objects.get_or_create(**data_dict)

# Usage example
csv_file_path = "products.csv"
model_name = "AsusLaptops"  # Your model name
import_data_with_mapping(csv_file_path, model_name)
