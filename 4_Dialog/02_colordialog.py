#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2/9/18 3:32 PM
# Author  : Jack Huang
# Email   : jackhuang719668276@163.com
# File    : 02_colordialog.py
# About   : 
# 1. 彩色的对话框
# 2. 
# 3. 


import sys
from PyQt4 import QtGui
from PyQt4 import QtCore


class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):

        # 初始颜色
        color = QtGui.QColor(0, 0, 0)

        self.button = QtGui.QPushButton(u'对话框', self)
        self.button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.button.move(20, 20)

        # 连接信号和槽: 按键clicked()信号发出过,触发showDialog
        self.connect(self.button, QtCore.SIGNAL('clicked()'),self.showDialog)
        self.setFocus()

        self.widget = QtGui.QWidget(self)
        # 设置初始颜色
        self.widget.setStyleSheet("QWidget { background-color: %s }"% color.name())
        self.widget.setGeometry(130, 22, 100, 100)

        self.setWindowTitle(u'彩色对话框')
        self.setGeometry(300, 300, 250, 180)


    def showDialog(self):
        # 获取颜色，重置颜色
        col = QtGui.QColorDialog.getColor()

        if col.isValid():
            self.widget.setStyleSheet("QWidget { background-color: %s }"% col.name())


if __name__ == '__main__':

    app = QtGui.QApplication(sys.argv)
    ex = Example()
    ex.show()
    app.exec_()