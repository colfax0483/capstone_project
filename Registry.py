import winreg


# 한글 레지스트리


class Hwp:

    def __init__(self):
        self.hwp10 = {}
        self.hwp15 = {}

    def hwp2010(self): # 한글2010
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Software\HNC\Hwp\8.0\HwpFrame\RecentFile") #한글 2010경로
        for registry in range(0, 10):  # 0에서 10까지 반복
            registrykey = winreg.EnumValue(key, registry)
            if registrykey[0].startswith('file'):
                print(registrykey[1].decode('utf-16')[:-5])
        return self.hwp10

    def hwp2015(self): # 한글2015
        key2 = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Software\Hnc\Hwp\9.0\HwpFrame_KOR\RecentFile") #한글 2015경로
        for registry2 in range(0, 10):
            registrykey2 = winreg.EnumValue(key2, registry2)
            if registrykey2[0].startswith('file'):
                print(registrykey2[1].decode('utf-16')[:-5])
        return self.hwp15


def main():
    print("어떤 항목을 출력할까요?\n1. 한글2010 2. 한글2015")
    select = int(input("숫자를 입력하세요: "))

    hwpregistry = Hwp() # 클래스 호출

    if select == 1:
        hwpregistry.hwp2010()# 클래스안에 함수호출

    elif select == 2:
        hwpregistry.hwp2015()

    else:
        print("잘못 선택 하셨습니다")


if __name__ == '__main__':
    main()
