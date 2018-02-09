#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2/9/18 2:49 PM
# Author  : Jack Huang
# Email   : jackhuang719668276@163.com
# File    : 01_sigslot.py
# About   : 
# 1. 信号和槽
# 2. 
# 3. 


import sys
from PyQt4 import QtGui, QtCore


class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):

        # 一个LCD屏
        lcd = QtGui.QLCDNumber(self)
        # 一个水平滑动条
        slider = QtGui.QSlider(QtCore.Qt.Horizontal, self)

        # 一个框布局
        vbox = QtGui.QVBoxLayout()
        # 添加上面两个元素到布局中去
        vbox.addWidget(lcd)
        vbox.addWidget(slider)

        self.setLayout(vbox)
        # 连接信号和槽
        # connect 方法有4个参数， sender 是发送信号的对象， signal 是发射的信号
        # receiver 是接收信号的对象， 最后， slog 是对信号反应的方法。
        self.connect(slider,  QtCore.SIGNAL('valueChanged(int)'), lcd,
            QtCore.SLOT('display(int)'))
        self.setWindowTitle(u'信号 & 槽')
        self.resize(250, 150)


app = QtGui.QApplication(sys.argv)
ex = Example()
ex.show()
sys.exit(app.exec_())