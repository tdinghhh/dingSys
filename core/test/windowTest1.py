#!/usr/bin/env python
#encoding: utf-8




import sys
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QTextEdit
from PyQt5.QtWidgets import QAction
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QDesktopWidget


class Demo1(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        """窗口显示主程序"""
        #下方状态栏小窗口
        self.statusBar().showMessage('index')

        #菜单
        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        menubar.addMenu('&File')
        menubar.addMenu('&Edit')
        menubar.addMenu('&View')
        menubar.addMenu('&Tools')

        #工具栏
        self.toolbar = self.addToolBar('Exit')




        #窗口大小
        self.resize(1000,800)
        # self.setGeometry(300,100,1000,800)
        self.center()
        self.setWindowTitle('dingSys')
        self.show()

    def center(self):
        """控制窗口显示在屏幕中心的方法"""
        #获得窗口
        qr = self.frameGeometry()
        #获得屏幕中心点
        cp = QDesktopWidget().availableGeometry().center()
        #显示到屏幕中心
        qr.moveCenter(cp)
        self.move(qr.topLeft())



app = QApplication(sys.argv)
ex = Demo1()
sys.exit(app.exec_())




