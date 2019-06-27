from urllib.request import urlopen
from bs4 import BeautifulSoup

data = { }
html = urlopen("https://www.boannews.com/media/o_list.asp")
bs = BeautifulSoup(html, "html.parser")

print(type(bs))
my_titles = bs.select('.news_txt')
print(my_titles)

for title in my_titles:
    print(title.text)

print("----------------")

for i in bs.find_all('div', {'class': 'news_list'}):
    title = i.select('.news_txt')[0].text
    link = i.select('a')[0].get('href')
    print(title)
    print("https://www.boannews.com" + link)
    data[title] = "https://www.boannews.com" + link

print(data)
