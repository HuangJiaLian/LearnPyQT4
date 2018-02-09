#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2/9/18 3:46 PM
# Author  : Jack Huang
# Email   : jackhuang719668276@163.com
# File    : 04_openfiledialog.py
# About   : 
# 1. 打开文件对话框
# 2. 
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

        openFile = QtGui.QAction(QtGui.QIcon('../icons/document.png'), 'Open', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open new File')
        self.connect(openFile, QtCore.SIGNAL('triggered()'), self.showDialog)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openFile)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('OpenFile')

    def showDialog(self):

        filename = QtGui.QFileDialog.getOpenFileName(self, 'Open file',
                    '/home')
        fname = open(filename)
        data = fname.read()
        self.textEdit.setText(data)

app = QtGui.QApplication(sys.argv)
ex = Example()
ex.show()
app.exec_()