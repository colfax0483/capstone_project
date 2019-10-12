import os
from openpyxl import load_workbook
# openpyxl모듈 다운
# 말뭉치 폴더 경로
path = "C:\\Users\\user\\Downloads\\범죄 말뭉치 검색결과 엑셀"
file_list = os.listdir(path)
print(file_list)
results = []

for file_name_raw in file_list:
    #말뭉치경로 설정후 뒤에 / 붙이기
    file_name = "C:\\Users\\user\\Downloads\\범죄 말뭉치 검색결과 엑셀/" + file_name_raw
    wb = load_workbook(filename=file_name, data_only=True)
    ws = wb['Sheet1']
    result = []
    result.append(file_name_raw)
    for r in ws.rows:
        row_index = r[0].row
        contex = r[1].value #앞문맥 출력
        search = r[2].value #검색어 출력
        back = r[3].value #뒷문맥 출력
        result.append(contex)
        result.append(search)
        result.append(back)
    results.append(result)
print(results)
