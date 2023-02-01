from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from utils import categoryConverter
import os
from dotenv import load_dotenv
import re

def mercadolibreScrapper():

    load_dotenv()

    driver = webdriver.Chrome(executable_path=os.getenv('CHROMEDRIVER_PATH'))
    products = []

    for page in range(15):

        driver.get(f'https://www.mercadolibre.com.co/ofertas?container_id=MCO779366-1&page={page + 1}')

        images = driver.find_elements('css selector', "img[data-src]")
        for image in images:
            data_src = image.get_attribute("data-src")
            driver.execute_script(f"arguments[0].setAttribute('src', '{data_src}')", image)
            driver.execute_script("arguments[0].removeAttribute('data-src')", image)

        for product in driver.find_elements('css selector', '.promotion-item.default'):
            try:
                if int(re.search(r'\d+', product.find_element('css selector', '.andes-money-amount__discount').text).group()) > 49:
                    products.append({
                        'title': product.find_element('css selector', '.promotion-item__title').text,
                        'discount': int(re.search(r'\d+', product.find_element('css selector', '.andes-money-amount__discount').text).group()),
                        'link': product.find_element('css selector', '.promotion-item__link-container').get_attribute('href'),
                        'provider': 'Mercadolibre',
                        'featured': 0,
                        'category': categoryConverter(product.find_element('css selector', '.promotion-item__title').text.split()[0]),
                        'imageLink': product.find_element('css selector', '.promotion-item__img').get_attribute('src')
                    })
            except Exception as e:
                print(e)
                continue

    return products
