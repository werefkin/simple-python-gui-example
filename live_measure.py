# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 11:02:05 2022

@author: r.gap
"""

import numpy as np
import time as times
import sys
from pyqtgraph.Qt import QtCore
# import pyqtgraph as pg
# from pyqtgraph.ptime import time
from window import Ui_MainWindow
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication

#########################################
# main
#########################################

global fname, data, flag, mon, monitor, monitor_number
fname = 'test.txt'
data = np.zeros(1024)
flag = 0





class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()
        
        self.measurement = Measure(self)
        
        self.ui.verticalWidget.show()
        
        self.ui.p = self.ui.verticalWidget.plot()
        self.ui.verticalWidget.setLabel('left', 'Value', units='au')
        self.ui.verticalWidget.setLabel('bottom', 'Sample no.', units='s')
        #self.ui.verticalWidget.setClipToView(True)
        

        self.ui.startMeasurementButton.clicked.connect(self.measurement.start)
        self.ui.startMeasurementButton.clicked.connect(self.flag_zero)
        self.ui.stopMeasurementButton.clicked.connect(self.flag_one)
                  
        
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update)
        self.timer.start(100)
        
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


class Measure(QtCore.QThread):
    
    def __init__(self, parent=None):
        QtCore.QThread.__init__(self, parent)

    def run(self):
        global data, flag, nPixelSize, pnDeviceID
        #dat = measure(fname)
        while flag == 0:
            #time.sleep(0.5)
            print('shape data: ', np.shape(data))
            print('flag: ', flag)
            data=np.random.rand(200)


if __name__ == '__main__':
    app = QtCore.QCoreApplication.instance()
    if app is None:
        app = QtWidgets.QApplication(sys.argv)
    # qtmodern.styles.dark(app)
    w = Window()
    # mw = qtmodern.windows.ModernWindow(w)
    # mw.show()
    w.show()
    # sys.exit(app.exec_)
    sys.exit(app.exec_())


