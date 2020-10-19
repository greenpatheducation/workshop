from bs4 import BeautifulSoup
import sys
import csv
import os
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException

url="https://www.goat.com/sneakers"
prod_links=[]
def getLinks(soup):
    #Get Product Links
    print("Product Links")
    for k in soup.find_all('div',attrs={'class':'filter-results-area'}):
        for img_link in k.find_all('a'):
            prod_links.append(img_link.get('href'))
    return sorted(prod_links)
if __name__=="__main__":
    getLinks(soup)
