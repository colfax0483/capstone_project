import sqlite3

class Note:

    def __init__(self):
        self.nonote = []

    def sqlcc(self):

        cur = sqlite3.connect("C:\\Users\\user\\AppData\\Local\Packages\\Microsoft.MicrosoftStickyNotes_8wekyb3d8bbwe\\LocalState\\plum.sqlite")
        # 스티커메모 경로 C:\Users\user\AppData\Local\Packages\Microsoft.MicrosoftStickyNotes_8wekyb3d8bbwe\LocalState\plum.sqlite
        return cur

    def test(self):
        c = Note.sqlcc(self)
        self.sql1 = "SELECT Text From Note;"


        for row in c.execute(self.sql1):
            self.nonote.append(row[0][41:])
        return self.nonote


def main():

    aaa=Note()
    bbb=aaa.test()
    print(bbb)

if __name__ == '__main__':
    main()


