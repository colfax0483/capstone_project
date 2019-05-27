"""
# Chrome History, Chrome Download Filename
@author: 15_박도현, 장래승, 장성민
"""
# -*- coding: utf-8 -*-

import sqlite3, datetime
import os, sys, io
import time

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

def concat(*args, sep=","):
    return sep.join(args)

class Chrome:
    def __init__(self,  select, historyfile = None):
        self.filename = []
        self.titlename = []
        self.selecter = 0 # 다운로드파일, 방문 기록 선택
        self.historyfile = historyfile or 'C:\\Users\\ADMIN\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\History'
        # self.historyfile = 'C:\\Users\\ADMIN\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\History'

    def __iter__(self):
        return self

    def fixdate(self, timestamp): # 시간 변환
        self.timestamp = timestamp
        #To convert, we create a datetime object for Jan 1 1601...
        self.epoch_start = datetime.datetime(1601,1,1)
        #create an object for the number of microseconds in the timestamp
        self.delta = datetime.timedelta(microseconds=int(self.timestamp))
        #and return the sum of the two.
        return self.epoch_start + self.delta

    def downloadfile(self, c): # 다운로드 파일(시간, 경로, 크기)
        self.selectStatement = 'SELECT target_path, referrer, start_time, end_time, received_bytes FROM downloads;'

        for row in c.execute(self.selectStatement):
            # print ("Download:",row[0])

            if str(row[4]) != 0: #SIZE==0 다운로드 하지 않은 파일
                base = os.path.basename(row[0])
                m = os.path.splitext(base)[0]
                if m != '': # 파일명이 없는 파일 제외
                    self.filename.append(m)
        print("다운로드 받은 파일 >>> ")
        print(self.filename)


    def visiturl(self, c): # 방문한 사이트 타이틀, URL
        self.selectStatement2 = 'SELECT visits.visit_time, urls.url, urls.title FROM visits, urls WHERE visits.url=urls.id;'

        for row in c.execute(self.selectStatement2):  # 방문한 사이트 타이틀
            # print(str(fixDate(row[0])),"\n\tURL: ", str(row[1]), "\n\tTITLE: ", row[2])
            if row[2] != '': # 내용이 없는것 제외
                self.titlename.append(row[2])

                ''' print ("\tFrom:",str(row[1]))
                    print ("\tStarted:",str(fixDate(row[2])))
                    print ("\tFinished:",str(fixDate(row[3])))
                    print ("\tSize:",str(row[4]))
                '''
        print("방문한 사이트 >>> ")
        print(self.titlename)

    def sqlselecter(self, select): # 여기에 메뉴 확장, 상위 함수 만들어서 기능 확장시키기
        try:
            cur = sqlite3.connect(self.historyfile, timeout=10)
            if (select == 1):
                self.visiturl(cur)

            elif(select == 2):
                self.downloadfile(cur)
        except:
            print("sql error occured")
        finally:
            cur.close()


def main():
    print("어떤 항목을 출력할까요?\n0. 전부 분석 1. 방문기록 2. 다운로드 파일")
    select = int(input("숫자를 입력하세요: "))

    startTime = time.time()
    r = Chrome(select, 'C:\\History')

    if (select == 0):
        history = r.sqlselecter(1)
        downloadfile = r.sqlselecter(2)
    elif (select == 1):
        history = r.sqlselecter(1)
    elif (select == 2):
        downloadfile = r.sqlselecter(2)
    else:
        print("잘못 선택")

    endTime = time.time()
    resultTime = round(endTime - startTime, 5)
    print("\nProcessing Time : %ssec." % resultTime)


if __name__ == '__main__':
    main()
