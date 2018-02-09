#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2/9/18 1:49 PM
# Author  : Jack Huang
# Email   : jackhuang719668276@163.com
# File    : 02_boxlayout.py
# About   : 
# 1. 框布局
# 2. 
# 3. 

import sys
from PyQt4 import QtGui


class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):
        # 创建两个按钮
        okButton = QtGui.QPushButton(u"确定")
        cancelButton = QtGui.QPushButton(u"取消")

        # 我们创建一个水平框布局，增加一个延展因素和两个按钮.
        hbox = QtGui.QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)

        # 为了创建所需的布局，我们把水平布局放到垂直布局中。
        vbox = QtGui.QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        # 最后，我们设置窗体的主布局。
        self.setLayout(vbox)

        self.setWindowTitle(u'框布局')
        self.resize(300, 150)

app = QtGui.QApplication(sys.argv)
ex = Example()
ex.show()
sys.exit(app.exec_())