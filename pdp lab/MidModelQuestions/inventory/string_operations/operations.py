import re

def perform_string_operations(data):
    print("String Operations and Regular Expressions:\n")

    search_term = "Speakers"
    matching_products = [product for product in data if product['name'].startswith(search_term)]
    print(f"Products starting with 'Speakers': {matching_products}\n")

    category_filter1 = "Electronics"
    electronics_product = [product for product in data if category_filter1 in product['category']]
    print("Electronic Products:", electronics_product,"\n")

    category_filter2 = "Clothing"
    clothing_product = [product for product in data if category_filter2 in product['category']]
    print("Clothing Products:", clothing_product,"\n")

    pattern = re.compile(r'T-Shirt', re.IGNORECASE)
    matching_products = [product for product in data if re.search(pattern, product['name'])]
    print("Matching Products:", matching_products)