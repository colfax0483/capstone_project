import pyesedb
import binascii
from datetime import datetime, timedelta

# WebCacheV24.dat, ESE Database Format
esedb_file = pyesedb.file()
esedb_file.open("C:\\GitProject\\capstone_private\\WebCacheV01.dat")                                                            # 파일 열기
ContainersTable = esedb_file.get_table_by_name("Containers")                                                            # containers 목록 열기
WebHistoryTables = []
OutputRecord = 0
Output = []
length = []

''''
def convert_timestamp(timestamp):
    epoch_start = datetime(year=1601, month=1,day=1)
    seconds_since_epoch = timestamp/10**7
    return epoch_start + timedelta(seconds=seconds_since_epoch)
'''
# 각 정보들은 Container_N 형식의 이름을 가진 테이블에 저장됨
for i in range(0, ContainersTable.get_number_of_records() - 1):                                                         # Containers 테이블 참조, Name 값, Directory 경로로 종류 구분
    Container_Record = ContainersTable.get_record(i)
    ContainerID = Container_Record.get_value_data_as_integer(0)
    Container_Name = Container_Record.get_value_data_as_string(8)
    Container_Directory = Container_Record.get_value_data_as_string(10)
    if Container_Name == "History" and "History.IE5" in Container_Directory:
        WebHistoryTables += [ContainerID]                                                                               # 해당 ContainerID를 historytable에 추가

for i in WebHistoryTables:                                                                                              # History 테이블 참조
    WebHistoryTable = esedb_file.get_table_by_name("Container_" + str(i))
    for j in range(0, WebHistoryTable.get_number_of_records() - 1):
        WebHistoryRecord = WebHistoryTable.get_record(j)
        Output.append({})
        Output[OutputRecord]["ResponseHeaders"] = WebHistoryRecord.get_value_data(21)
        if (binascii.hexlify(Output[OutputRecord]["ResponseHeaders"][0:1])) != b'79':                                   # ResponseHeader값에서 79로 시작하는 값 제외
            Output[OutputRecord]["ResponseHeaders"] = WebHistoryRecord.get_value_data(21)[58:]                          # 0번째 기준 58번째값부터 저장
            buffer = int.from_bytes((Output[OutputRecord]["ResponseHeaders"][0:1]), 'big',signed=False) * 2             # buffer(문자열 크기지정)=58,59번째 한 바이트를 정수로 바꾼후에 곱하기 2
            length = ((Output[OutputRecord]["ResponseHeaders"][4:buffer + 4]))                                          # length(문자열)=61번째 값부터 buffer(문자열크기)+4까지 제목 문자열임
            if length != b'':
                print(length.decode('utf-16'))                                                                              # UTF16으로 디코딩 문자열 출력
            OutputRecord += 1