# author:Xdmony
# contact: jerkyadmon@gmail.com
# datetime:2020/4/16 10:21 下午
# software: PyCharm
# description:

"""
文件说明：任务列表，显示已添加操作
"""

import sys

from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QWidget,QApplication,QListWidget,QListWidgetItem,QHBoxLayout,QListView,QPushButton

size = QSize(80,60)

class Progress(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.list = QListWidget()
        self.list.setFlow(QListView.LeftToRight)

        # item1 = QListWidgetItem()
        # item1.setSizeHint(size)
        # item2 = QListWidgetItem()
        # item2.setSizeHint(size)
        # item3 = QListWidgetItem()
        # item3.setSizeHint(size)
        #
        # w1 = QPushButton("item1")
        # w2 = QPushButton("item2")
        # w3 = QPushButton("item3")

        # self.list.addItem(item1)
        # self.list.addItem(item2)
        # self.list.addItem(item3)
        #
        # self.list.setItemWidget(item1,w1)
        # self.list.setItemWidget(item2,w2)
        # self.list.setItemWidget(item3,w3)

        self.layout = QHBoxLayout()
        self.layout.addWidget(self.list)
        self.setLayout(self.layout)

    def addTask(self,taskName):
        item = QListWidgetItem()
        item.setSizeHint(size)
        task = QPushButton(taskName)
        self.list.addItem(item)
        self.list.setItemWidget(item,task)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    progress = Progress()
    progress.show()
    sys.exit(app.exec_())