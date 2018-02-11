#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2/10/18 10:32 AM
# Author  : Jack Huang
# Email   : jackhuang719668276@163.com
# File    : 06_pixmap.py
# About   : 
# 1. pixmap 显示图片
# 2. 
# 3. 


from PyQt4 import QtGui

class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):

        hbox = QtGui.QHBoxLayout(self)
        pixmap = QtGui.QPixmap("../pics/python.png")

        label = QtGui.QLabel(self)
        label.setPixmap(pixmap)

        hbox.addWidget(label)
        self.setLayout(hbox)

        self.setWindowTitle(u"显示图片")
        self.move(250, 200)


def main():

    app = QtGui.QApplication([])
    exm = Example()
    exm.show()
    app.exec_()


if __name__ == '__main__':
    main()
