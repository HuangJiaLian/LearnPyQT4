#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2/9/18 10:51 AM
# Author  : Jack Huang
# Email   : jackhuang719668276@163.com
# File    : 06_center.py
# About   : 
# 1. 居中显示窗口
# 2. 
# 3. 


import sys
from PyQt4 import QtGui

class Center(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        self.setWindowTitle(u'居中显示窗口')
        self.resize(350, 250)
        self.center()
    #
    def center(self):
        # 计算屏幕分辨率
        screen = QtGui.QDesktopWidget().screenGeometry()
        # 获得widget的尺寸
        size =  self.geometry()
        self.move((screen.width()-size.width())/2, (screen.height()-size.height())/2)


app = QtGui.QApplication(sys.argv)
qb = Center()
qb.show()
sys.exit(app.exec_())