#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2/9/18 9:41 AM
# Author  : Jack Huang
# Email   : jackhuang719668276@163.com
# File    : 01_start.py
# About   : 正式开始学习pyqt

import sys
# 导入GUI组件
from PyQt4 import QtGui

# sys.argv 使得程序可以在shell中运行
app = QtGui.QApplication(sys.argv)

# QWidget 窗口组件是PyQt4中所有用户界面对象的基类，
# 我们使用 QWidget 默认的构造，没有父亲。
# 没有父亲的窗口组件称为窗体。
widget = QtGui.QWidget()

widget.resize(450, 250)
widget.setWindowTitle(u'正式开始学习PyQT')
widget.show()

# 最后，我们输入应用程序的主事件循环，事件处理从这里开始。
# sys.exit()方法确保干净的退出。将通知环境应用程序是如何结束的。
# exec_() 方法会有下划线，一切皆有含义，这显然是因为exec是Python的关键字，
# 因此，用 exec_() 来取代它。
sys.exit(app.exec_())

