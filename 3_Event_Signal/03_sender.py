#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2/9/18 3:04 PM
# Author  : Jack Huang
# Email   : jackhuang719668276@163.com
# File    : 03_sender.py
# About   : 
# 1. 信号的发送者(确定哪个组件发出了信号)
# 2. 
# 3. 



import sys
from PyQt4 import QtGui, QtCore


class Example(QtGui.QMainWindow):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):

        # 两个按键
        button1 = QtGui.QPushButton(u"按键1", self)
        button1.move(30, 50)

        button2 = QtGui.QPushButton(u"按键2", self)
        button2.move(150, 50)

        # 这里的槽是一个自定义的函数
        self.connect(button1, QtCore.SIGNAL('clicked()'),
            self.buttonClicked)

        self.connect(button2, QtCore.SIGNAL('clicked()'),
            self.buttonClicked)

        self.statusBar().showMessage(u'就绪')
        self.setWindowTitle(u'事件发送者')
        self.resize(290, 150)

    # 槽
    # 通过调用 sender() 方法我们确定信号来源。在程序的状态栏，我们显示按下的按钮的标签。
    def buttonClicked(self):
        # 确定信号的发送者
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + u'被按下')

app = QtGui.QApplication(sys.argv)
ex = Example()
ex.show()
sys.exit(app.exec_())