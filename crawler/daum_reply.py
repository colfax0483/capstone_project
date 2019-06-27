import os
os.chdir(os.path.dirname(__file__))
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

def js_execute(url):
    client = webdriver.PhantomJS(executable_path = 'phantomjs.exe')
    client.get(url)
    bs = BeautifulSoup(client.page_source)
    return bs

def non_js_execute(url):
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_driver_path = 'chromedriver.exe'
    driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=chrome_driver_path)
    driver.get(url)
    bs = BeautifulSoup(driver.page_source, "html.parser")
    return bs

if __name__=='__main__':

    data = []
    url = "https://news.v.daum.net/v/20190416114303621"
    my_titles = non_js_execute(url).select('#alex-area > div > div > div > div> ul > li > div > .desc_txt')
    # print(my_titles)
    # print(len(my_titles))
    for title in my_titles:
        print(title.get_text())
        data.append(title.get_text())

    print(data)