#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2/9/18 3:41 PM
# Author  : Jack Huang
# Email   : jackhuang719668276@163.com
# File    : 03_fontdialog.py
# About   : 
# 1. 字体选择对话框
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

        hbox = QtGui.QHBoxLayout()

        button = QtGui.QPushButton(u'对话框', self)
        button.setFocusPolicy(QtCore.Qt.NoFocus)
        button.move(20, 20)

        hbox.addWidget(button)

        self.connect(button, QtCore.SIGNAL('clicked()'), self.showDialog)

        self.label = QtGui.QLabel('Knowledge only matters', self)
        self.label.move(130, 20)

        hbox.addWidget(self.label, 1)
        self.setLayout(hbox)

        self.setWindowTitle(u'字体对话框')
        self.setGeometry(300, 300, 250, 110)

    # 获取字体，重置字体
    def showDialog(self):

        font, ok = QtGui.QFontDialog.getFont()
        if ok:
            self.label.setFont(font)


if __name__ == '__main__':

    app = QtGui.QApplication(sys.argv)
    ex = Example()
    ex.show()
    app.exec_()