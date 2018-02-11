#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2/10/18 10:56 AM
# Author  : Jack Huang
# Email   : jackhuang719668276@163.com
# File    : 08_splitter.py
# About   : 
# 1. QSplitter 使得用户可以通过拖动子窗口组件的边界来控制子窗口组件的尺寸。
# 2. 布局就是搞清楚包含关系

from PyQt4 import QtGui, QtCore


class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()


    def initUI(self):
        # 一个布局框
        hbox = QtGui.QHBoxLayout(self)

        # 三个框架窗口组件
        topleft = QtGui.QFrame(self)
        topleft.setFrameShape(QtGui.QFrame.StyledPanel)

        topright = QtGui.QFrame(self)
        topright.setFrameShape(QtGui.QFrame.StyledPanel)

        bottom = QtGui.QFrame(self)
        bottom.setFrameShape(QtGui.QFrame.StyledPanel)

        # 两个分离器
        # splitter1 包含　topleft 和　topright
        splitter1 = QtGui.QSplitter(QtCore.Qt.Horizontal) # 一个水平分离器
        splitter1.addWidget(topleft)
        splitter1.addWidget(topright)
        # spliter2 包含　spliter1 和　bottom
        splitter2 = QtGui.QSplitter(QtCore.Qt.Vertical)# 一个垂直分离器
        splitter2.addWidget(splitter1)
        splitter2.addWidget(bottom)

        # hbox 包含splitter2
        hbox.addWidget(splitter2)
        self.setLayout(hbox)

        self.setWindowTitle(u'QSplitter 分离器')
        QtGui.QApplication.setStyle(QtGui.QStyleFactory.create('Cleanlooks'))
        self.setGeometry(250, 200, 350, 250)


def main():

    app = QtGui.QApplication([])
    ex = Example()
    ex.show()
    app.exec_()


if __name__ == '__main__':
    main()
