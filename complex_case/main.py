# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 15:40:04 2022

@author: werefkin
"""



import numpy as np
import time as times
import sys
from pyqtgraph.Qt import QtCore
import qtmodern.styles
import qtmodern.windows# import pyqtgraph as pg
# from pyqtgraph.ptime import time
from gui_design import Ui_Hypersen
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import pyqtSlot

#########################################
# main
#########################################

global fname, data, flag, mon, monitor, monitor_number
fname = 'test.txt'
data = np.zeros(1024)
flag = 1





class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Hypersen()
        self.ui.setupUi(self)
        self.show()
        
        #THREADS
        self.measurement = Measure(self)
        
        #PLOT
        self.ui.plotSignal.show()
        self.ui.p = self.ui.plotSignal.plot()
        self.ui.plotSignal.setLabel('left', 'Signal', units='au')

        #BUTTONS
        self.ui.startButton.clicked.connect(self.measurement.start)
        self.ui.startButton.clicked.connect(self.flag_zero)
        self.ui.stopButton.clicked.connect(self.flag_one)
                  
        #TIMER
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update)
        self.timer.start(100)
        
        #SIGNALS
        self.measurement.status.connect(self.addlogline)
        
    def update(self):
        self.displaydata = data[:]
        self.ui.p.setData(self.displaydata, name='Raw Signal')
        
    def flag_one(self):
        # do stuff
        global flag
        flag = 1
        
    def flag_zero(self):
        # do stuff
        global flag
        flag = 0
        
    def closeEvent(self, event):
        global flag
        flag=1
        times.sleep(0.5)
        event.accept()
        QApplication.quit()
        
    @pyqtSlot(object)
    def addlogline(self, status_text):
        self.ui.logs.append(status_text)  
        


class Measure(QtCore.QThread):
                        
    status = QtCore.pyqtSignal(object)

    def __init__(self, parent=None):
        QtCore.QThread.__init__(self, parent)

    def run(self):
        global data, flag
        
        self.ms_msg='Measurements started'
        self.status.emit(self.ms_msg)
        while flag == 0:
            #time.sleep(0.5)
            print('shape data: ', np.shape(data))
            print('flag: ', flag)
            data=np.random.rand(1500)


if __name__ == '__main__':
    app = QtCore.QCoreApplication.instance()
    if app is None:
        app = QtWidgets.QApplication(sys.argv)
    qtmodern.styles.dark(app)
    w = Window()
    mw = qtmodern.windows.ModernWindow(w)
    mw.show()
    w.show()
    # sys.exit(app.exec_)
    sys.exit(app.exec_())

# this is the end