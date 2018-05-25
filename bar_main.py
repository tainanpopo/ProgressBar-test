#!/usr/bin/env python3.6.3
# -*- coding: UTF-8 -*-

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from bar import Ui_MainWindow

class MyForm(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyForm, self).__init__(parent)
        self.setupUi(self)
        self.job_count = 10
        self.ok_count = 0
        self.pushButton.clicked.connect(self.run) #連結開始按鈕
            
    def run(self):
        value = (self.ok_count / self.job_count) * 100 #設定進度條進度
        self.progressBar.setValue(value)
        self.ok_count += 1
        
        if self.ok_count > self.job_count:
            sys.exit(0)
        
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())
