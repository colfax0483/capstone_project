"""
# 2019-05-30
@author: 15_장성민
"""
import json

# bookmarks = C:\Users\user\AppData\Local\Google\Chrome\User Data\Default\Bookmarks
with open('C:\\Users\\user\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Bookmarks', 'rt', encoding='UTF8') as f:
    json_data = json.load(f)

name_list = []  # name 리스트
url_list = []  # url 리스트
for json in range(len(json_data["roots"]["bookmark_bar"]["children"])):  # name과 url를 찾는 함수
    try:
        json1 = json_data["roots"]["bookmark_bar"]["children"][json]["name"]  # []이부분에 다른 숫자를 넣으면 다른값이 출력됨
        json2 = json_data["roots"]["bookmark_bar"]["children"][json]["url"]
        if json1 != '':
            name_list.append(json1)
        if json2 != '':
            url_list.append(json2)
    except:
        break

print(name_list)
print(url_list)
