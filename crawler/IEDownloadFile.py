# 미사용 코드 이동 190717 박도현
import sqlite3
import os

def iedownloadfile():
    file = []
    title = []

    select1 = 'SELECT _DownloadPath FROM iedownload_M_ ;'
    select2 = 'SELECT _AccessedTime, _Url, _ResponseHeaders, _WebPageInfo FROM History_L_;'

    #파일 DB 접속
    con = sqlite3.connect('C:\\Users\\Jang\\Desktop\\history.db')
    #cursor 객체 생성
    cur = con.cursor()

    for row in con.execute(select2) :  # 방문한 사이트 타이틀
        if row[3] != '':  # 내용이 없는것 제외
            title.append(row[3][:-1])  #[:-1]은 뒤에 붙는 \x00을 없애주기 위해서

    con.close() #새로운 파일 DB에 접속해주기 위해

    #파일 DB 접속
    con = sqlite3.connect('C:\\Users\\Jang\\Desktop\\iedownload.db')

    for row in con.execute(select1):  # 다운로드 받은 파일
        f = os.path.basename(row[0])  # 파일 추출
        name = os.path.splitext(f)[0]  # 파일명과 확장자 분리 후, 파일명만 저장
        if name != '':  # 내용이 없는것 제외
           file.append(name)


def main():
    print("Select")
    print(title)
    print(file)

if __name__ == '__main__':
    main()



