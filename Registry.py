import winreg
import os

# 한글 레지스트리

class Hwpoffice:

    def __init__(self):
        self.reg = []

    def hwp2010(self): # 한글2010
        try:
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Software\HNC\Hwp\8.0\HwpFrame\RecentFile") #한글 2010경로
        except FileNotFoundError:
            return
        for registry in range(0, 10):  # 0에서 10까지 반복
            registrykey = winreg.EnumValue(key, registry)
            if registrykey[0].startswith('file'):
                self.reg.append(os.path.basename(registrykey[1].decode('utf-16').encode('utf-8').decode('utf-8')[:-5])) #디코딩 후 불필요한 문자열 제거
        return self.reg

    def hwp2015(self): # 한글2015
        try:
            key2 = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Software\Hnc\Hwp\9.0\HwpFrame_KOR\RecentFile") #한글 2015경로
        except FileNotFoundError:
            return
        for registry2 in range(0, 10):
            registrykey2 = winreg.EnumValue(key2, registry2)
            if registrykey2[0].startswith('file'):
                self.reg.append(os.path.basename(registrykey2[1].decode('utf-16').encode('utf-8').decode('utf-8')[:-5]))
        return self.reg

    def word2016(self): # 워드2016
        try:
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Software\\Microsoft\\Office\\16.0\\Word\\File MRU") #워드2016경로
        except FileNotFoundError: #FileNotFoundError뜨면 넘어가기
            return
        try:
            for registry in range(0, 10):  # 0에서 10까지 반복
                registrykey = winreg.EnumValue(key, registry)
                if registrykey[0]:
                    self.reg.append(os.path.basename(registrykey[1][:-5])) #디코딩 후 불필요한 문자열 제거
            return self.reg
        except OSError:
            return

    def excel2016(self): # 엑셀2016
        try:
            key2 = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Software\\Microsoft\\Office\\16.0\\Excel\\File MRU") #엑셀2016경로
        except FileNotFoundError:
            return
        try:
            for registry2 in range(0, 10):
                registrykey2 = winreg.EnumValue(key2, registry2)
                if registrykey2[0]:
                    self.reg.append(os.path.basename(registrykey2[1][:-5]))
            return self.reg
        except OSError:
            return

    def point2016(self): # 파워포인트2016
        try:
            key3 = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Software\\Microsoft\\Office\\16.0\\PowerPoint\\File MRU") #파워포인트2016 경로
        except FileNotFoundError:
            return
        try:
            for registry3 in range(0, 10):
                registrykey3 = winreg.EnumValue(key3, registry3)
                if registrykey3[0]:
                    self.reg.append(os.path.basename(registrykey3[1][:-5]))
            return self.reg
        except OSError:
            return

    def selecter(self):
        self.hwp2010()
        self.hwp2015()
        self.word2016()
        self.excel2016()
        self.point2016()
        return self.reg


def main():
    '''
        print("어떤 항목을 출력할까요?\n1. 한글2010 2. 한글2015")
        select = int(input("숫자를 입력하세요: "))

        hwpregistry = Hwp() # 클래스 호출

        if select == 1:
            aaa = hwpregistry.hwp2010()
            print(aaa)# 클래스안에 함수호출

        elif select == 2:
            hwpregistry.hwp2015()

        else:
            print("잘못 선택 하셨습니다")
    '''

    stry = Hwpoffice()
    regis = stry.selecter()
    print(regis)

if __name__ == '__main__':
    main()
