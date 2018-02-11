#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2/10/18 11:08 AM
# Author  : Jack Huang
# Email   : jackhuang719668276@163.com
# File    : 09_combobox.py
# About   : 
# 1. QComboBox 窗口组件允许用户从列表清单中选择。
# 2. 下拉选择
# 3. 

from PyQt4 import QtGui, QtCore


class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()


    def initUI(self):

        self.label = QtGui.QLabel("Ubuntu", self)

        combo = QtGui.QComboBox(self)
        combo.addItem("Ubuntu")
        combo.addItem("Mandriva")
        combo.addItem("Fedora")
        combo.addItem("Red Hat")
        combo.addItem("Gentoo")

        combo.move(50, 50)
        self.label.move(50, 150)
        # 下拉框被激活，执行方法onActivated
        self.connect(combo, QtCore.SIGNAL('activated(QString)'),
            self.onActivated)

        self.setGeometry(250, 200, 350, 250)
        self.setWindowTitle(u'QComboBox 下拉选择')

    def onActivated(self, text):

        self.label.setText(text)
        self.label.adjustSize()


def main():

    app = QtGui.QApplication([])
    ex = Example()
    ex.show()
    app.exec_()


if __name__ == '__main__':
    main()
