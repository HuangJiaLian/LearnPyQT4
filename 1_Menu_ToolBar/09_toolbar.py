#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2/9/18 11:29 AM
# Author  : Jack Huang
# Email   : jackhuang719668276@163.com
# File    : 09_toolbar.py
# About   : 
# 1. 工具栏

import sys
from PyQt4 import QtGui, QtCore

class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)

        self.resize(250, 150)
        self.setWindowTitle(u'工具栏')

        # 先准备好行为
        self.exit = QtGui.QAction(QtGui.QIcon('icons/power-button.png'), u'退出', self)
        self.exit.setShortcut('Ctrl+Q')
        self.connect(self.exit, QtCore.SIGNAL('triggered()'), QtCore.SLOT('close()'))

        self.toolbar = self.addToolBar(u'退出')
        self.toolbar.addAction(self.exit)


app = QtGui.QApplication(sys.argv)
main = MainWindow()
main.show()
sys.exit(app.exec_())

