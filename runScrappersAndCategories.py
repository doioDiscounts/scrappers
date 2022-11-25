
from alkosto import alkostoScrapper
from dafiti import dafitiScrapper
from linio import linioScrapper
from falabella import falabellaScrapper
from utils import pushToElasticSearch, setCategories, setProviders
import json

def runScrapersAndCategories():

    #alkostoProducts = alkostoScrapper()
    # falabellaProducts = falabellaScrapper()
    #dafitiProducts = dafitiScrapper()
    falabellaProducts = falabellaScrapper()
    #linioProducts = linioScrapper()

    #pushToElasticSearch(alkostoProducts, "Alkosto")
    # pushToElasticSearch(falabellaProducts, "Falabella")
    # pushToElasticSearch(dafitiProducts, "Dafiti")
    #pushToElasticSearch(linioProducts, 'Linio')

    file = open('falabella.json', 'a')
    file.write(json.dumps(falabellaProducts))
    file.close()

    #setCategories()

    #setProviders(['Linio'])


runScrapersAndCategories()


