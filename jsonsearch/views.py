from django.shortcuts import render
import json


def code_search(request):
    with open('jsonsearch/static/product_test.json', 'r') as file:
        data = json.load(file)

    product_code = []
    search_numbers = ['9', '3', '8', '2']
    final_products = set()
    for product in data:
        product_code = str(product.get('productCode', ''))
        for number in search_numbers:
            if str(number) in product_code:
                final_products.add(product_code)

    return render(request, 'main.html', {'final_products': final_products})
