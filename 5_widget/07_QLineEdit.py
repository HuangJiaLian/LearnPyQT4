#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2/10/18 10:51 AM
# Author  : Jack Huang
# Email   : jackhuang719668276@163.com
# File    : 07_QLineEdit.py
# About   : 
# 1. QLineEdit 窗口组件用来输入或者编辑单行纯文本，有撤销/重做，剪切/粘贴和拖放功能。
# 2. 行编辑框
# 3. 


from PyQt4 import QtGui
from PyQt4 import QtCore


class Example(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        self.initUI()


    def initUI(self):

        self.label = QtGui.QLabel(self)
        edit = QtGui.QLineEdit(self)

        edit.move(60, 100)
        self.label.move(60, 40)
        # 编辑窗的信号改变,调用方法 onChanged
        self.connect(edit, QtCore.SIGNAL('textChanged(QString)'),
            self.onChanged)

        self.setWindowTitle('QLineEdit')
        self.setGeometry(250, 200, 350, 250)


    def onChanged(self, text):
        self.label.setText(text)
        self.label.adjustSize()


def main():

    app = QtGui.QApplication([])
    exm = Example()
    exm.show()
    app.exec_()


if __name__ == '__main__':
    main()