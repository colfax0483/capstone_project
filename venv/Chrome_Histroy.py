import sqlite3, datetime
import os

filename = []
titlename = []

def fixDate(timestamp):
    #Chrome stores timestamps in the number of microseconds since Jan 1 1601.
    #To convert, we create a datetime object for Jan 1 1601...
    epoch_start = datetime.datetime(1601,1,1)
    #create an object for the number of microseconds in the timestamp
    delta = datetime.timedelta(microseconds=int(timestamp))
    #and return the sum of the two.
    return epoch_start + delta

selectStatement = 'SELECT target_path, referrer, start_time, end_time, received_bytes FROM downloads;' # 다운로드 파일(시간, 경로, 크기)
selectStatement2 = 'SELECT visits.visit_time, urls.url, urls.title FROM visits, urls WHERE visits.url=urls.id;' # 방문한 사이트 타이틀, URL
selectStatement3 = '''SELECT  urls.url AS "NAVIGATED_FROM",  VISITSESSIONS.URL AS "NAVIGATED_TO"
FROM (
    SELECT visits.id AS ID,visits.from_visit AS CHILDSESSION, visits.url AS URLID, urls.url AS URL
    FROM visits, urls
    WHERE visits.url = urls.id) AS VISITSESSIONS, visits, urls
WHERE visits.id = VISITSESSIONS.Parent AND visits.url = urls.id'''

historyFile = 'C:\\History'
# historyFile = 'C:\\Users\\ADMIN\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\History'
c = sqlite3.connect(historyFile, timeout=10)
for row in c.execute(selectStatement):
    # print ("Download:",row[0])

    if str(row[4]) != 0: #SIZE가 0이면 다운로드 하지 않은 파일
        base = os.path.basename(row[0])
        m = os.path.splitext(base)[0]
        if m != '': # 파일명이 없는 파일 제외
            filename.append(m)

''' print ("\tFrom:",str(row[1]))
    print ("\tStarted:",str(fixDate(row[2])))
    print ("\tFinished:",str(fixDate(row[3])))
    print ("\tSize:",str(row[4]))
'''

for row in c.execute(selectStatement2):  # 방문한 사이트 타이틀
    # print(str(fixDate(row[0])),"\n\tURL: ", str(row[1]), "\n\tTITLE: ", row[2])
    if row[2] != '': # 내용이 없는것 제외
        titlename.append(row[2])


if __name__=='__main__':
    print(filename)
    print(titlename)