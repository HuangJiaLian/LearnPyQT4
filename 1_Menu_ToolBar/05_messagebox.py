#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2/9/18 10:44 AM
# Author  : Jack Huang
# Email   : jackhuang719668276@163.com
# File    : 05_messagebox.py
# About   : 
# 1. 消息框,是为了程序更人性化
# 2. 
# 3. 

import sys
from PyQt4 import QtGui

class MessageBox(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle(u'消息框')
    # 如果我们关闭 QWidget ，将会产生一个 QCloseEvent 事件，我们需要重新实现 closeEvent() 事件来改变组件的行为。
    def closeEvent(self, event):
        # 接受用户的选择
        reply = QtGui.QMessageBox.question(self, u'提示',
            u"确定要退出吗?", QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
        # 如果点击Yes按钮，表明接受这个事件，将会关闭窗口组件并进回到应用程序的结尾，反之则忽略该关闭事件。
        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

app = QtGui.QApplication(sys.argv)
qb = MessageBox()
qb.show()
sys.exit(app.exec_())
