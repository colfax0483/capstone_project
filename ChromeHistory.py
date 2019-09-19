"""
# Chrome History, Chrome Download Filename
@author: 15_박도현, 장래승, 장성민, 김민태
"""
# -*- coding: utf-8 -*-

import sqlite3, datetime
import os, sys, io
import time
from datetime import datetime, timedelta

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

def concat(*args, sep=","):
    return sep.join(args)

class Mysql:
    def __init__(self, filedir = None):
        self.filename = {}
        self.titlename = {}

    @staticmethod
    def sqlselecter(self): # 여기에 메뉴 확장, 상위 함수 만들어서 기능 확장시키기
        try:
            cur = sqlite3.connect(self.historyfile, timeout=10)
            return cur
        except:
            print("sql error occured")
        #finally:
            #cur.close()

class Chrome(Mysql):
    def __init__(self, historyfile = None):
        super(__class__,self).__init__(historyfile)  # 부모클래스 init 메서드 상속
        self.selecter = 0  # 다운로드파일, 방문 기록 선택
        self.historyfile = historyfile or 'C:\\Users\\ADMIN\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\History'
        # self.historyfile = 'C:\\Users\\ADMIN\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\History'

    @staticmethod
    def fixdate(timestamp): # 시간 변환
        timestamp = timestamp
        #To convert, we create a datetime object for Jan 1 1601...
        epoch_start = datetime(1601,1,1)
        delta = timedelta(microseconds=int(timestamp))
        forsecond = epoch_start + delta
        return forsecond.strftime("%Y-%m-%d %H:%M:%S")

    def downloadfile(self, c): # 다운로드 파일(시간, 경로, 크기)
        self.selectStatement = 'SELECT target_path, referrer, start_time, end_time, received_bytes FROM downloads;'

        for row in c.execute(self.selectStatement):
            # print ("Download:",row[0])
            downdate = str(fixDate(row[2]))
            if str(row[4]) != 0: #SIZE==0 다운로드 하지 않은 파일
                base = os.path.basename(row[0])
                m = os.path.splitext(base)[0]
                if m != '': # 파일명이 없는 파일 제외
                    self.filename[m] = downdate

        return self.filename

    def visiturl(self): # 방문한 사이트 타이틀, URL
        c = Mysql.sqlselecter(self)
        self.selectStatement2 = 'SELECT visits.visit_time, urls.url, urls.title FROM visits, urls WHERE visits.url=urls.id;'

        for row in c.execute(self.selectStatement2):  # 방문한 사이트 타이틀
            # print(str(fixDate(row[0])),"\n\tURL: ", str(row[1]), "\n\tTITLE: ", row[2])
            sitelist = ['YouTube', 'NAVER', 'Google', 'Daum']
            title = row[2].replace(" : 네이버 통합검색", "")
            title = row[2].replace("- Google 검색","")

            title = row[2].rsplit('-' ,1)[0]
            title = row[2].rsplit(':', 1)[0]

            visitdate = str(Chrome.fixdate(row[0]))

            for i in sitelist:
                if i in row[2]:
                    title = row[2].replace(i,"")

            if title != '': # 내용이 없는것 제외
                self.titlename[visitdate] = title
               # print(title)
                ''' print ("\tFrom:",str(row[1]))
                    print ("\tStarted:",str(fixDate(row[2])))
                    print ("\tFinished:",str(fixDate(row[3])))
                    print ("\tSize:",str(row[4]))
                '''

        # print(self.titlename)
        return self.titlename

class Firefox(Mysql):
    def __init__(self, historyfile = None): #변수에 아무 값도 입력되지 않았을때, 어떤 값으로 초기화할지 지정해 줄 수 있다.
        super(__class__, self).__init__(historyfile)
        self.title = {}
        self.file = {}
        self.selecter = 0  # 전체 or 다운로드파일 or 방문 기록 선택
        self.firefox = firefox or 'C:\\Users\\Jang\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\kuaxamep.default-release\\places.sqlite'
        # self.firefox = "C:\Users\Jang\AppData\Roaming\Mozilla\Firefox\Profiles\<Random>.default-release\places.sqlite"
        # <Random> 값이 존재하는데, 이 값은 Firefox 경로 밑에 profile.ini 파일 아래에 존재

    def datetime(self, timestamp):  # 시간 변환
        timestamp = timestamp
        visit_time = datetime.datetime(1970, 1, 1, 9) + datetime.timedelta(microseconds=int(timestamp))
        return visit_time

    def webtitle(self, con):  # 방문한 웹사이트명
        self.select1 = 'SELECT moz_places.url, moz_places.title, moz_historyvisits.visit_date FROM moz_places, moz_historyvisits WHERE moz_places.id = moz_historyvisits.place_id;'  # 방문 사이트

        for row in con.execute(self.select1):  # 방문한 사이트 타이틀
            titledate = str(self.datetime(row[2]))
            visit = row[1]

            if visit != None:  # 내용이 없는것 제외
                self.title[visit] = titledate

        print(self.title)

    def downloadfile(self, con):  # 다운로드 파일명
        self.select2 = 'SELECT anno_attribute_id, content, dateAdded FROM moz_annos;'  # 다운로드 받은 파일

        for row in con.execute(self.select2):  # 다운로드 받은 파일
            downdate = str(self.datetime(row[2]))

            if str(row[0]) != '2':  # 다운로드 url을 갖고 오기위한 moz_places의 place식별자. file url 정보와 나머지 정보를 나누어 저장
                down = os.path.basename(row[1])  # 다운로드 받은 파일 추출
                # name = os.path.splitext(down)[0]  # 파일명과 확장자 분리 후, 파일명만 저장
                if down != None:  # 내용이 없는것 제외
                    self.file[down] = downdate

        print(self.file)

def main():
    print("어떤 항목을 출력할까요?\n0. 전부 분석 1. 방문기록 2. 다운로드 파일")
    select = int(input("숫자를 입력하세요: "))

    startTime = time.time()
    chrome = Chrome('D:\\GitProject\\capstone_private\\History')
    # foxpath = Firefox('C:\\Users\\Jang\\Desktop\\places.sqlite') #클래스 호출

    if (select == 0):
        history = chrome.visiturl()

        downloadfile = chrome.sqlselecter(2)
        print(history)
        print(downloadfile)
    elif (select == 1):
        history = chrome.visiturl()
        print(list(history.keys()))
        print(list(history.values()))
    elif (select == 2):
        downloadfile = chrome.sqlselecter(2)
        print(downloadfile)
    else:
        print("잘못 선택")

    endTime = time.time()
    resultTime = round(endTime - startTime, 5)
    print("\nProcessing Time : %ssec." % resultTime)
''' 
    # Firefox 아티팩트 불러올 때 주석 해제하고 테스트
    if(select == 0) :
        webtitle = path.sqlselecter(1) #클래스 내 sqlselecter 함수 사용
        downloadfile = path.sqlselecter(2)
    elif (select == 1):
        webtitle = path.sqlselecter(1)
    elif (select == 2):
        downloadfile = path.sqlselecter(2)
    else:
        print('Error')
'''

if __name__ == '__main__':
    main()
