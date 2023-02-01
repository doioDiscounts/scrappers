import requests
from utils import categoryConverter

def panamericanaScrapper():

    url = "https://www.panamericana.com.co/_v/segment/graphql/v1?extensions=%7B%22persistedQuery%22%3A%7B%22version%22%3A1%2C%22sha256Hash%22%3A%2267d0a6ef4d455f259737e4edb1ed58f6db9ff823570356ebc88ae7c5532c0866%22%2C%22sender%22%3A%22vtex.store-resources%400.x%22%2C%22provider%22%3A%22vtex.search-graphql%400.x%22%7D%2C%22variables%22%3A%22eyJoaWRlVW5hdmFpbGFibGVJdGVtcyI6ZmFsc2UsInNrdXNGaWx0ZXIiOiJBTEwiLCJzaW11bGF0aW9uQmVoYXZpb3IiOiJkZWZhdWx0IiwiaW5zdGFsbG1lbnRDcml0ZXJpYSI6Ik1BWF9XSVRIT1VUX0lOVEVSRVNUIiwicHJvZHVjdE9yaWdpblZ0ZXgiOmZhbHNlLCJtYXAiOiJwcm9kdWN0Q2x1c3RlcklkcyIsInF1ZXJ5IjoiNjg4MSIsIm9yZGVyQnkiOiJPcmRlckJ5QmVzdERpc2NvdW50REVTQyIsImZyb20iOjAsInRvIjoxMSwic2VsZWN0ZWRGYWNldHMiOlt7ImtleSI6InByb2R1Y3RDbHVzdGVySWRzIiwidmFsdWUiOiI2ODgxIn1dLCJmYWNldHNCZWhhdmlvciI6IlN0YXRpYyIsImNhdGVnb3J5VHJlZUJlaGF2aW9yIjoiZGVmYXVsdCIsIndpdGhGYWNldHMiOmZhbHNlfQ%3D%3D%22%7D"
    products = []

    response = requests.get(url)

    for product in response.json()['data']['productSearch']['products']:
        if 100 - (product['priceRange']['sellingPrice']['highPrice'] * 100 / product['priceRange']['listPrice']['highPrice']) > 49:
            products.append({
                'title': product['productName'],
                'discount': round(100 - (product['priceRange']['sellingPrice']['highPrice'] * 100 / product['priceRange']['listPrice']['highPrice'])),
                'imageLink': product['items'][0]['images'][0]['imageUrl'],
                'link': f'https://www.panamericana.com.co{product["link"]}',
                'provider': 'Panamericana',
                'category': categoryConverter(product['categories'][0].split('/')[1]),
                'featured': 0
            })

    return products
