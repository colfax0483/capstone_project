from selenium import webdriver
import time
from bs4 import BeautifulSoup

wd = webdriver.Chrome('chromedriver.exe')
url = 'https://news.naver.com/main/ranking/read.nhn?rankingType=popular_day&oid=015&aid=0004119339&date=20190404&type=1&rankingSectionId=105&rankingSeq=1'
wd.get(url)
time.sleep(3)
text = wd.page_source
# print(text)
soup = BeautifulSoup(text, 'html.parser')

for li in soup.select('#cbox_module > div > div.u_cbox_content_wrap > ul > li'):

    if li.select_one('span[class="u_cbox_contents"]'):
        print(li.select_one('span[class="u_cbox_contents"]').text, end=' ')

    print()

wd.quit()