from selenium import webdriver
import os
from dotenv import load_dotenv
from utils import categoryConverter
import time

def linioScrapper():

    load_dotenv()

    driver = webdriver.Chrome(executable_path=os.getenv('CHROMEDRIVER_PATH'))

    driver.get('https://www.linio.com.co/')
    time.sleep(3)
    driver.find_element('xpath','/html/body/div[6]/div[2]/div/div[1]').click()
    

    return

    products = []

    for categoryIndex in range(3, 20):

        try:

            driver.find_element('xpath','//*[@id="open-left-menu"]/div').click()
            driver.find_element('xpath',f'//*[@id="main-menu"]/nav/ul/li[{categoryIndex}]/a').click()
            
            for item in range(1, 50):
                
                try:

                    product = {}

                    if int(driver.find_element('xpath',f'//*[@id="catalogue-product-container"]/div[{item}]/a[1]/div[2]/div[3]/div[1]/span[2]').text[1:-1]) > 40:

                        product['provider'] = 'Linio'
                        product['featured'] = 0
                        product['category'] = categoryConverter(driver.find_element('xpath','/html/body/div[3]/main/div[1]/ol/li[2]/span').text)
                        product['title'] = driver.find_element('xpath',f'//*[@id="catalogue-product-container"]/div[{item}]/a[1]/div[2]/p/span').text
                        product['discount'] = driver.find_element('xpath',f'//*[@id="catalogue-product-container"]/div[{item}]/a[1]/div[2]/div[3]/div[1]/span[2]').text[1:-1]
                        driver.find_element('xpath',f'//*[@id="catalogue-product-container"]/div[{item}]/a[1]/div[2]/p/span').click()
                        product['link'] = driver.current_url
                        product['imageLink'] = driver.find_element('xpath','//*[@id="image-product"]/figure/picture/img').get_attribute('src')
                        if product not in products: products.append(product)
                        driver.back()

                except Exception as e:
                    print(e)
                    pass

        
        except Exception as e:
            print(e)
            pass
    
    driver.quit()

    return products
