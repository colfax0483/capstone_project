import sqlite3

class Note:

    def __init__(self, path = None):
        self.nonote = []
        self.path = path or "C:\\Users\\user\\AppData\\Local\\Packages\\Microsoft.MicrosoftStickyNotes_8wekyb3d8bbwe\\LocalState\\plum.sqlite"
        self.cur = sqlite3.connect(self.path)
        # 스티커메모 경로 C:\Users\user\AppData\Local\Packages\Microsoft.MicrosoftStickyNotes_8wekyb3d8bbwe\LocalState\plum.sqlite

    def sticky(self):
        self.sql1 = "SELECT Text From Note;"

        for row in self.cur.execute(self.sql1):
            self.nonote.append(row[0][41:])
        return self.nonote


def main():

    aaa = Note(path=r'D:\GitProject\capstone_private\ziptest\artifacts\plum.sqlite')
    bbb = aaa.sticky()
    for i in bbb:
        print(i)
    print("len of result : " + str(len(bbb)))

if __name__ == '__main__':
    main()


