"""
# 2019-05-30
@author: 15_장성민
"""
import json

def chromebookmark():
    # bookmarks = C:\Users\user\AppData\Local\Google\Chrome\User Data\Default\Bookmarks
    with open('C:\\Secu\\Bookmarks', 'rt', encoding='UTF8') as f:
        json_data = json.load(f)

    name_list = []  # name 리스트
    url_list = []  # url 리스트
    for row in range(len(json_data["roots"]["bookmark_bar"]["children"])):  # name과 url를 찾는 함수
        try:
            json1 = json_data["roots"]["bookmark_bar"]["children"][row]["name"]  # []이부분에 다른 숫자를 넣으면 다른값이 출력됨
            json2 = json_data["roots"]["bookmark_bar"]["children"][row]["url"]
            if json1 != '':
                name_list.append(json1)
            if json2 != '':
                url_list.append(json2)
        except:
            break

    print(name_list)
    print(url_list)

def main():
    chromebookmark()

if __name__ == '__main__':
    main()
