import pandas as pd
import numpy as np
import requests
import json
from time import sleep
import warnings 
warnings.filterwarnings('ignore')

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
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Executa o navegador em segundo plano
    driver=webdriver.Chrome(service=service, options=chrome_options) #, options=chrome_options
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

links = get_links(5)
print(links)
