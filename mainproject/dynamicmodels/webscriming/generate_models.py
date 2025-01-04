import os
import pandas as pd
import re


def determine_field_type(column_name):
    column_lower = column_name.lower()
    
    if any(x in column_lower for x in ['image', 'link', 'url', 'src']):
        return 'models.URLField(max_length=500, null=True, blank=True)'
    
    if any(x in column_lower for x in ['price', 'cost', 'amount']):
        return 'models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)'
    
    if any(x in column_lower for x in ['description', 'detail', 'content', 'text']):
        return 'models.TextField(null=True, blank=True)'
        
    if any(x in column_lower for x in ['specification', 'json', 'data']):
        return 'models.JSONField(null=True, blank=True)'
        
    return 'models.CharField(max_length=255, null=True, blank=True)'

def create_model_file(folder_path, df, folder_name):
    model_name = ''.join(word.capitalize() for word in folder_name.split('-'))
    
    model_code = [
        'from django.db import models\n\n',
        f'class {model_name}(models.Model):\n'
    ]
    
    for column in df.columns:
        field_name = column.lower().replace(' ', '_').replace('/', '_')
        field_type = determine_field_type(column)
        model_code.append(f'    {field_name} = {field_type}\n')
    
    model_code.extend([
        '\n    class Meta:\n',
        f'        verbose_name = "{model_name}"\n',
        f'        verbose_name_plural = "{model_name}s"\n\n',
        '    def __str__(self):\n',
        '        return self.product_title if hasattr(self, "product_title") else str(self.id)\n'
    ])
    
    models_path = os.path.join(folder_path, 'models.py')
    with open(models_path, 'w', encoding='utf-8') as f:
        f.write(''.join(model_code))
    print(f"Created models.py for {folder_name}")

def process_folder(folder_path):
    folder_name = os.path.basename(folder_path)
    csv_files = [f for f in os.listdir(folder_path) if f.endswith('products.csv')]
    
    if csv_files:
        csv_path = os.path.join(folder_path, csv_files[0])
        df = pd.read_csv(csv_path)
        print(f"\nProcessing {folder_name}")
        print("Columns after cleaning:", df.columns.tolist())
        create_model_file(folder_path, df, folder_name)
        return True
    return False

def main():
    base_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data_of_everypage')
    folders = [f for f in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, f))]
    
    for folder_name in folders:
        folder_path = os.path.join(base_dir, folder_name)
        process_folder(folder_path)

if __name__ == "__main__":
    main()
