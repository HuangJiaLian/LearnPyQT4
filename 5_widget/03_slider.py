#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2/10/18 9:45 AM
# Author  : Jack Huang
# Email   : jackhuang719668276@163.com
# File    : 03_slider.py
# About   : 
# 1. qslider 滑块, 滑动条
# 2. 显示图标　label
# 3. 

import sys
from PyQt4 import QtGui
from PyQt4 import QtCore


class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):

        slider = QtGui.QSlider(QtCore.Qt.Horizontal, self)
        slider.setFocusPolicy(QtCore.Qt.NoFocus)
        slider.setGeometry(30, 40, 200, 20) # 滑动条的位置,长宽
        self.connect(slider, QtCore.SIGNAL('valueChanged(int)'),self.changeValue) # 连接信号和槽

        # 显示图标初始化
        self.label = QtGui.QLabel(self)
        self.label.setPixmap(QtGui.QPixmap('../icons/mute.png'))
        self.label.setGeometry(250, 35, 80, 30)

        self.setWindowTitle(u'Slider 滑动条')
        self.setGeometry(300, 300, 350, 250)

    # 根据滑动条的大小调节显示的图片
    def changeValue(self, value):
        if value == 0:
            self.label.setPixmap(QtGui.QPixmap('../icons/mute.png'))
        elif value > 0 and value <= 30:
            self.label.setPixmap(QtGui.QPixmap('../icons/min.png'))
        elif value > 30 and value < 80:
            self.label.setPixmap(QtGui.QPixmap('../icons/med.png'))
        else:
            self.label.setPixmap(QtGui.QPixmap('../icons/max.png'))


if __name__ == '__main__':

    app = QtGui.QApplication(sys.argv)
    ex = Example()
    ex.show()
    app.exec_()
