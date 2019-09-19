import pyesedb
import binascii
from datetime import datetime, timedelta


class Iehistory:
    def __init__(self, historyfile = None):
        self.historyfile = historyfile
        # WebCacheV24.dat, ESE Database Format
        self.esedb_file = pyesedb.file()
        self.esedb_file.open('D:\\GitProject\\capstone_private\\WebCacheV01.dat')  # 파일 열기
        self.ContainersTable = self.esedb_file.get_table_by_name("Containers")  # containers 목록 열기
        self.WebHistoryTables = []
        self.OutputRecord = 0
        self.Output = []
        self.result = {}

    def convert_timestamp(self, timestamp):
        epoch_start = datetime(year=1601, month=1,day=1,hour=9)
        seconds_since_epoch = timestamp/10**7
        return (epoch_start + timedelta(seconds=seconds_since_epoch)).strftime("%Y-%m-%d %H:%M:%S")

    def history(self):
        # 각 정보들은 Container_N 형식의 이름을 가진 테이블에 저장됨
        for i in range(0, self.ContainersTable.get_number_of_records() - 1):                                                         # Containers 테이블 참조, Name 값, Directory 경로로 종류 구분
            Container_Record = self.ContainersTable.get_record(i)
            ContainerID = Container_Record.get_value_data_as_integer(0)
            Container_Name = Container_Record.get_value_data_as_string(8)
            Container_Directory = Container_Record.get_value_data_as_string(10)
            if Container_Name == "History" and "History.IE5" in Container_Directory:
                self.WebHistoryTables += [ContainerID]                                                                               # 해당 ContainerID를 historytable에 추가

        for i in self.WebHistoryTables:                                                                                              # History 테이블 참조
            WebHistoryTable = self.esedb_file.get_table_by_name("Container_" + str(i))
            for j in range(0, WebHistoryTable.get_number_of_records() - 1):
                WebHistoryRecord = WebHistoryTable.get_record(j)
                self.Output.append({})
                self.Output[self.OutputRecord]["AccessedTime"] = WebHistoryRecord.get_value_data_as_integer(13)
                self.Output[self.OutputRecord]["ResponseHeaders"] = WebHistoryRecord.get_value_data(21)
                if (binascii.hexlify(self.Output[self.OutputRecord]["ResponseHeaders"][0:1])) != b'79':                                   # ResponseHeader값에서 79로 시작하는 값 제외
                    self.Output[self.OutputRecord]["ResponseHeaders"] = WebHistoryRecord.get_value_data(21)[58:]                          # 0번째 기준 58번째값부터 저장
                    buffer = int.from_bytes((self.Output[self.OutputRecord]["ResponseHeaders"][0:1]), 'big',signed=False) * 2             # buffer(문자열 크기지정)=58,59번째 한 바이트를 정수로 바꾼후에 곱하기 2
                    length = ((self.Output[self.OutputRecord]["ResponseHeaders"][4:buffer + 4]))                                          # length(문자열)=61번째 값부터 buffer(문자열크기)+4까지 제목 문자열임

                    # print((self.convert_timestamp(self.Output[self.OutputRecord]["AccessedTime"])),(length.decode('utf-16').encode('utf-8').decode('utf-8')))  # UTF16으로 디코딩 문자열 출력
                    title = length.decode('utf-16').encode('utf-8').decode('utf-8')[:-1]
                    sitelist = ['YouTube', 'NAVER', 'Google', 'Daum']
                    title = title.replace(" : 네이버 통합검색", "")
                    title = title.replace("- Google 검색", "")

                    title = title.rsplit('-', 1)[0]
                    title = title.rsplit(':', 1)[0]
                    title = title.strip()
                    for i in sitelist:
                        if i in title:
                            title = title.replace(i, "")
                    if title != '':
                        self.result[(self.convert_timestamp(self.Output[self.OutputRecord]["AccessedTime"]))] = title
                self.OutputRecord += 1
        return self.result

def main():
    path = ('D:\\GitProject\\capstone_private\\WebCacheV01.dat')
    ie = Iehistory().history()

    print(ie)

if __name__ == '__main__':
    main()
