
from alkosto import alkostoScrapper
from carulla import carullaScrapper
from dafiti import dafitiScrapper
from falabella import falabellaScrapper
from gef import gefScrapper
from mercadolibre import mercadolibreScrapper
from panamericana import panamericanaScrapper
from utils import pushToElasticSearch, setCategories, setProviders
import json

from velez import velezScrapper

def runScrapersAndCategories():

    products = alkostoScrapper() + carullaScrapper() + dafitiScrapper() + falabellaScrapper() + gefScrapper() + mercadolibreScrapper() + panamericanaScrapper() + velezScrapper()
    print(len(products))

    file = open('products.json', 'w')
    file.write(json.dumps(products))
    file.close()

runScrapersAndCategories()