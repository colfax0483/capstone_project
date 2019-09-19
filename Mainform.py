"""
# GUI Main Window
@author: 15_박도현, 장래승, 장성민, 김민태
"""

# -*- coding: utf-8 -*-
# TODO GUI 에러코드 발생후 종료 시 Interpreter 설정에서 Emulate terminal ... 옵션 켜기

import sys
import os
from PyQt5.QtWidgets import *
from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSlot, pyqtSignal, QObject, QEventLoop, Qt, QDate, QTime, QTimer, QThread
from PyQt5 import uic
from ChromeHistory import *
from IeHistory import Iehistory
from Registry import Registry
from Sticky import Note
from unzip import *
from Morpheme import Morpheme

form_class = uic.loadUiType("MainWindow.ui")[0]
timer = QtCore.QTimer()

class MainGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class MyWindow(MainGUI, QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.file_dict = {}
        # 객체 초기화 시 버튼과 기능함수 연결
        self.FileLoad.clicked.connect(self.open_file)
        self.Btn_Analyze.clicked.connect(self.analyze)
        self.Btn_Wordlist.clicked.connect(self.wordlist)

        # tableWidget 아티팩트, 날짜 테이블
        self.tableWidget.setColumnCount(2)
        column_headers = ['Date', 'Artifacts']
        self.tableWidget.setHorizontalHeaderLabels(column_headers)
        self.currentRowCount = self.tableWidget.rowCount()
        self.tableWidget.insertRow(self.currentRowCount)
        self.tableWidget.setItem(self.currentRowCount, 0, QTableWidgetItem("Some Text"))
        self.artilist = [] # 검색한 아티팩트 이름 담을 리스트

        # tableWidget_2 단어, 비율 테이블
        self.tableWidget_2.setColumnCount(2)
        column_headers2 = ['Word', 'Count']
        self.tableWidget_2.setHorizontalHeaderLabels(column_headers2)
        self.currentRowCount2 = self.tableWidget_2.rowCount()
        self.tableWidget_2.insertRow(self.currentRowCount2)
        # self.tableWidget_2.setItem(self.currentRowCount2, 0, QTableWidgetItem("Some Text"))
        self.wordlist = {}


    @pyqtSlot() # 꼭 필요없으나 메모리, 속도에서 약간의 이득
    def open_file(self): # 파일찾기 Btn_clicked
        try:
            self.file_name = QFileDialog.getOpenFileName(self, 'Open File', os.getenv('HOME'))
            path = self.Brw_Dir.setText(self.file_name[0]) # file_name[0] 파일 경로
            strpath = self.Brw_Dir.toPlainText() # None -> str
            unzip = Unzip(strpath)
            self.file_dict = unzip.fopen()
            print(self.file_dict)
        except FileNotFoundError:
            pass

        return self.file_dict

    @pyqtSlot()
    def addrow(self, src):
        for val, key in enumerate(src): # val = 0,1,2,3 ... key=history딕셔너리의 키값(아티팩트)
            self.tableWidget.insertRow(self.currentRowCount) # 새로운 행을(row) 현재행(self.currentRowCount) 다음에 추가
            artitem = QTableWidgetItem(src.get(key)) # 시간
            dateitem = QTableWidgetItem(key) # 방문기록
            self.tableWidget.setItem(self.currentRowCount, 1, artitem) # (행, 열, 방문기록)
            self.tableWidget.setItem(self.currentRowCount, 0, dateitem) # (행, 열, 시간)

    @pyqtSlot()
    def analyze(self):
        print("Analyze Btn Clicked")
        self.tableWidget.clear()  # QListWidget Clear
        self.tableWidget.setRowCount(0)
        self.currentRowCount = self.tableWidget.rowCount()
        self.tableWidget.horizontalHeader().setStretchLastSection(True)

        # 체크박스 구현부분, 새로 만들면 if 추가하면 됨
        if self.chk_Chrome.isChecked() and 'chromehs' in self.file_dict: #체크박스가 체크되었고 file_dict에 파일경로가 있으면
            chrome = Chrome(self.file_dict['chromehs']) # key값으로 value값 가져오기, Chrome 객체선언
            history = chrome.visiturl()
            self.addrow(history)

        if self.chk_Firefox.isChecked() and 'firefox' in self.file_dict:
            firefox = Firefox(self.file_dict['firefox'])
            fhistory = firefox.visiturl()
            self.addrow(fhistory)

        if self.chk_IE.isChecked() and 'ie' in self.file_dict:
             ie = Iehistory(self.file_dict['ie'])
             iehistory = ie.history()
             self.addrow(iehistory)

        if self.chk_Registry.isChecked():
            registry = Registry()
            reglist= registry.selecter()
            for idx in reglist:
                self.tableWidget.insertRow(self.currentRowCount)
                regitem = QTableWidgetItem(idx)  # 레지스트리아티팩트
                self.tableWidget.setItem(self.currentRowCount, 1, regitem)

        if self.chk_Stickymemo.isChecked() and 'stickymemo' in self.file_dict:
            stkmemo = Note(self.file_dict['stickymemo'])
            stkymemo = stkmemo.sticky()
            for idx in stkymemo:
                self.tableWidget.insertRow(self.currentRowCount)
                stkitem = QTableWidgetItem(idx)
                self.tableWidget.setItem(self.currentRowCount, 1, stkitem)
                '''
                시간까지 있을 때 아래의 코드 사용(dictionary)
                self.addrow(stkymemo)
                '''

        column_headers = ['Date', 'Artifacts'] # 헤더명 재설정
        self.tableWidget.setHorizontalHeaderLabels(column_headers)
        row_count = self.tableWidget.rowCount()
        # TODO 현재 행 개수 불러오기; txt list로 넘기기
        for idx in range(row_count):
            text = self.tableWidget.item(idx, 1)
            self.artilist.append(text.text())

        # print(self.artilist)


    @pyqtSlot()
    def wordlist(self):
        # 아티팩트에서 명사 추출해서 나온 횟수 출력
        self.words = Morpheme(self.artilist)
        self.wordlist = self.words.parser()

        for val, key in enumerate(self.wordlist): # val = 0,1,2,3 ... key=history딕셔너리의 키값(아티팩트)
            self.tableWidget_2.insertRow(self.currentRowCount2) # 새로운 행을(row) 현재행(self.currentRowCount) 다음에 추가
            word = QTableWidgetItem(str(self.wordlist[key])) # 단어
            count = QTableWidgetItem(key) # 횟수
            self.tableWidget_2.setItem(self.currentRowCount2, 0, count) # (행, 열, 횟수)
            self.tableWidget_2.setItem(self.currentRowCount2, 1, word) # (행, 열, 단어)


        column_headers2 = ['Word', 'Count'] # 헤더명 재설정
        self.tableWidget_2.setHorizontalHeaderLabels(column_headers2)


    def closeEvent(self, event): # 가비지 콜렉션 정리 후 프로세스 종료하도록 (정상종료를 위해)
        self.deleteLater()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
