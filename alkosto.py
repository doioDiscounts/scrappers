# As soon as it opens, make it full screen

from selenium import webdriver
from dotenv import load_dotenv
import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from utils import categoryConverter

load_dotenv()

def alkostoScrapper():

    driver = webdriver.Chrome(executable_path=os.getenv('CHROMEDRIVER_PATH'))
    action = ActionChains(driver)
    products = []
    driver.get('https://www.alkosto.com/')
    
    for a in range(13):
        for b in range(4):
            action.move_to_element(driver.find_element(By.XPATH, f'/html/body/main/header/div[2]/nav[2]/div[4]/ul[1]/li[{a + 1}]/a')).perform()
            time.sleep(2)
            driver.find_element(By.XPATH, f'/html/body/main/header/div[2]/nav[2]/div[4]/ul[2]/li[{a + 2}]/div[{b + 2}]/a').click()
            driver.get(f'{driver.current_url}?isGrid=true&pageSize=100')
            for n in range(len(driver.find_elements(By.CSS_SELECTOR, '.product__grid--item.product__grid--alkosto'))):
                try:
                    if int(100 - ((int(driver.find_element(By.XPATH, f'/html/body/main/section/section/div/div/ul/li[{n + 1}]/div/div[3]/div[1]/p[2]/span[1]').text.replace('$', '').replace('.', '')) * 100) / int(driver.find_element(By.XPATH, f'/html/body/main/section/section/div/div/ul/li[{n + 1}]/div/div[3]/div[1]/p[1]').text.replace('$', '').replace('.', '')))) > 49:
                        products.append({
                            'discount': int(100 - ((int(driver.find_element(By.XPATH, f'/html/body/main/section/section/div/div/ul/li[{n + 1}]/div/div[3]/div[1]/p[2]/span[1]').text.replace('$', '').replace('.', '')) * 100) / int(driver.find_element(By.XPATH, f'/html/body/main/section/section/div/div/ul/li[{n + 1}]/div/div[3]/div[1]/p[1]').text.replace('$', '').replace('.', '')))),
                            'title': driver.find_element(By.XPATH, f'/html/body/main/section/section/div/div/ul/li[{n + 1}]/div/div[2]/h2/a').text,
                            'imageLink': f"https://www.alkosto.com{driver.find_element(By.XPATH, f'/html/body/main/section/section/div/div/ul/li[{n + 1}]/div/div[1]/div/div/a/img').get_attribute('data-src')}",
                            'link': driver.find_element(By.XPATH, f'/html/body/main/section/section/div/div/ul/li[{n + 1}]/div/div[2]/h2/a').get_attribute('href'),
                            'provider': 'Alkosto',
                            'category': categoryConverter(driver.find_element(By.XPATH, '/html/body/main/section/div[1]/h1').text),
                            'featured': 0
                        })
                except: pass

    driver.quit()

    return products