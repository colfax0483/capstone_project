import sqlite3

#파일 DB 접속
con = sqlite3.connect('C:\Secu\history.db')
#cursor 객체 생성
cur = con.cursor()

cur.execute('PRAGMA table_info(History_M_)')
print(cur.fetchall())
cur.execute('SELECT _SyncTime, _Url, _WebPageInfo FROM History_M_')
print(cur.fetchall())

cur.close()
con.close()