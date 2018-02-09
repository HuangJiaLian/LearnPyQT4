#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2/9/18 1:57 PM
# Author  : Jack Huang
# Email   : jackhuang719668276@163.com
# File    : 03_gridlayout01.py
# About   : 
# 1. 
# 2. 
# 3.

import sys
from PyQt4 import QtGui


class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle(u'网格布局')

        names = ['Cls', 'Bck', '', 'Close', '7', '8', '9', '/',
            '4', '5', '6', '*', '1', '2', '3', '-',
            '0', '.', '=', '+']

        # 新建一个网格布局
        grid = QtGui.QGridLayout()

        j = 0
        pos = [(0, 0), (0, 1), (0, 2), (0, 3),
                (1, 0), (1, 1), (1, 2), (1, 3),
                (2, 0), (2, 1), (2, 2), (2, 3),
                (3, 0), (3, 1), (3, 2), (3, 3),
                (4, 0), (4, 1), (4, 2), (4, 3)]

        for i in names:
            button = QtGui.QPushButton(i)
            if j == 2:
                grid.addWidget(QtGui.QLabel(''), 0, 2)
            else:
                grid.addWidget(button, pos[j][0], pos[j][1])
            j = j + 1

        self.setLayout(grid)

app = QtGui.QApplication(sys.argv)
ex = Example()
ex.show()
sys.exit(app.exec_())