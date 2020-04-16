# author:Xdmony
# contact: jerkyadmon@gmail.com
# datetime:2020/4/16 10:11 下午
# software: PyCharm
# description:

"""
文件说明：显示输入输出数据集的List控件
"""


from PyQt5.QtCore import QSize, pyqtSignal
from PyQt5.QtWidgets import QListWidget, QListWidgetItem, QPushButton, QWidget, QHBoxLayout, QTabWidget

itemSize = QSize(100,30)

class List(QListWidget):
    update_ = pyqtSignal(str)

    def __init__(self):
        QListWidget.__init__(self)

    def add_item(self,dataName):
        item = QListWidgetItem()
        item.setSizeHint(itemSize)
        self.addItem(item)
        itemBtn = QPushButton(dataName)
        self.setItemWidget(item,itemBtn)
        itemBtn.clicked.connect(self.item_click)

    def item_click(self):
        dataName = self.sender().text()
        self.update_.emit(dataName)


"""
测试用
"""
class Window(QWidget):
    def __init__(self):
        super(Window,self).__init__()
        layout = QHBoxLayout()
        self.list = List()
        self.list.add_item("test")
        self.tabs = QTabWidget()
        layout.addWidget(self.list)
        layout.addWidget(self.tabs)
        self.list.update_.connect(self.click_test)

        self.setLayout(layout)

    def click_test(self, txt):
        tab = QWidget()
        self.tabs.addTab(tab,txt)


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    l = Window()
    l.show()
    sys.exit(app.exec_())

