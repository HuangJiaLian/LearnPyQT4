#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2/10/18 10:10 AM
# Author  : Jack Huang
# Email   : jackhuang719668276@163.com
# File    : 04_progressbar.py
# About   : 
# 1. 进度条　progressbar　
# 2. 定时器　定时器事件


import sys
from PyQt4 import QtGui
from PyQt4 import QtCore


class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):
        # 进度条
        self.pbar = QtGui.QProgressBar(self)
        self.pbar.setGeometry(30, 40, 200, 25)

        self.button = QtGui.QPushButton('Start', self)
        self.button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.button.move(40, 80)

        # 连接信号和槽: 按键开始
        self.connect(self.button, QtCore.SIGNAL('clicked()'),self.doAction)

        # 一个定时器
        self.timer = QtCore.QBasicTimer()
        self.step = 0

        self.setWindowTitle(u'ProgressBar 进度条')
        self.setGeometry(300, 300, 350, 250)

    # 定时器事件
    def timerEvent(self, event):
        # 定时器记录的数值超过100, 停止定时器
        if self.step >= 100:
            self.timer.stop()
            return
        # 步数加１
        self.step = self.step + 1
        self.pbar.setValue(self.step)

    def doAction(self):

        if self.timer.isActive():
            self.timer.stop()
            self.button.setText('Start')
        else:
            # 100对应10s; 10对应1s=1000ms; 1对应100ms
            # 开始定时器 通过调用 start() 方法加载定时器事件，
            # 该方法有两个参数，超时时间（ timeout ）和接受事件的对象（ object ）。
            self.timer.start(100, self)
            self.button.setText('Stop')


if __name__ == '__main__':

    app = QtGui.QApplication(sys.argv)
    ex = Example()
    ex.show()
    app.exec_()