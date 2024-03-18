import pandas as pd
import numpy as np
import requests
import json
from time import sleep
import warnings 
warnings.filterwarnings('ignore')
import asyncio
from time import sleep

import asyncio
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

"""
 Second way --- using the "webdriver-manager"
 we will be able to always download the latest version of the "chromedriver" 
 using our Google Chrome version as a reference.
"""   

def get_links(number_of_pages):
    service=Service(ChromeDriverManager().install())
    driver=webdriver.Chrome(service=service) #, options=chrome_options
    #allow us to navigate trough any page and to open a html archive in our pc.
    #driver.get(r"https://www.zolo.ca/")
    list_links=[]
    for page in range(1, number_of_pages + 1):
        #print(len(list_links))
        try:
            #define the link of the current page to be opened.'
            current_page = 'https://www.zolo.ca/toronto-real-estate/apartments-for-rent/page-'+str(page)
            #open a page based on the link formed.
            driver.get(current_page)
            #gets all the articles to a list.
            articles = driver.find_elements(By.TAG_NAME, 'article')
            #inside of each article it is looking for the "a hef" where we got the link to the detailed page.
            for article in articles:
                try:
                    link = article.find_element(By.TAG_NAME, 'a').get_attribute('href')
                    list_links.append(link)
                    #print(link)
                except:
                    continue
            list_links2 = []
            #best order of elements -> ID > XPATH > CLASS_NAME
            sleep(0.2)
            #creating the dataframe to input into sheets.
            df_links = pd.DataFrame(columns=['links_zolo'], data=list_links)

            #removing link duplicates.
            df_links.drop_duplicates(inplace=True)
        except:
            continue
    driver.quit()
    return df_links

df_links = get_links(5)
print(df_links)

df_links.head()

#async def fetch_data(df_links):
service=Service(ChromeDriverManager().install())
driver=webdriver.Chrome(service=service) #, options=chrome_options

for link in df_links['links_zolo']:
    #link = 'https://www.zolo.ca/toronto-real-estate/85-mcmahon-drive/2809'
    driver.get(link)

    try:
        dados_detalhados_cabecalho = driver.find_element(By.XPATH,"/html/body/section[2]/div/div/section[2]/section[1]/div").text
    except NoSuchElementException:
        dados_detalhados_cabecalho = None
    # price
    try:
        price = driver.find_element(By.XPATH,"/html/body/section[2]/div/div/section[2]/section[1]/div").text
    except NoSuchElementException:
        price = None
    # address
    try:
        address = driver.find_element(By.XPATH, '/html/body/section[2]/div/div/section[1]/section[1]/h1').text
    except:
        address = None

    try:
        city = driver.find_element(By.XPATH, '/html/body/section[2]/div/div/section[1]/section[1]/div/a[1]').text
    except:
        city = None

    try:
        size = driver.find_element(By.XPATH, '/html/body/section[2]/div/div/section[2]/section[2]/ul/li[3]/span').text
    except:
        size = None

    try:
        status = driver.find_element(By.XPATH, '/html/body/section[2]/div/div/section[3]/div/div[1]').text
    except:
        status = None

    try:
        added = driver.find_element(By.XPATH, '/html/body/section[2]/div/div/section[7]/section/div[2]/dl[1]/dd/span').text
    except:
        added = None
    

    
    print(price)
    print(address)
    print(city)
    print(size)
    print(status)
    print(added)
    print('')


#asyncio.run(fetch_data(df_links))


