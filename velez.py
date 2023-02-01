import requests
from utils import categoryConverter

def velezScrapper():

    url = "https://www.velez.com.co/api/catalog_system/pub/products/search/"
    products = []

    response = requests.get(url)

    for product in response.json():
        try:
            if round(100 - (product['items'][2]['sellers'][0]['commertialOffer']['Installments'][0]['Value'] * 100 / product['items'][0]['sellers'][0]['commertialOffer']['Price'])) > 49:
                products.append({
                    'title': product['productName'],
                    'discount': round(100 - (product['items'][2]['sellers'][0]['commertialOffer']['Installments'][0]['Value'] * 100 / product['items'][0]['sellers'][0]['commertialOffer']['Price'])),
                    'imageLink': product['items'][0]['images'][0]['imageUrl'],
                    'link': product['link'],
                    'provider': 'Velez',
                    'category': categoryConverter(product['categories'][0].split('/')[2]),
                    'featured': 0
                })
        except: pass
    
    return products

print(velezScrapper())