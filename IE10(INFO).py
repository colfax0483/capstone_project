import sys
import pyesedb
import ast
import binascii
import struct
import codecs
from datetime import datetime, timedelta


#WebCacheV24.dat, ESE Database Format
esedb_file = pyesedb.file()
esedb_file.open("C:\\Users\\user\\Desktop\\WebCacheV01.dat")                        #파일 열기
ContainersTable = esedb_file.get_table_by_name("Containers")                        #containers 목록 열기
WebHistoryTables = []
OutputRecord = 0
Output = []
length=[]
result=[]

''''
def convert_timestamp(timestamp):
    epoch_start = datetime(year=1601, month=1,day=1)
    seconds_since_epoch = timestamp/10**7
    return epoch_start + timedelta(seconds=seconds_since_epoch)
'''
#각 정보들은 Container_N 형식의 이름을 가진 테이블에 저장됨
for i in range(0,ContainersTable.get_number_of_records()-1):                        #Containers 테이블 참조, Name 값, Directory 경로로 종류 구분
    Container_Record = ContainersTable.get_record(i)
    ContainerID = Container_Record.get_value_data_as_integer(0)
    Container_Name = Container_Record.get_value_data_as_string(8)
    Container_Directory = Container_Record.get_value_data_as_string(10)
    if Container_Name == "History" and "History.IE5" in Container_Directory:
        WebHistoryTables += [ContainerID]                                           #해당 ContainerID를 historytable에 추가

for i in WebHistoryTables:                                                          #History 테이블 참조
    WebHistoryTable = esedb_file.get_table_by_name("Container_"+ str(i))
    for j in range(0,WebHistoryTable.get_number_of_records()-1):
        WebHistoryRecord = WebHistoryTable.get_record(j)
        Output.append({})
        #if WebHistoryRecord.is_long_value(17):
        #    Output[OutputRecord]["URL"] = WebHistoryRecord.get_value_data_as_long_value(17).get_data_as_string()
        #else:
        Output[OutputRecord]["ResponseHeaders"] = WebHistoryRecord.get_value_data(21)[58:]
        OutputRecord += 1

for i in range(len(Output)):
    #print(binascii.hexlify(Output[i]["ResponseHeaders"]))
    #length = (binascii.hexlify(Output[i]["ResponseHeaders"][0:4]))
    #print(length)
    buffer=int.from_bytes((Output[i]["ResponseHeaders"][0:1]),'big',signed=False)*2                 #buffer=제목 문자열의 크기 (정수형으로 변환)
    #print(buffer)
    length=((Output[i]["ResponseHeaders"][4:buffer+4]))                            #length=제목 문자열의 유니코드값
    #print(length)
    print(length.decode('utf-16'))



