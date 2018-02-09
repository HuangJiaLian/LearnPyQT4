#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2/9/18 3:22 PM
# Author  : Jack Huang
# Email   : jackhuang719668276@163.com
# File    : 01_inputdialog.py
# About   : 
# 1. 输入对话框
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

        self.button = QtGui.QPushButton(u'对话框', self)
        self.button.setFocusPolicy(QtCore.Qt.NoFocus)

        self.button.move(20, 20)
        self.connect(self.button, QtCore.SIGNAL('clicked()'),self.showDialog)
        self.setFocus()

        self.label = QtGui.QLineEdit(self)
        self.label.move(130, 22)

        self.setWindowTitle(u'输入对话框')
        self.setGeometry(300, 300, 350, 80)

    def showDialog(self):
        # 获取用户的输入
        text, ok = QtGui.QInputDialog.getText(self, u'输入对话框',u'请输入你的名字:')
        # 这个例子有一个按钮和一个单行编辑器，按钮显示输入对话框来获取值，输入的值将会显示在单行编辑器中。
        if ok:
            self.label.setText(str(text))


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    ex.show()
    app.exec_()