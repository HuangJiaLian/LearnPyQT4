#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2/9/18 3:02 PM
# Author  : Jack Huang
# Email   : jackhuang719668276@163.com
# File    : 02_escape.py
# About   :
# 1. 重新实现事件处理程序
# 2. 我们重新实现了 keyPressEvent() 处理。
# 3. 如果我们按下了escape按钮，程序将退出。


import sys
from PyQt4 import QtGui, QtCore


class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()

        self.setWindowTitle('Escape')
        self.resize(250, 150)

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Escape:
            self.close()


app = QtGui.QApplication(sys.argv)
ex = Example()
ex.show()
sys.exit(app.exec_())

