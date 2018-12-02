#!/usr/bin/env python3.6.3
# -*- coding: UTF-8 -*-

import sys
import time
import requests
import re
import random
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QMessageBox
from bar import Ui_MainWindow


class go_Thread(QThread):  # create a thread to avoid the ui dead
    stop_signal = pyqtSignal()

    def __init__(self, go):
        QThread.__init__(self)
        self.go = go
        self.stop_flag = False

    def stop(self):
        self.stop_flag = True
        self.run()

    def run(self):
        # print('stop_flag : {}'.format(self.stop_flag))
        if self.stop_flag == False:
            self.go()
        else:
            self.stop_signal.emit()


class progress_Thread(QThread):  # create a thread to avoid the ui dead
    update = pyqtSignal(int, int, int)

    def __init__(self, bar_value, ok_job_count, total_job_count):
        QThread.__init__(self)
        self.bar_value = bar_value
        self.ok_job_count = ok_job_count
        self.total_job_count = total_job_count

    def __del__(self):
        self.wait()

    def run(self):  # 發送訊號
        self.update.emit(self.bar_value, self.ok_job_count,
                         self.total_job_count)


class MyForm(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyForm, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle('ProgressBar-Test')
        self.total_job_count = 10000
        self.ok_job_count = 0
        self.startButton.clicked.connect(self.start)  # 連結開始按鈕
        # self.exitButton.clicked.connect(self.stop_work)  # stop thread

    def go(self):
        while True:
            self.bar_value = (self.ok_job_count /
                              self.total_job_count) * 100  # 設定進度條進度
            try:
                self._progress_Thread = progress_Thread(
                    self.bar_value, self.ok_job_count, self.total_job_count)
                self._progress_Thread.update.connect(
                    self.set_labels)
                self._progress_Thread.start()
            except Exception as e:
                print(e)

            if self.ok_job_count == self.total_job_count:
                self._progress_Thread.wait()  # 確定子進程都結束了才退出
                self._progress_Thread.quit()
                # 如果為 True，代表執行完 run 函式的時候，線程即退出
                print(self._progress_Thread.isFinished())
                print('The progress_Thread is finished!')
                print('Done')
                break
            self.ok_job_count += 1

    def start(self):
        self.ok_job_count = 0
        try:
            self._go_Thread = go_Thread(
                self.go)
            # when stop_flag == True, all threads are done!
            self._go_Thread.stop_signal.connect(self.done)
            self._go_Thread.start()
        except Exception as e:
            print(e)

    def done(self):
        print(self._go_Thread.isFinished())
        print('The go_Thread is finished!')
        print('Done!')

    def stop_work(self):  # 進入 stop 函數，go_thread 隨即停止。
        self._go_Thread.stop()

    # set progressBar and ok_job label and total_job label
    def set_labels(self, bar_value, ok_job_count, total_job_count):
        self.progressBar.setValue(bar_value)
        self.ok_job.setText(str(ok_job_count))
        self.total_job.setText(str(total_job_count))

    def closeEvent(self, event):  # 退出事件
        buttonReply = QMessageBox.question(self, '警告', '你確定要退出嗎?',
                                           QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if buttonReply == QtWidgets.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())
