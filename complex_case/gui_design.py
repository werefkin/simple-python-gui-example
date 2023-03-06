# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Hypersen(object):
    def setupUi(self, Hypersen):
        Hypersen.setObjectName("Hypersen")
        Hypersen.resize(800, 600)
        Hypersen.setMinimumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtWidgets.QWidget(Hypersen)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.initializeButton = QtWidgets.QPushButton(self.centralwidget)
        self.initializeButton.setObjectName("initializeButton")
        self.horizontalLayout.addWidget(self.initializeButton)
        self.startButton = QtWidgets.QPushButton(self.centralwidget)
        self.startButton.setObjectName("startButton")
        self.horizontalLayout.addWidget(self.startButton)
        self.stopButton = QtWidgets.QPushButton(self.centralwidget)
        self.stopButton.setObjectName("stopButton")
        self.horizontalLayout.addWidget(self.stopButton)
        self.measureButton = QtWidgets.QPushButton(self.centralwidget)
        self.measureButton.setObjectName("measureButton")
        self.horizontalLayout.addWidget(self.measureButton)
        self.gridLayout.addLayout(self.horizontalLayout, 3, 0, 1, 1)
        self.logs = QtWidgets.QTextBrowser(self.centralwidget)
        self.logs.setMaximumSize(QtCore.QSize(16777215, 100))
        self.logs.setObjectName("logs")
        self.gridLayout.addWidget(self.logs, 1, 0, 1, 1)
        self.plotSignal = PlotWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plotSignal.sizePolicy().hasHeightForWidth())
        self.plotSignal.setSizePolicy(sizePolicy)
        self.plotSignal.setMinimumSize(QtCore.QSize(0, 400))
        self.plotSignal.setObjectName("plotSignal")
        self.gridLayout.addWidget(self.plotSignal, 0, 0, 1, 1)
        Hypersen.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Hypersen)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        Hypersen.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Hypersen)
        self.statusbar.setObjectName("statusbar")
        Hypersen.setStatusBar(self.statusbar)

        self.retranslateUi(Hypersen)
        QtCore.QMetaObject.connectSlotsByName(Hypersen)

    def retranslateUi(self, Hypersen):
        _translate = QtCore.QCoreApplication.translate
        Hypersen.setWindowTitle(_translate("Hypersen", "Imager"))
        self.initializeButton.setText(_translate("Hypersen", "Initialize system"))
        self.startButton.setText(_translate("Hypersen", "Start"))
        self.stopButton.setText(_translate("Hypersen", "Stop"))
        self.measureButton.setText(_translate("Hypersen", "Measure"))

from pyqtgraph import PlotWidget
