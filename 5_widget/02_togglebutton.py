#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2/10/18 9:36 AM
# Author  : Jack Huang
# Email   : jackhuang719668276@163.com
# File    : 02_togglebutton.py
# About   : 
# 1. 切换按钮 togglebutton
# 2. 切换按钮是指一个两种状态的按钮，按下和非按下。通过点击切换两种状态。在某种状态下来这种方式很合适。
# 3. 


import sys
from PyQt4 import QtGui
from PyQt4 import QtCore


class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):

        self.color = QtGui.QColor(0, 0, 0)
        # 三个按钮　连接对应的信号, 被clicked()后触发setColor方法
        self.red = QtGui.QPushButton('Red', self)
        self.red.setCheckable(True)
        self.red.move(10, 10)

        self.connect(self.red, QtCore.SIGNAL('clicked()'), self.setColor)

        self.green = QtGui.QPushButton('Green', self)
        self.green.setCheckable(True)
        self.green.move(10, 60)

        self.connect(self.green, QtCore.SIGNAL('clicked()'), self.setColor)

        self.blue = QtGui.QPushButton('Blue', self)
        self.blue.setCheckable(True)
        self.blue.move(10, 110)

        self.connect(self.blue, QtCore.SIGNAL('clicked()'), self.setColor)



        self.square = QtGui.QWidget(self)
        self.square.setGeometry(150, 20, 100, 100)
        self.square.setStyleSheet("QWidget { background-color: %s }" %
            self.color.name())

        self.setWindowTitle(u'ToggleButton(切换按钮)')
        self.setGeometry(300, 300, 380, 270)


    def setColor(self):
        # 用于检测是那个按钮触发的这个操作
        source = self.sender()

        # 设置对应的分量
        if source.text() == "Red":
            if self.red.isChecked():
                self.color.setRed(255)
            else: self.color.setRed(0)

        elif source.text() == "Green":
            if self.green.isChecked():
                self.color.setGreen(255)
            else: self.color.setGreen(0)

        else:
            if self.blue.isChecked():
                self.color.setBlue(255)
            else: self.color.setBlue(0)
        # 通过样式表修改背景色。
        self.square.setStyleSheet("QWidget { background-color: %s }" %
            self.color.name())



if __name__ == '__main__':

    app = QtGui.QApplication(sys.argv)
    ex = Example()
    ex.show()
    app.exec_()
