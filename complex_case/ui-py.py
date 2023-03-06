# -*- coding: utf-8 -*-
"""
Created on Tue May 21 15:08:51 2019

@author: r.zor
"""


from PyQt5 import uic

fin = open(r'design.ui','r')
fout = open(r'gui_design.py','w')

uic.compileUi(fin,fout,execute=False)
fin.close()
fout.close()



#if __name__ == "__main__":
#    import sys
#    app = QtWidgets.QApplication(sys.argv)
#    MainWindow = QtWidgets.QMainWindow()
#    ui = Ui_MainWindow()
#    ui.setupUi(MainWindow)
#    MainWindow.show()
#    sys.exit(app.exec_())


