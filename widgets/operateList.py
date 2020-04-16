
"""
@description: 数据挖掘和预处理菜单
"""

from PyQt5.QtCore import QSize, pyqtSignal
from PyQt5.QtWidgets import QWidget, QPushButton, QFormLayout, \
    QListWidget, QListWidgetItem, QHBoxLayout
import global_var

"""
# preList = ["数据清洗","数据集成","数据变换","特征选择","特征提取"]
# associationList = ["apriori关联规则"]
# clusterList = ["k-means聚类"]
# classificationList = ["决策树分类"]
# regressionList = ["线性回归"]
# visualList = ["散点图"]
"""

operateBtnAll = [global_var.preBtnList, global_var.associationBtnList, global_var.clusterBtnList,
                 global_var.classificationBtnList, global_var.regressionBtnList, global_var.visualBtnList]

class CustomWidget(QWidget):
    click_ = pyqtSignal(str)
    def __init__(self, item,index, *args, **kwargs):
        super(CustomWidget, self).__init__(*args, **kwargs)
        self.oldSize = None
        self.item = item
        layout = QFormLayout(self)
        layout.setSpacing(5)
        layout.setContentsMargins(0,5,0,0)
        for btn in operateBtnAll[index]:
            layout_line = QHBoxLayout()
            layout_line.addStretch(1)
            button = QPushButton(btn)
            button.clicked.connect(self.operateClick)
            layout_line.addWidget(button)
            layout_line.setStretch(1,7)
            layout_line.addStretch(1)
            layout.addRow(layout_line)

    def operateClick(self):
        print("btnClicked")
        operate = self.sender().text()
        self.click_.emit(operate)

    def resizeEvent(self, event):
        # 解决item的高度问题
        super(CustomWidget, self).resizeEvent(event)
        self.item.setSizeHint(QSize(self.minimumWidth(), self.height()))


class CustomButton(QPushButton):
    # 按钮作为开关

    def __init__(self, item, *args, **kwargs):
        super(CustomButton, self).__init__(*args, **kwargs)
        self.item = item
        self.setCheckable(True)  # 设置可选中

    def resizeEvent(self, event):
        # 解决item的高度问题
        super(CustomButton, self).resizeEvent(event)
        self.item.setSizeHint(QSize(self.minimumWidth(), self.height()))


class OperateList(QListWidget):
    clickBtn_ = pyqtSignal(str)
    def __init__(self, *args, **kwargs):
        super(OperateList, self).__init__(*args, **kwargs)

        operate = ["数据预处理","关联分析","聚类分析","分类分析","回归分析","可视化工具"]
        for i in operate:
            # 开关
            self.item = QListWidgetItem(self)
            btn = CustomButton(self.item, i, self, objectName='testBtn')
            self.setItemWidget(self.item, btn)

            # 被折叠控件
            self.item = QListWidgetItem(self)
            self.item.setSelected(False)
            # 通过按钮的选中来隐藏下面的item
            btn.toggled.connect(self.item.setHidden)
            index = operate.index(i)
            self.widget = CustomWidget(self.item,index)
            self.setItemWidget(self.item, self.widget)

            self.widget.click_.connect(self.itemClick)
    def itemClick(self,txt):
        self.clickBtn_.emit(txt)



if __name__ == '__main__':
    import sys
    import cgitb
    sys.excepthook = cgitb.enable(1, None, 5, '')
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    # 通过qss改变按钮的高度
    app.setStyleSheet('#testBtn{min-height:40px;}')
    w = OperateList()
    w.show()
    sys.exit(app.exec_())