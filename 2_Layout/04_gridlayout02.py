#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2/9/18 2:22 PM
# Author  : Jack Huang
# Email   : jackhuang719668276@163.com
# File    : 04_gridlayout02.py
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
        # 创建三个标签
        title = QtGui.QLabel('Title')
        author = QtGui.QLabel('Author')
        review = QtGui.QLabel('Review')

        # 三个编辑框
        titleEdit = QtGui.QLineEdit()
        authorEdit = QtGui.QLineEdit()
        reviewEdit = QtGui.QTextEdit()

        # 一个网格布局
        grid = QtGui.QGridLayout()
        grid.setSpacing(10) # 间距

        grid.addWidget(title, 1, 0)
        grid.addWidget(titleEdit, 1, 1)

        grid.addWidget(author, 2, 0)
        grid.addWidget(authorEdit, 2, 1)

        grid.addWidget(review, 3, 0)
        # 占5行
        grid.addWidget(reviewEdit, 3, 1,5,1)

        self.setLayout(grid)

        self.setWindowTitle(u'网格布局')
        self.resize(350, 300)

app = QtGui.QApplication(sys.argv)
ex = Example()
ex.show()
sys.exit(app.exec_())
