#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2/9/18 10:17 AM
# Author  : Jack Huang
# Email   : jackhuang719668276@163.com
# File    : quitbutton.py
# About   : 
# 1. 关闭窗口,pushbutton
# 2. 信号: QTCore这个模块中包含信号和槽,本例中点击按钮发送clicked()信号
# 3. 槽:槽可以是PyQt的槽或者任何的Python调用。本例中槽是quit()

import sys
from PyQt4 import QtGui, QtCore

class QuitButton(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle(u'关闭按钮')

        # 创建一个按钮并放置在 QWidget 上
        quit = QtGui.QPushButton(u'关闭', self)
        quit.setGeometry(170, 120, 64, 35)

        # PyQt4中的事件处理系统是建立信号和槽机制.
        # 如果点击按钮，信号 clicked() 将会发射，槽可以是PyQt的槽或者任何的Python调用。
        # QtCore.QObject.connect() 把信号和槽连接起来。
        # 在这个例子中槽是PyQt预定义的 quit() 槽，发射方和接收方两个对象间进行通讯，发射方为按钮，接收方为application对象。
        self.connect(quit, QtCore.SIGNAL('clicked()'),
            QtGui.qApp, QtCore.SLOT('quit()'))


app = QtGui.QApplication(sys.argv)
qb = QuitButton()
qb.show()
sys.exit(app.exec_())