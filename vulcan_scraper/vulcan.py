from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

#configure webdriver to use chrome broswer
driver = webdriver.Chrome(executable_path="")

#store the articles 
articles =[]

driver.get('https://vulcanpost.com/category/news/')
content = driver.page_source
print(content)


