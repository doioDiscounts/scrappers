import requests
from utils import categoryConverter

def gefScrapper():

    url = "https://www.gef.co/search/resources/api/v2/products?categoryId=3074457345616678176&storeId=10151&langId=-24"
    products = []

    response = requests.get(url)

    for product in response.json()['contents']:
        if round(100 - (float(product['price'][1]['value']) * 100 / float(product['price'][0]['value']))) > 49:
            products.append({
                'title': product['name'],
                'discount': round(100 - (float(product['price'][1]['value']) * 100 / float(product['price'][0]['value']))),
                'imageLink': f'https://www.gef.co{product["thumbnail"]}',
                'link': f'https://www.gef.co{product["seo"]["href"]}',
                'provider': 'Gef',
                'category': categoryConverter(product['thumbnailRaw'].split("/")[5]),
                'featured': 0
            })

    return products