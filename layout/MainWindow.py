import sys

import pandas as pd
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, \
    QVBoxLayout, QTextEdit, QPushButton, QListWidget, QLabel, QTabWidget, \
    QListWidgetItem, QFileDialog, QDialog,QLineEdit
from PyQt5 import QtCore

from layout.Opreation import Opreation
from layout.Progress import Progress
import global_var

list_itemSize = QSize(100,30)

class MainWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.resize(1080,720)

        #widget测试用(textedit)
        # text_test_up = QTextEdit("up")
        # text_test_down = QTextEdit("down")
        # up_m_temp = QTextEdit("progress")
        # down_r_temp = QTextEdit("opreation")
        tab1 = QTextEdit("tab1 test")
        tab2 = QWidget()
        tab3 = QWidget()
        # label_data = QLabel("dataSet1")
        # label_data.setAlignment(Qt.AlignCenter)
        set1 = QListWidgetItem()
        set1.setSizeHint(list_itemSize)
        dataSet1 = QPushButton("dataSet1")

    #上方布局
        #left(up_l)
        up_l = QVBoxLayout()
        self.btn_local = QPushButton("从文件打开")
        self.btn_db = QPushButton("从数据库打开")
        up_l.addWidget(self.btn_local)
        up_l.addWidget(self.btn_db)
        #middle
        progress = Progress()
        #right
        self.btn_run = QPushButton("运行")
        self.btn_exit = QPushButton("退出")
        self.btn_local.clicked.connect(self.data_local)

    #下方布局
        #left(down_l)
        down_l = QVBoxLayout()
        self.label_in = QLabel("输入数据")
        self.label_in.setAlignment(Qt.AlignCenter)
        self.label_in.setContentsMargins(5,5,5,0)
        self.list_in = QListWidget()
        self.list_in.addItem(set1)
        self.list_in.setItemWidget(set1,dataSet1)
        self.label_out = QLabel("输出数据")
        self.label_out.setAlignment(Qt.AlignCenter)#居中对齐
        self.list_out = QListWidget()
        down_l.addWidget(self.label_in)
        down_l.addWidget(self.list_in)
        down_l.addWidget(self.label_out)
        down_l.addWidget(self.list_out)
        down_l.setStretch(0,1)
        down_l.setStretch(1,7)
        down_l.setStretch(2,1)
        down_l.setStretch(3,7)
        # down_l.setContentsMargins(5,5,5,0)
        down_l.setSpacing(0)
        #middle(tabs)
        self.tabs = QTabWidget()
        self.tabs.setTabShape(QTabWidget.Triangular)
        self.tabs.setDocumentMode(True)
        self.tabs.setMovable(True)
        self.tabs.setTabsClosable(True)
        self.tabs.tabCloseRequested.connect(self.close_tab)
        self.tabs.addTab(tab1,"tab1")
        self.tabs.addTab(tab2,"tab2")
        self.tabs.addTab(tab3,"tab3")
        #right
        self.oprea = Opreation()

    #设置UI上下方布局为水平布局
        #up
        layout_up = QHBoxLayout()
        # layout_up.addWidget(text_test_up)
        layout_up.addLayout(up_l)
        layout_up.addWidget(progress)
        layout_up.addWidget(self.btn_run)
        layout_up.addWidget(self.btn_exit)
        layout_up.setStretch(0,2)
        layout_up.setStretch(1,8)
        layout_up.setStretch(2,1)
        layout_up.setStretch(3,1)
        #down
        layout_down = QHBoxLayout()
        # layout_down.addWidget(text_test_down)
        layout_down.addLayout(down_l)
        layout_down.addWidget(self.tabs)
        layout_down.addWidget(self.oprea)
        layout_down.setStretch(0,1)
        layout_down.setStretch(1,3)
        layout_down.setStretch(2,1)

    #设置UI总体布局
        layout_main = QVBoxLayout()
        layout_main.addLayout(layout_up)
        layout_main.addLayout(layout_down)
        layout_main.setStretch(0,1)
        layout_main.setStretch(1,10)

        self.setLayout(layout_main)

    @QtCore.pyqtSlot()
    def close_tab(self,index):
        self.tabs.removeTab(index)

    @QtCore.pyqtSlot()
    def add_tab(self,tab,title):
        self.tabs.addTab(tab,title)

    @QtCore.pyqtSlot()
    def data_local(self):
        fileName,fileType = QFileDialog.getOpenFileName(self,'选择文件','','*.csv')
        if fileName!=None and fileName!="":
            global_var.filePath = fileName
            self.dialog = QDialog()
            self.dialog.resize(400, 40)
            hbox_u = QHBoxLayout()
            hbox_d = QHBoxLayout()
            vbox = QVBoxLayout()
            label = QLabel("数据集命名：")
            self.lineText = QLineEdit()
            self.btn_ok = QPushButton("确定")
            self.btn_cancel = QPushButton("取消")
            self.btn_ok.clicked.connect(self.on_ok_click)
            self.btn_cancel.clicked.connect(self.on_cancel_click)
            hbox_u.addWidget(label)
            hbox_u.addWidget(self.lineText)
            hbox_u.setStretch(0, 1)
            hbox_u.setStretch(1, 2)
            hbox_d.addStretch(2)
            hbox_d.addWidget(self.btn_ok)
            hbox_d.addWidget(self.btn_cancel)
            vbox.addLayout(hbox_u)
            vbox.addLayout(hbox_d)
            self.dialog.setLayout(vbox)
            self.dialog.setWindowModality(Qt.ApplicationModal)
            self.dialog.exec_()

    @QtCore.pyqtSlot()
    def on_ok_click(self):
        #命名数据集
        dataSetItem = QPushButton(self.lineText.text())#输入数据Item
        global_var.dataSet["dataName"] = self.lineText.text()
        global_var.dataSet["data"] = pd.read_csv(global_var.filePath)
        global_var.dataSet["Path"] = global_var.filePath
        dataSet = global_var.dataSet
        global_var.dataList.append(dataSet)
        global_var.dataMap[self.lineText.text()] = dataSet
        listItem = QListWidgetItem()
        listItem.setSizeHint(list_itemSize)
        self.list_in.addItem(listItem)
        self.list_in.setItemWidget(listItem,dataSetItem)
        self.dialog.close()

    @QtCore.pyqtSlot()
    def on_cancel_click(self):
        global_var.filePath = ""
        self.dialog.close()

    @QtCore.pyqtSlot()
    def data_db(self):
        pass
        # print(global_var.filePath)

    @QtCore.pyqtSlot()
    def run(self):
        pass

    @QtCore.pyqtSlot()
    def exit(self):
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())