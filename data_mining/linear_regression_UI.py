# author:Xdmony
# contact: jerkyadmon@gmail.com
# datetime:2020/4/19 4:02 下午
# software: PyCharm
# description:

"""
文件说明：线性回归
"""
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget,QHBoxLayout,QVBoxLayout,QLabel,QLineEdit,QPushButton
import global_var


class Linear(QWidget):
    add_ = pyqtSignal(str)
    def __init__(self):
        super(Linear,self).__init__()
        layout_h = QHBoxLayout()
        layout_v = QVBoxLayout()
        label_scale = QLabel("样本占比：")
        self.input_scale = QLineEdit()
        layout_h.addWidget(label_scale)
        layout_h.addWidget(self.input_scale)
        layout_h.addStretch(3)
        layout_v.addLayout(layout_h)
        layout_btn = QHBoxLayout()
        layout_btn.addStretch(3)
        btn = QPushButton("添加至任务")
        btn.clicked.connect(self.addTask)
        layout_btn.addWidget(btn)
        layout_v.addLayout(layout_btn)
        layout_v.addStretch(5)
        self.setLayout(layout_v)

    def addTask(self):
        scale = self.input_scale.text()
        txt = global_var.regressionBtnList[0]
        global_var.scale = scale
        global_var.taskData.data_mining = txt
        self.add_.emit(txt)