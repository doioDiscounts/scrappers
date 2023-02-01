import requests
from utils import categoryConverter

def falabellaScrapper():

    url = "https://rcom.dynamicyield.com/v3/recommend/8774132"
    data = {"data":[{"wId":"174803"}],"ctx":{"type":"CATEGORY","data":["cat1660941", "cat1360967"]}}
    products = []

    response = requests.post(url, json=data)

    for product in response.json()['response'][0]['slots']:
        if float(product['item']['offer_discount']) > .49:
            products.append({
                'title': product['item']['name'],
                'discount': int(round(float(product['item']['offer_discount']) * 100)),
                'imageLink': product['item']['image_url'],
                'link': product['item']['url'],
                'provider': 'Falabella',
                'category': categoryConverter(product['item']['name'].split()[0]),
                'featured': 0
            })

    return products