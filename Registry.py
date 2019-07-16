import winreg
import os

# 한글 레지스트리

class Hwp:

    def __init__(self):
        self.reshwp = []

    def hwp2010(self): # 한글2010
        try:
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Software\HNC\Hwp\8.0\HwpFrame\RecentFile") #한글 2010경로
        except FileNotFoundError:
            return
        for registry in range(0, 10):  # 0에서 10까지 반복
            registrykey = winreg.EnumValue(key, registry)
            if registrykey[0].startswith('file'):
                self.reshwp.append(os.path.basename(registrykey[1].decode('utf-16').encode('utf-8').decode('utf-8')[:-5])) #디코딩 후 불필요한 문자열 제거
        return self.reshwp

    def hwp2015(self): # 한글2015
        try:
            key2 = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Software\Hnc\Hwp\9.0\HwpFrame_KOR\RecentFile") #한글 2015경로
        except FileNotFoundError:
            return
        for registry2 in range(0, 10):
            registrykey2 = winreg.EnumValue(key2, registry2)
            if registrykey2[0].startswith('file'):
                self.reshwp.append(os.path.basename(registrykey2[1].decode('utf-16').encode('utf-8').decode('utf-8')[:-5]))
        return self.reshwp

    def selecter(self):
        self.hwp2010()
        self.hwp2015()
        return self.reshwp


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

    hwpregistry = Hwp()
    reghwp = hwpregistry.selecter()
    print(reghwp)

if __name__ == '__main__':
    main()
