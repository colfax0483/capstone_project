# 미사용 코드 이동 190717 박도현
# Registry.py로 병합됨
import winreg
import os

# 오피스 레지스트리

class Office:

    def __init__(self):
        self.regoffice = []

    def word2016(self): # 워드2016
        try:
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Software\\Microsoft\\Office\\16.0\\Word\\File MRU") #워드2016경로
        except FileNotFoundError: #FileNotFoundError뜨면 넘어가기
            return
        try:
            for registry in range(0, 10):  # 0에서 10까지 반복
                registrykey = winreg.EnumValue(key, registry)
                if registrykey[0]:
                    self.regoffice.append(os.path.basename(registrykey[1][:-5])) #디코딩 후 불필요한 문자열 제거
            return self.regoffice
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
                    self.regoffice.append(os.path.basename(registrykey2[1][:-5]))
            return self.regoffice
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
                    self.regoffice.append(os.path.basename(registrykey3[1][:-5]))
            return self.regoffice
        except OSError:
            return

    def selecter(self):
        self.word2016()
        self.excel2016()
        self.point2016()
        return self.regoffice


def main():
    hwpregistry = Office()
    reghwp = hwpregistry.selecter()
    print(reghwp)

if __name__ == '__main__':
    main()
