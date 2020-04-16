# author:Xdmony
# contact: jerkyadmon@gmail.com
# datetime:2020/4/16 10:13 下午
# software: PyCharm
# description:

"""
文件说明：tab编辑区
"""

from PyQt5.QtWidgets import QTabWidget

class Tabs(QTabWidget):
    def __init__(self):
        QTabWidget.__init__(self)
        self.setTabsClosable(True)
        self.setTabShape(QTabWidget.Triangular)
        self.setDocumentMode(True)
        self.tabCloseRequested.connect(self.close_Tab)

    def close_Tab(self,index):
        self.removeTab(index)

    def add_Tab(self,tab,title):
        self.addTab(tab,title)