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
        driver.get(f'https://www.dafiti.com.co/precio-especial/?special_price=1&sort=discount&dir=desc&page={pageIndex + 1}')
        driver.maximize_window()
        driver.refresh()
        y = 1000
        for timer in range(0,25):
            driver.execute_script("window.scrollTo(0, "+str(y)+")")
            y += 1000  
            time.sleep(1)
        for product in range(50):
            try:
                products.append({
                    'title': driver.find_element(By.XPATH, f'/html/body/div[3]/div[1]/div[2]/div[4]/div[2]/div[3]/section/ul/li[{1 + product}]/div[2]/a[2]/div[3]/p[2]').text,
                    'discount': driver.find_element(By.XPATH, f'/html/body/div[3]/div[1]/div[2]/div[4]/div[2]/div[3]/section/ul/li[{1 + product}]/div[2]/a[2]/div[2]/div').text[1:-1],
                    'link': driver.find_element(By.XPATH, f'/html/body/div[3]/div[1]/div[2]/div[4]/div[2]/div[3]/section/ul/li[{1 + product}]/div[2]/a[2]').get_attribute('href'),
                    'provider': 'Dafiti',
                    'featured': 0,
                    'category': categoryConverter(driver.find_element(By.XPATH, f'/html/body/div[3]/div[1]/div[2]/div[4]/div[2]/div[3]/section/ul/li[{1 + product}]/div[2]/a[2]/div[3]/p[2]').text.split()[0]),
                    'imageLink': driver.find_element(By.XPATH, f'/html/body/div[3]/div[1]/div[2]/div[4]/div[2]/div[3]/section/ul/li[{1 + product}]/div[2]/a[2]/div[1]/ul/li/img').get_attribute('src')
                })
            except: pass
    
    driver.quit()

    return products
