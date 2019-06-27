import requests
import urllib.request

client_key = 'wmZKyTWcrrOGBWRVZBFs'
client_secret = 'tmI9O6Mf_c'

encText = urllib.parse.quote("검색할 단어")
naver_url = 'https://openapi.naver.com/v1/search/news.json?query=' + '불금'

header_params = {"X-Naver-Client-Id":client_key, "X-Naver-Client-Secret":client_secret}
# headers= header_params 는 header 변경시에만 필요하고, 그렇지 않으면, requests.get(원하는 URL) 만 해도 됨
response = requests.get(naver_url, headers = header_params)
# 별도 json.loads() 라이브러리 메서드 사용하지 않아도, reqeusts 라이브러리에 있는 json() 메서드로 간단히 처리 가능함
# print(response.json())
# print(response.text)

# HTTP 응답 코드는 status_code 에 저장됨
if(response.status_code == 200):
    data = response.json()
    print(data['items'][0]['title'])
    print(data['items'][0]['link'])
    print(data['items'][0]['description'])
else:
    print("Error Code:" + response.status_code)