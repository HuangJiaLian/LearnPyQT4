#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2/11/18 11:41 AM
# Author  : Jack Huang
# Email   : jackhuang719668276@163.com
# File    : 02_dragdrop_button.py.py
# About   : 
# 1. 
# 2. 
# 3.

import sys
from PyQt4 import QtGui
from PyQt4 import QtCore

# 自定义一个Button, 继承自QPushButton
class Button(QtGui.QPushButton):

    def __init__(self, title, parent):
        super(Button, self).__init__(title, parent)

    # 鼠标移动事件
    def mouseMoveEvent(self, e):

        if e.buttons() != QtCore.Qt.RightButton:
            return

        mimeData = QtCore.QMimeData()

        drag = QtGui.QDrag(self)
        drag.setMimeData(mimeData)
        drag.setHotSpot(e.pos() - self.rect().topLeft())

        dropAction = drag.start(QtCore.Qt.MoveAction)

    # 鼠标按下事件
    def mousePressEvent(self, e):

        QtGui.QPushButton.mousePressEvent(self, e)
        if e.button() == QtCore.Qt.LeftButton:
            print 'press'

class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        # 允许拖放
        self.setAcceptDrops(True)

        self.button = Button('Button', self)
        self.button.move(100, 65)

        self.setWindowTitle(u'点击或者移动')
        self.setGeometry(300, 300, 280, 150)

    def dragEnterEvent(self, e):

        e.accept()

    def dropEvent(self, e):

        position = e.pos()
        self.button.move(position)

        e.setDropAction(QtCore.Qt.MoveAction)
        e.accept()

def main():

    app = QtGui.QApplication(sys.argv)
    ex = Example()
    ex.show()
    app.exec_()


if __name__ == '__main__':
    main()
