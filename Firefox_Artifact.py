import sqlite3
import os

file = []
title = []

select1 = 'SELECT url, title FROM moz_places;' # 방문 사이트
select2 = 'SELECT anno_attribute_id, content FROM moz_annos;' # 다운로드 받은 파일

Firefox = 'C:\\Users\\Jang\\Desktop\\places.sqlite'
#FireFox = "C:\Users\Jang\AppData\Roaming\Mozilla\Firefox\Profiles\kuaxamep.default-release\places.sqlite"
# <Random> 값이 존재하는데, 이 값은 Firefox 경로 밑에 profile.ini 파일 아래에 존재

#파일 DB 접속
con = sqlite3.connect(Firefox)

for row in con.execute(select1) :  # 방문한 사이트 타이틀
    if row[1] != None:  # 내용이 없는것 제외
        title.append(row[1])

for row in con.execute(select2):  # 다운로드 받은 파일
    if str(row[0]) != '2': # 다운로드 url을 갖고 오기위한 moz_places의 place식별자
                           # file url 정보와 나머지 정보를 나누어 저장
        f = os.path.basename(row[1])  # 다운로드 받은 파일 추출
        # name = os.path.splitext(f)[0]  # 파일명과 확장자 분리 후, 파일명만 저장
        if f != '':  # 내용이 없는것 제외
            file.append(f)

if __name__=='__main__':
   print(title)
   print(file)




