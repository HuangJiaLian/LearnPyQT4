#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2/9/18 3:17 PM
# Author  : Jack Huang
# Email   : jackhuang719668276@163.com
# File    : 04_emit.py
# About   : 
# 1. 发送信号,自己定义新的信号
# 2. 
# 3. 


import sys
from PyQt4 import QtGui, QtCore


class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):

        self.connect(self, QtCore.SIGNAL('closeEmitApp()'),
            QtCore.SLOT('close()'))

        self.setWindowTitle(u'发射信号')
        self.resize(250, 150)

    # 我们创建一个名为 closeEmitApp() 的新信号，在鼠标的按下实践中发射该信号。
    def mousePressEvent(self, event):
        self.emit(QtCore.SIGNAL('closeEmitApp()'))


app = QtGui.QApplication(sys.argv)
ex = Example()
ex.show()
sys.exit(app.exec_())
