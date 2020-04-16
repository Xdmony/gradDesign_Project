import sys

import pandas as pd
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, \
    QVBoxLayout, QPushButton,  QLabel, QTabWidget, \
     QFileDialog, QDialog,QLineEdit
from PyQt5 import QtCore
from widgets.tabs import Tabs
from widgets.operateList import OperateList
from widgets.dataList import List

from layout.Progress import Progress
import global_var

from layout.data_tail import DataTail,PandasModel

list_itemSize = QSize(100,30)

class MainWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.resize(1080,720)

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
        self.list_in = List()
        self.label_out = QLabel("输出数据")
        self.label_out.setAlignment(Qt.AlignCenter)#居中对齐
        self.list_out = List()
        self.list_in.update_.connect(self.on_listItem_click)
        down_l.addWidget(self.label_in)
        down_l.addWidget(self.list_in)
        down_l.addWidget(self.label_out)
        down_l.addWidget(self.list_out)
        down_l.setStretch(0,1)
        down_l.setStretch(1,7)
        down_l.setStretch(2,1)
        down_l.setStretch(3,7)
        down_l.setSpacing(0)
        #middle(tabs)
        self.tabs = Tabs()
        #right
        self.oprea = OperateList()
        self.oprea.clickBtn_.connect(self.operateChoose)

    #设置UI上下方布局为水平布局
        #up
        layout_up = QHBoxLayout()
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

    #数据导入
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
        #命名数据集并保存
        global_var.dataSet.isLocal = True
        global_var.dataSet.name = self.lineText.text()
        global_var.dataSet.data = pd.read_csv(global_var.filePath)
        dataSet = global_var.dataSet
        global_var.dataList.append(dataSet)
        global_var.dataMap[self.lineText.text()] = dataSet
        self.list_in.add_item(self.lineText.text())
        self.dialog.close()

    @QtCore.pyqtSlot()
    def on_cancel_click(self):
        global_var.filePath = ""
        self.dialog.close()

    @QtCore.pyqtSlot()
    def data_db(self):
        pass

    #运行任务，任务流可以从global_var获取
    @QtCore.pyqtSlot()
    def run(self):
        pass

    @QtCore.pyqtSlot()
    def exit(self):
        pass

    # @QtCore.pyqtSlot()  #该注解会重定义slot为无参类型
    def on_listItem_click(self,dataName):
        df = global_var.dataMap[dataName].data
        tab = DataTail()
        model = PandasModel(df)
        tab.dataTable.setModel(model)
        self.tabs.add_Tab(tab,dataName)

    @QtCore.pyqtSlot()
    def on_listItem_doubleclick(self):
        pass

    def operateChoose(self,operateName):
        #operate为所选择操作名，可以为之创建tab
        tab = QTabWidget() #所选操作对应tab
        self.tabs.add_Tab(tab,operateName)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())