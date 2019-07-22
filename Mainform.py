"""
# GUI Main Window
@author: 15_박도현, 장래승, 장성민, 김민태
"""

# -*- coding: utf-8 -*-
import sys
import os
from PyQt5.QtWidgets import *
from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSlot, pyqtSignal, QObject, QEventLoop, Qt, QDate, QTime, QTimer, QThread
from PyQt5 import uic
from ChromeHistory import *
from Registry import Registry
from unzip import *

form_class = uic.loadUiType("MainWindow.ui")[0]
timer = QtCore.QTimer()

class MainGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class MyWindow(MainGUI, QMainWindow, form_class):
    def __init__(self):
        super().__init__()

        # 객체 초기화 시 버튼과 기능함수 연결
        self.FileLoad.clicked.connect(self.open_file)
        self.Btn_Analyze.clicked.connect(self.analyze)


    @pyqtSlot() # 꼭 필요없으나 메모리, 속도에서 약간의 이득
    def open_file(self):
        print("파일찾기 Btn_clicked")
        self.file_name = QFileDialog.getOpenFileName(self, 'Open File', os.getenv('HOME'))
        self.Brw_Dir.setText(self.file_name[0])

        print(self.file_name[0])

        return self.file_name[0]


    @pyqtSlot()
    def analyze(self):
        print("Analyze Btn Clicked")
        self.listWidget.clear()  # QListWidget Clear
        # 파일 경로 확인
        try:
            path = self.Brw_Dir.toPlainText()
        except:
            print("경로가 없거나 아티팩트 파일이 아님 (.zip)")

        # 체크박스 구현부분, 새로 만들면 if 추가하면 됨
        if self.chk_Chrome.isChecked() == True:
            chrome = Chrome(path)
            history = chrome.visiturl()
            for idx in list(history.keys()):
                self.listWidget.addItem(QListWidgetItem(idx))
        if self.chk_Firefox.isChecked() == True:
            firefox = Firefox(path)
            fhistory = firefox.visiturl()
        if self.chk_IE.isChecked() == True:
            pass
        if self.chk_Registry.isChecked() == True:
            registry = Registry()
            reglist= registry.selecter()
            for idx in reglist:
                self.listWidget.addItem(QListWidgetItem(idx))


    def closeEvent(self, event): # 가비지 콜렉션 정리 후 프로세스 종료하도록 (정상종료를 위해)
        self.deleteLater()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
