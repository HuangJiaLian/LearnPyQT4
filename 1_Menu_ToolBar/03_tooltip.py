#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2/9/18 10:09 AM
# Author  : Jack Huang
# Email   : jackhuang719668276@163.com
# File    : 03_tooltip.py
# About   : 
# 1.工具提示（气泡帮助）
# 2.字体修改, 加粗显示

import sys
from PyQt4 import QtGui
from PyQt4 import QtCore

# 新类　Tooltip继承自QtGui.QWidget
class Tooltip(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Tooltip')
        # <b></b>是用来加粗的
        self.setToolTip('This is a <b>QWidget</b> widget')
        # 字体，字号
        QtGui.QToolTip.setFont(QtGui.QFont('OldEnglish', 10))


app = QtGui.QApplication(sys.argv)
tooltip = Tooltip()
tooltip.show()
sys.exit(app.exec_())