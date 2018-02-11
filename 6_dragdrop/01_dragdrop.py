#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2/10/18 11:16 AM
# Author  : Jack Huang
# Email   : jackhuang719668276@163.com
# File    : 01_dragdrop.py
# About   : 
# 1. 拖放: 我们将从单行编辑器中拖动纯文本到按钮上.
# 2. 自定义类,类的继承
# 3. 

import sys
from PyQt4 import QtGui
# 为了把文本放到 QPushButton 窗口组件上，必须重新实现一些方法。
# 我们创建自己的 Button 类，从 QPushButton 继承。
class Button(QtGui.QPushButton):

    def __init__(self, title, parent):
        super(Button, self).__init__(title, parent)
        self.setAcceptDrops(True) # 为窗口组件设置可以接受放入事件。

    def dragEnterEvent(self, e): # 首先重新实现 dragEnterEvent() 方法。接受了解的数据类型，在该例子中是纯文本。

        if e.mimeData().hasFormat('text/plain'):
            e.accept()
        else:
            e.ignore()
    # 在重新实现 dropEvent() 方法中，我们定义在拖入事件中处理什么任务。这里我们修改按钮的文字.
    def dropEvent(self, e):
        self.setText(e.mimeData().text())


class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):

        edit = QtGui.QLineEdit('', self)
        edit.setDragEnabled(True)
        edit.move(30, 65)

        button = Button("Button", self)
        button.move(190, 65)

        self.setWindowTitle('Simple Drag & Drop')
        self.setGeometry(300, 300, 300, 150)


def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    ex.show()
    app.exec_()


if __name__ == '__main__':
    main()