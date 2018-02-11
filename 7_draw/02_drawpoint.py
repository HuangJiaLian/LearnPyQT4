#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2/11/18 2:07 PM
# Author  : Jack Huang
# Email   : jackhuang719668276@163.com
# File    : 04_drawpoint.py
# About   : 
# 1.　
# 2. 
# 3. 

import sys, random
from PyQt4 import QtGui, QtCore


class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Points')

    def paintEvent(self, e):

        qp = QtGui.QPainter()
        qp.begin(self)
        self.drawPoints(qp)
        qp.end()

    def drawPoints(self, qp):

        qp.setPen(QtCore.Qt.red)
        size = self.size()

        for i in range(1000):
            x = random.randint(1, size.width()-1)
            y = random.randint(1, size.height()-1)
            qp.drawPoint(x, y)

app = QtGui.QApplication(sys.argv)
ex = Example()
ex.show()
app.exec_()

