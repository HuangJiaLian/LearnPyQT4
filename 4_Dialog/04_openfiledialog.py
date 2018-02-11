#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2/9/18 3:46 PM
# Author  : Jack Huang
# Email   : jackhuang719668276@163.com
# File    : 04_openfiledialog.py
# About   : 
# 1. 打开文件对话框
# 2. 加载中文
# 3. 

import sys
from PyQt4 import QtGui
from PyQt4 import QtCore


class Example(QtGui.QMainWindow):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):

        self.textEdit = QtGui.QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.statusBar()
        self.setFocus()

        # 创建一个打开文件的行为
        openFile = QtGui.QAction(QtGui.QIcon('../icons/document.png'), u'打开', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('打开一个文件')
        # 当这个行为被触发,显示对话框
        self.connect(openFile, QtCore.SIGNAL('triggered()'), self.showDialog)

        # 创建菜单栏,添加打开文件的行为
        menubar = self.menuBar()
        fileMenu = menubar.addMenu(u'&文件')
        fileMenu.addAction(openFile)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle(u'打开文件')

    def showDialog(self):
        # 打开文件，设置默认的路径为当前目录
        filename = QtGui.QFileDialog.getOpenFileName(self, u'打开文件','.')
        fname = open(filename)
        data = fname.read()
        # 这样就允许可以在文本里面包含中文了
        data = unicode(data, "utf-8")
        # 修改编辑框的文本
        self.textEdit.setText(data)

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    ex.show()
    app.exec_()