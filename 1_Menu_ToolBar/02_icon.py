#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2/9/18 9:42 AM
# Author  : Jack Huang
# Email   : jackhuang719668276@163.com
# File    : 02_icon.py
# About   :
# 1.添加一个程序图标(只有Windows可以看窗口图标)
# 2.面向对象的编程: 面向对象编程中三个最重要东西是类,数据和方法
# 3.类的继承

import sys
from PyQt4 import QtGui

# 使用面向对象的编程
# 创建一个名为 Icon 的新类，继承自 QtGui.QWidget 类
class Icon(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle(u'添加一个窗口图标')
        self.setWindowIcon(QtGui.QIcon('icons/web.png'))

app = QtGui.QApplication(sys.argv)
icon = Icon()
# show() 这个方法继承于　QtGui.QWidget　类
icon.show()
sys.exit(app.exec_())

