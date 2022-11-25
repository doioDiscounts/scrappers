from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from utils import categoryConverter
import os
from dotenv import load_dotenv

def dafitiScrapper():

    load_dotenv()

    driver = webdriver.Chrome(executable_path=os.getenv('CHROMEDRIVER_PATH'))
    products = []

    for pageIndex in range(2):
        for cardIndex in range(50):
            driver.get(f'https://www.dafiti.com.co/precio-especial/?special_price=1&sort=discount&dir=desc&page={pageIndex + 1}')
            driver.refresh()
            time.sleep(1)
            driver.find_elements(By.CSS_SELECTOR, '.itm-product-main-info')[cardIndex].find_element(By.CSS_SELECTOR, '.itm-title').click()
            time.sleep(1)
            try:

                products.append({
                    'title': driver.find_element(By.XPATH, '//*[@id="content"]/section/div[1]/div[2]/h3').text,
                    'discount': driver.find_element(By.XPATH, '//*[@id="percent_box"]').text[1:-1],
                    'link': driver.current_url,
                    'provider': 'Dafiti',
                    'featured': 0,
                    'category': categoryConverter(driver.find_element(By.XPATH, '//*[@id="content"]/div[2]/div[1]/ul/li[2]/a/span').text),
                    'imageLink': driver.find_element(By.XPATH, '//*[@id="prdImage"]').get_attribute('src')
                })
            
            except: pass
    
    driver.quit()
    
    return products