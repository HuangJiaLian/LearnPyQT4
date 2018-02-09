#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2/9/18 11:05 AM
# Author  : Jack Huang
# Email   : jackhuang719668276@163.com
# File    : 08_menubar.py
# About   : 
# 1. 菜单栏
# 2. 添加菜单动作
# 3. 信号和槽


import sys
from PyQt4 import QtGui, QtCore

class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)

        self.resize(350, 250)
        self.setWindowTitle(u'菜单栏')
        # 创建菜单动作: 退出
        exit = QtGui.QAction(QtGui.QIcon('icons/power-button.png'), u'退出', self)
        exit.setShortcut('Ctrl+Q')
        # 设置菜单动作的状态栏提示
        exit.setStatusTip(u'退出应用')
        # 动作的实际用途
        self.connect(exit, QtCore.SIGNAL('triggered()'), QtCore.SLOT('close()'))

        self.statusBar()
        
        menubar = self.menuBar()
        # 添加菜单
        # &是下划线
        file = menubar.addMenu(u'&文件')
        file.addAction(exit)

app = QtGui.QApplication(sys.argv)
main = MainWindow()
main.show()
sys.exit(app.exec_())