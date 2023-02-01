import requests
from utils import categoryConverter

def carullaScrapper():

    urls = ['https://www.carulla.com/_v/segment/graphql/v1?extensions=%7B%22persistedQuery%22%3A%7B%22version%22%3A1%2C%22sha256Hash%22%3A%2267d0a6ef4d455f259737e4edb1ed58f6db9ff823570356ebc88ae7c5532c0866%22%2C%22sender%22%3A%22vtex.store-resources%400.x%22%2C%22provider%22%3A%22vtex.search-graphql%400.x%22%7D%2C%22variables%22%3A%22eyJoaWRlVW5hdmFpbGFibGVJdGVtcyI6dHJ1ZSwic2t1c0ZpbHRlciI6IkFMTF9BVkFJTEFCTEUiLCJzaW11bGF0aW9uQmVoYXZpb3IiOiJkZWZhdWx0IiwiaW5zdGFsbG1lbnRDcml0ZXJpYSI6Ik1BWF9XSVRIT1VUX0lOVEVSRVNUIiwicHJvZHVjdE9yaWdpblZ0ZXgiOmZhbHNlLCJtYXAiOiJwcm9kdWN0Q2x1c3RlcklkcyIsInF1ZXJ5IjoiOTk1OSIsIm9yZGVyQnkiOiJPcmRlckJ5QmVzdERpc2NvdW50REVTQyIsImZyb20iOjAsInRvIjoxOSwic2VsZWN0ZWRGYWNldHMiOlt7ImtleSI6InByb2R1Y3RDbHVzdGVySWRzIiwidmFsdWUiOiI5OTU5In1dLCJmYWNldHNCZWhhdmlvciI6IlN0YXRpYyIsImNhdGVnb3J5VHJlZUJlaGF2aW9yIjoiZGVmYXVsdCIsIndpdGhGYWNldHMiOmZhbHNlfQ%3D%3D%22%7D', 'https://www.carulla.com/_v/segment/graphql/v1?extensions=%7B%22persistedQuery%22%3A%7B%22version%22%3A1%2C%22sha256Hash%22%3A%2267d0a6ef4d455f259737e4edb1ed58f6db9ff823570356ebc88ae7c5532c0866%22%2C%22sender%22%3A%22vtex.store-resources%400.x%22%2C%22provider%22%3A%22vtex.search-graphql%400.x%22%7D%2C%22variables%22%3A%22eyJoaWRlVW5hdmFpbGFibGVJdGVtcyI6dHJ1ZSwic2t1c0ZpbHRlciI6IkFMTF9BVkFJTEFCTEUiLCJzaW11bGF0aW9uQmVoYXZpb3IiOiJkZWZhdWx0IiwiaW5zdGFsbG1lbnRDcml0ZXJpYSI6Ik1BWF9XSVRIT1VUX0lOVEVSRVNUIiwicHJvZHVjdE9yaWdpblZ0ZXgiOmZhbHNlLCJtYXAiOiJjIiwicXVlcnkiOiJtYXNjb3RhcyIsIm9yZGVyQnkiOiJPcmRlckJ5QmVzdERpc2NvdW50REVTQyIsImZyb20iOjAsInRvIjoxOSwic2VsZWN0ZWRGYWNldHMiOlt7ImtleSI6ImMiLCJ2YWx1ZSI6Im1hc2NvdGFzIn1dLCJmYWNldHNCZWhhdmlvciI6IlN0YXRpYyIsImNhdGVnb3J5VHJlZUJlaGF2aW9yIjoiZGVmYXVsdCIsIndpdGhGYWNldHMiOmZhbHNlfQ%3D%3D%22%7D', "https://www.carulla.com/_v/segment/graphql/v1?extensions=%7B%22persistedQuery%22%3A%7B%22version%22%3A1%2C%22sha256Hash%22%3A%2267d0a6ef4d455f259737e4edb1ed58f6db9ff823570356ebc88ae7c5532c0866%22%2C%22sender%22%3A%22vtex.store-resources%400.x%22%2C%22provider%22%3A%22vtex.search-graphql%400.x%22%7D%2C%22variables%22%3A%22eyJoaWRlVW5hdmFpbGFibGVJdGVtcyI6dHJ1ZSwic2t1c0ZpbHRlciI6IkFMTF9BVkFJTEFCTEUiLCJzaW11bGF0aW9uQmVoYXZpb3IiOiJkZWZhdWx0IiwiaW5zdGFsbG1lbnRDcml0ZXJpYSI6Ik1BWF9XSVRIT1VUX0lOVEVSRVNUIiwicHJvZHVjdE9yaWdpblZ0ZXgiOmZhbHNlLCJtYXAiOiJjIiwicXVlcnkiOiJ2aW5vcy15LWxpY29yZXMiLCJvcmRlckJ5IjoiT3JkZXJCeUJlc3REaXNjb3VudERFU0MiLCJmcm9tIjowLCJ0byI6MTksInNlbGVjdGVkRmFjZXRzIjpbeyJrZXkiOiJjIiwidmFsdWUiOiJ2aW5vcy15LWxpY29yZXMifV0sImZhY2V0c0JlaGF2aW9yIjoiU3RhdGljIiwiY2F0ZWdvcnlUcmVlQmVoYXZpb3IiOiJkZWZhdWx0Iiwid2l0aEZhY2V0cyI6ZmFsc2V9%22%7D"]
    products = []

    for url in urls:

        response = requests.get(url)

        for product in response.json()['data']['productSearch']['products']:
            if round(100 - (product['priceRange']['sellingPrice']['highPrice'] * 100 / product['priceRange']['listPrice']['highPrice'])) > 49:
                products.append({
                    'title': product['productName'],
                    'discount': round(100 - (product['priceRange']['sellingPrice']['highPrice'] * 100 / product['priceRange']['listPrice']['highPrice'])),
                    'imageLink': product['items'][0]['images'][0]['imageUrl'],
                    'link': f'https://www.carulla.com/{product["link"]}',
                    'provider': 'Carulla',
                    'category': categoryConverter(product['categories'][0].split('/')[1]),
                    'featured': 0
                })
        
    return products