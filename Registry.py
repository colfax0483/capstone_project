import winreg


#레지스트리 주소
key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Software\HNC\Hwp\8.0\HwpFrame\RecentFile")
#서브주소가 바뀌면 바꿔줘야됨
for registry in range(len("Software\HNC\Hwp\8.0\HwpFrame\RecentFile")):#레지스트리 주소에서 뽑아오는 함수
    try:
        registry = winreg.EnumValue(key, registry)
        print(registry)
    except:
        break