#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2/10/18 9:25 AM
# Author  : Jack Huang
# Email   : jackhuang719668276@163.com
# File    : 01_checkbox.py
# About   : 
# 1. qcheckbox 复选框
# 2. 
# 3.利用这个可以做一个Todo List 软件

import sys
from PyQt4 import QtGui
from PyQt4 import QtCore


class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle(u'Checkbox (复选框)')
        self.cb = QtGui.QCheckBox(u'显示标题', self)
        self.cb.setFocusPolicy(QtCore.Qt.NoFocus)
        self.cb.move(10, 10)
        self.cb.toggle()
        # 连接信号和槽, 复选框的状态发生改变,触发方法　changeTitle
        self.connect(self.cb, QtCore.SIGNAL('stateChanged(int)'),
            self.changeTitle)

    def changeTitle(self, value):
        # 通过复选框的状态设置窗口标题
        if self.cb.isChecked():
            self.setWindowTitle(u'Checkbox　(复选框)')
        else:
            self.setWindowTitle('')


if __name__ == '__main__':

    app = QtGui.QApplication(sys.argv)
    ex = Example()
    ex.show()
    app.exec_()


