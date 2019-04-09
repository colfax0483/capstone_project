from selenium import webdriver
import time
from bs4 import BeautifulSoup

path = "chromedriver.exe"

driver = webdriver.Chrome(path)
driver.get('https://entertain.v.daum.net/v/20190406115446529')
time.sleep(3)

html = driver.page_source
# print(text)
soup = BeautifulSoup(html, 'html.parser')

titles = soup.select('#alex-area > div > div > div > div > ul > li > div > .desc_text')

for cover in titles:
    print(cover.get_text())