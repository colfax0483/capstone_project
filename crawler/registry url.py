# 미사용 코드 이동 190717 박도현

import winreg

#최근 url검색 기록 레지스트리

class Regurl:

    def __init__(self):
        self.regurl = []

    def url(self):
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Software\Microsoft\Internet Explorer\TypedURLs") # url레지스트리 주소
        for registry in range(0, 10):  # 0에서 10까지 반복
            registrykey = winreg.EnumValue(key, registry)
            if registrykey[0]:
                self.regurl.append(registrykey[1])
        return self.regurl



def main():
    urlregistry = Regurl()
    urlkey = urlregistry.url()
    print(urlkey)

if __name__ == '__main__':
    main()
