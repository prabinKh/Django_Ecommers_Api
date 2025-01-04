import os
import pandas as pd
import django
from django.conf import settings
import sys

def setup_django():
    # Add your project to sys.path
    project_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    sys.path.append(project_path)
    
    # Setup Django settings
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoecommersapi.settings')
    django.setup()

def save_products_to_model(folder_name, df):
    # Import the model dynamically
    model_name = ''.join(word.capitalize() for word in folder_name.split('-'))
    module = __import__(f'data_of_everypage.{folder_name}.models', fromlist=[model_name])
    Model = getattr(module, model_name)
    
    # Save each product
    for _, row in df.iterrows():
        product_data = {}
        for column in df.columns:
            field_name = column.lower().replace(' ', '_').replace('/', '_')
            product_data[field_name] = row[column]
        
        Model.objects.create(**product_data)
    
    print(f"Saved {len(df)} products to {model_name} model")

def process_folder(folder_path):
    folder_name = os.path.basename(folder_path)
    csv_files = [f for f in os.listdir(folder_path) if f.endswith('products.csv')]
    
    if csv_files:
        csv_path = os.path.join(folder_path, csv_files[0])
        df = pd.read_csv(csv_path)
        save_products_to_model(folder_name, df)
        return True
    return False

def main():
    setup_django()
    
    base_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data_of_everypage')
    folders = [f for f in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, f))]
    
    for folder_name in folders:
        folder_path = os.path.join(base_dir, folder_name)
        process_folder(folder_path)

if __name__ == "__main__":
    main()