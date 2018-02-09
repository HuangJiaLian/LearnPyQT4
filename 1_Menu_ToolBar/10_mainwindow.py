#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2/9/18 11:34 AM
# Author  : Jack Huang
# Email   : jackhuang719668276@163.com
# File    : 10_mainwindow.py
# About   : 
# 1. 结合状态栏，菜单栏，工具栏的内容，做一个主窗口
# 2. 
# 3. 


import sys
from PyQt4 import QtGui, QtCore

class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)

        self.resize(350, 250)
        self.setWindowTitle(u'主窗口')

        # 添加一个编辑框
        textEdit = QtGui.QTextEdit()
        self.setCentralWidget(textEdit)

        # 创建一个退出行为
        exit = QtGui.QAction(QtGui.QIcon('icons/power-button.png'), u'Exit', self)
        exit.setShortcut('Ctrl+Q')
        exit.setStatusTip(u'退出应用')
        self.connect(exit, QtCore.SIGNAL('triggered()'), QtCore.SLOT('close()'))

        self.statusBar()

        menubar = self.menuBar()
        file = menubar.addMenu(u'&文件')
        file.addAction(exit)

        toolbar = self.addToolBar(u'退出')
        toolbar.addAction(exit)


app = QtGui.QApplication(sys.argv)
main = MainWindow()
main.show()
sys.exit(app.exec_())