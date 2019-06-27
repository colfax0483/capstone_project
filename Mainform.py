"""
# Chrome History, Chrome Download Filename
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

form_class = uic.loadUiType("MainWindow.ui")[0]
timer = QtCore.QTimer()

class MainGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class MyWindow(MainGUI, QMainWindow, form_class):
    def __init__(self):
        super().__init__()

        self.FileLoad.clicked.connect(self.open_file)


    @pyqtSlot() # 꼭 필요없으나 메모리, 속도에서 약간의 이득
    def open_file(self):
        print("파일찾기 Btn_clicked")
        file_name = QFileDialog.getOpenFileName(self, 'Open File', os.getenv('HOME'))
        print(file_name)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
