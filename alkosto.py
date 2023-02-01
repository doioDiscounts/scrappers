import requests
from utils import categoryConverter

def alkostoScrapper():

    products = []
    url = "https://qx5ips1b1q-dsn.algolia.net/1/indexes/*/queries?x-algolia-agent=Algolia%20for%20JavaScript%20(4.5.1)%3B%20Browser%20(lite)%3B%20instantsearch.js%20(4.40.3)%3B%20JS%20Helper%20(3.8.0)&x-algolia-api-key=04636813b7beb6abd08a7e35f8c880a1&x-algolia-application-id=QX5IPS1B1Q"
    data = {
    "requests": [
        {
            "indexName": "alkostoIndexAlgoliaPRD",
            "params": "hitsPerPage=1000"
        }
    ]
}

    response = requests.post(url, json=data)

    for product in response.json()['results'][0]['hits']:
        if 100 - (product['lowestprice_double'] * 100 / product['pricevalue_cop_double']) > 49:
            products.append({
                'title': product['name_text_es'],
                'discount': 100 - (product['lowestprice_double'] * 100 / product['pricevalue_cop_double']),
                'imageLink': f'https://www.alkosto.com{product["img-820wx820h_string"]}',
                'link': f'https://www.alkosto.com{product["url_es_string"]}',
                'provider': 'Alkosto',
                'category': categoryConverter(product['categoryname_text_es_mv'][0]),
                'featured': 0
            })

    return products