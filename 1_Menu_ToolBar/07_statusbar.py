#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2/9/18 11:00 AM
# Author  : Jack Huang
# Email   : jackhuang719668276@163.com
# File    : statusbar.py
# About   : 
# 1. 状态栏


import sys
from PyQt4 import QtGui

class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)

        self.resize(350, 250)
        self.setWindowTitle(u'状态栏')
        # 状态栏
        self.statusBar().showMessage(u'就绪')


app = QtGui.QApplication(sys.argv)
main = MainWindow()
main.show()
sys.exit(app.exec_())
