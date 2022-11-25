from selenium import webdriver
from dotenv import load_dotenv
import os
import time
from utils import categoryConverter

load_dotenv()

def falabellaScrapper():

    driver = webdriver.Chrome(executable_path=os.getenv('CHROMEDRIVER_PATH'))
    products = []
    
    driver.get('https://www.falabella.com.co/falabella-co')
    driver.refresh()

    for a in range(7):
        time.sleep(5)
        driver.find_element('xpath', f'/html/body/div[1]/div/div[3]/div/div[2]/div/div/div[{2 + a}]').click()
        for b in range(8):

            time.sleep(5)
            driver.find_element('xpath', f'/html/body/div[2]/main/div/div/section[1]/div[2]/article[{1 + b}]/a/div/img').click()
            time.sleep(5)
            
            for c in range(31):
                try:
                    products.append({
                        'discount': int(driver.find_element('xpath', f'/html/body/div[1]/div/div[2]/div[2]/section[2]/div[2]/div[2]/div[{2 + c}]/div/a/div[2]/div[1]/span[2]').text.partition('%')[0]),
                        'title': driver.find_element('xpath', f'/html/body/div[1]/div/div[2]/div[2]/section[2]/div[2]/div[2]/div[{2 + c}]/div/a/div[1]/div[1]/span[1]/b').text,
                        'imageLink': driver.find_element('xpath', f'/html/body/div[1]/div/div[2]/div[2]/section[2]/div[2]/div[2]/div[{2 + c}]/div/div/div/a/img[1]').get_attribute('src').replace('170', '1500'),
                        'link': driver.find_element('xpath', f'/html/body/div[1]/div/div[2]/div[2]/section[2]/div[2]/div[2]/div[{2 + c}]/div/div/div/a').get_attribute('href'),
                        'provider': 'Falabella',
                        'category': categoryConverter(driver.find_element('xpath', '/html/body/div[1]/div/div[2]/div[2]/section[1]/div[1]/span/h1').text),
                        'featured': 0
                    })
                except: pass
            for c in range(47):
                try:
                    products.append({
                        'discount': int(driver.find_element('xpath', f'/html/body/div[1]/div/div[2]/div[2]/section[2]/div/div[2]/div[{2 + c}]/div/div[1]/div[2]/div/span[2]').text.partition('%')[0]),
                        'title': driver.find_element('xpath', f'/html/body/div[1]/div/div[2]/div[2]/section[2]/div/div[2]/div[{2 + c}]/div/div[2]/a/span[1]/b').text,
                        'imageLink': driver.find_element('xpath', f'/html/body/div[1]/div/div[2]/div[2]/section[2]/div/div[2]/div[{2 + c}]/div/div[1]/div[1]/a/img[1]').get_attribute('src').replace('240', '1500'),
                        'link': driver.find_element('xpath', f'/html/body/div[1]/div/div[2]/div[2]/section[2]/div/div[2]/div[{2 + c}]/div/div[1]/div[1]/a').get_attribute('href'),
                        'provider': 'Falabella',
                        'category': categoryConverter(driver.find_element('xpath', '/html/body/div[1]/div/div[2]/div[2]/section[1]/div[1]/span/h1').text),
                        'featured': 0
                    })
                except: pass

            driver.execute_script("window.history.go(-1)")
        driver.execute_script("window.history.go(-1)")
    
    return products