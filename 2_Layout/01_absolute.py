#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2/9/18 1:46 PM
# Author  : Jack Huang
# Email   : jackhuang719668276@163.com
# File    : 01_absolute.py
# About   : 
# 1. 绝对布局
# 2. 
# 3. 

import sys
from PyQt4 import QtGui


class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):
        label1 = QtGui.QLabel(u'绝对布局', self)
        label1.move(15, 10)

        label2 = QtGui.QLabel(u'学习PyQT编程', self)
        label2.move(35, 40)

        self.setWindowTitle(u'绝对布局')
        self.resize(250, 150)

app = QtGui.QApplication(sys.argv)
ex = Example()
ex.show()
sys.exit(app.exec_())