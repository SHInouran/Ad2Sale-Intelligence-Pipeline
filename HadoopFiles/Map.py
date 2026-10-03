import sys
import csv
import random
import os
import re

# 1. Path Logic: Get the directory where Map.py lives to find products.csv
script_dir = os.path.dirname(os.path.abspath(__file__))
products_path = os.path.join(script_dir, 'products.csv')

# 2. Function to extract only the age (e.g., "35-44") from the target string
def extract_age(target_string):
    if not target_string:
        return "Unknown"
    # This looks for the pattern of numbers-numbers
    match = re.search(r'\d+-\d+', target_string)
    if match:
        return match.group()
    # Fallback: find any single age number if no range exists
    match_single = re.search(r'\d+', target_string)
    return match_single.group() if match_single else "Unknown"

def load_products(filename):
    """Returns a unique list of products from the product file."""
    products = []
    try:
        with open(filename, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                # Using 'product_name' as per your latest request
                if row['product_name'] not in products:
                    products.append(row['product_name'])
    except Exception as e:
        print(f"Error loading products: {e}", file=sys.stderr)
        # Fallback to prevent random.choice from crashing
        products = ["Generic_Product"]
    return products

# Load the products list once at the start
all_products = load_products(products_path)

# 3. Processing the input from Hadoop / Standard Input
reader = csv.reader(sys.stdin)

for row in reader:
    # Skip empty rows or the header
    if not row or row[0] == "Campaign_ID":
        continue

    try:
        # 1. Extract and Clean Columns
        camp_id   = row[0]
        
        # Apply the age extraction here
        age_only  = extract_age(row[1])
        
        # ensure indices (row[3], row[10], etc.) match file structure
        duration  = row[3]
        channel   = row[4]
        
        # Convert metrics to floats for the Reducer to sum them up later
        clicks    = float(row[10]) if row[10] else 0.0
        impres    = float(row[11]) if row[11] else 0.0
        engage    = float(row[12]) if row[12] else 0.0
        
        # 2. Randomly assign a product
        assigned_product = random.choice(all_products)

        # 3. Construct the Key and Value
        # Key: Campaign_ID
        key = camp_id
        value = (f"{age_only}|{duration}|{assigned_product}|{channel}|"
                 f"{impres}|{engage}|{clicks}")

        # Hadoop output format: Key [TAB] Value
        print(f"{key}\t{value}")

    except (IndexError, ValueError) as e:
        # Skip rows that are missing columns or have bad numbers
        continue