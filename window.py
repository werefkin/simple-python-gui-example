# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 646)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalWidget = PlotWidget(self.centralwidget)
        self.verticalWidget.setGeometry(QtCore.QRect(10, 0, 871, 541))
        self.verticalWidget.setObjectName("verticalWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 550, 871, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.horizontalLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.startMeasurementButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.startMeasurementButton.setObjectName("startMeasurementButton")
        self.gridLayout.addWidget(self.startMeasurementButton, 0, 0, 1, 1)
        self.stopMeasurementButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.stopMeasurementButton.setObjectName("stopMeasurementButton")
        self.gridLayout.addWidget(self.stopMeasurementButton, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 900, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.startMeasurementButton.setText(_translate("MainWindow", "start measurements"))
        self.stopMeasurementButton.setText(_translate("MainWindow", "stop measurement"))
from pyqtgraph import PlotWidget
