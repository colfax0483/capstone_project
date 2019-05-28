import sqlite3
import os

class Firefox:
    def __init__(self, firefox): #변수에 아무 값도 입력되지 않았을때, 어떤 값으로 초기화할지 지정해 줄 수 있다.

        self.filename = []
        self.titlename = []
        self.selecter = 0 # 전체 or 다운로드파일 or 방문 기록 선택
        self.firefox = firefox or 'C:\\Users\\Jang\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\0q5fx2ae.default-release\\places.sqlite'
        #self.firefox = "C:\Users\Jang\AppData\Roaming\Mozilla\Firefox\Profiles\<Random>.default-release\places.sqlite"
        # <Random> 값이 존재하는데, 이 값은 Firefox 경로 밑에 profile.ini 파일 아래에 존재

    def webtitle(self, con): #방문한 웹사이트명
        self.select1 = 'SELECT url, title FROM moz_places;' # 방문 사이트

        for row in con.execute(self.select1):  # 방문한 사이트 타이틀
            if row[1] != None:  # 내용이 없는것 제외
                self.titlename.append(row[1])

        print(self.titlename)

    def downloadfile(self, con): #다운로드 파일명
        self.select2 = 'SELECT anno_attribute_id, content FROM moz_annos;' # 다운로드 받은 파일

        for row in con.execute(self.select2):  # 다운로드 받은 파일
            if str(row[0]) != '2':  # 다운로드 url을 갖고 오기위한 moz_places의 place식별자
                # file url 정보와 나머지 정보를 나누어 저장
                f = os.path.basename(row[1])  # 다운로드 받은 파일 추출
                # name = os.path.splitext(f)[0]  # 파일명과 확장자 분리 후, 파일명만 저장
                if f != '':  # 내용이 없는것 제외
                    self.filename.append(f)

        print(self.filename)

    def sqlselecter(self, select):  #sql 파싱을 위해

        con = sqlite3.connect(self.firefox) # 파일 DB에 접속

        if (select == 1):
           self.webtitle(con)

        elif(select == 2):
           self.downloadfile(con)

        #con.close() 프로그램 종료 시 python에서 열려있는 파일의 객체를 자동으로 닫아준다.
        #직접 닫아 주는 것이 좋다. 쓰기모드로 열었던 파일을 닫지 않고 다시 사용할 경우 오류가 발생하기 때문

def main():
    print('0. 전부 분석 1. 방문기록 2. 다운로드 파일')
    select = int(input('숫자를 입력하세요: '))

    path = Firefox('C:\\Users\\Jang\\Desktop\\places.sqlite') #클래스 호출

    if(select == 0) :
        webtitle = path.sqlselecter(1) #클래스 내 sqlselecter 함수 사용
        downloadfile = path.sqlselecter(2)
    elif (select == 1):
        webtitle = path.sqlselecter(1)
    elif (select == 2):
        downloadfile = path.sqlselecter(2)
    else:
        print('Error')

if __name__ == '__main__':
    main()



