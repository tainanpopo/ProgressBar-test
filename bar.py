# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bar.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(352, 78)
        # MainWindow.setFixedSize(MainWindow.width(), MainWindow.height())
        # MainWindow.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setMinimumSize(QtCore.QSize(0, 0))
        self.centralwidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.centralwidget.setFont(font)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setStyleSheet(
            "font: 63 18pt \"Bahnschrift SemiBold Condensed\";")
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout_2.addWidget(self.progressBar, 0, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.ok_job = QtWidgets.QLabel(self.centralwidget)
        self.ok_job.setStyleSheet(
            "font: 63 18pt \"Bahnschrift SemiBold Condensed\";")
        self.ok_job.setObjectName("ok_job")
        self.gridLayout.addWidget(self.ok_job, 0, 0, 1, 1)
        self.splash = QtWidgets.QLabel(self.centralwidget)
        self.splash.setStyleSheet(
            "font: 63 18pt \"Bahnschrift SemiBold Condensed\";")
        self.splash.setObjectName("splash")
        self.gridLayout.addWidget(self.splash, 0, 1, 1, 1)
        self.total_job = QtWidgets.QLabel(self.centralwidget)
        self.total_job.setStyleSheet(
            "font: 63 18pt \"Bahnschrift SemiBold Condensed\";")
        self.total_job.setObjectName("total_job")
        self.gridLayout.addWidget(self.total_job, 0, 2, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 2, 1, 1)
        self.startButton = QtWidgets.QPushButton(self.centralwidget)
        self.startButton.setStyleSheet(
            "font: 63 18pt \"Bahnschrift SemiBold Condensed\";")
        self.startButton.setObjectName("startButton")
        self.gridLayout_2.addWidget(self.startButton, 0, 3, 1, 1)
        self.exitButton = QtWidgets.QPushButton(self.centralwidget)
        self.exitButton.setStyleSheet(
            "font: 63 18pt \"Bahnschrift SemiBold Condensed\";")
        self.exitButton.setObjectName("exitButton")
        self.gridLayout_2.addWidget(self.exitButton, 0, 4, 1, 1)
        self.horizontalLayout_2.addLayout(self.gridLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 352, 21))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.ok_job.setText(_translate("MainWindow", "0"))
        self.splash.setText(_translate("MainWindow", "/"))
        self.total_job.setText(_translate("MainWindow", "0"))
        self.startButton.setText(_translate("MainWindow", "Start"))
        self.exitButton.setText(_translate("MainWindow", "Stop"))
