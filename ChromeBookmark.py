import json
from collections import OrderedDict
from pprint import pprint


# bookmarks = C:\Users\user\AppData\Local\Google\Chrome\User Data\Default\Bookmarks
with open('C:\\Secu\\Bookmarks', 'rt', encoding='UTF8') as f:
    json_data = json.load(f, object_pairs_hook=OrderedDict)

pprint(json_data)

name_list = []  # name 리스트
url_list = []  # url 리스트

'''
for name, title in json_data["roots"].items():
    print("key %s" % json_data[name])
    if name == 'name':
        print("%s = %s" % (name, title))
'''

for i in range(0, len(json_data["roots"]["bookmark_bar"]["children"])):
    try:
        json1 = json_data["roots"]["bookmark_bar"]["children"][i]["name"]  # []이부분에 다른 숫자를 넣으면 다른값이 출력됨
        json2 = json_data["roots"]["bookmark_bar"]["children"][i]["url"]
        if json1 != '':
            name_list.append(json1)
        if json2 != '':
            url_list.append(json2)
    except:
        break

print(name_list)
print(url_list)

