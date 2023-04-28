
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service(r"/Users/aniziocp/.cache/selenium/chromedriver/")
driver = webdriver.Chrome(service=service)

