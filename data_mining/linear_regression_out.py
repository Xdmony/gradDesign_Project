# author:Xdmony
# contact: jerkyadmon@gmail.com
# datetime:2020/4/19 5:57 下午
# software: PyCharm
# description:

"""
文件说明：
"""
from PyQt5.QtWidgets import QWidget,QLabel,QVBoxLayout,QHBoxLayout
from layout.data_tail import DataTail_Out,PandasModel
import global_var


class LR_out(QWidget):
    def __init__(self):
        super(LR_out,self).__init__()
        model_label1 = QLabel("斜率：  "+str(global_var.taskData.model.coef_))
        model_label2 = QLabel("截距：  "+str(global_var.taskData.model.intercept_))
        test_label = QLabel("测试集：")
        predict_label = QLabel("预测值：")
        test_data = DataTail_Out()
        model_in = PandasModel(global_var.taskData.data_in)
        test_data.dataTable.setModel(model_in)
        predict_data = DataTail_Out()
        model_out = PandasModel(global_var.taskData.data_out)
        predict_data.dataTable.setModel(model_out)
        layout = QVBoxLayout()  #总体布局
        layout_model = QHBoxLayout()
        layout_model.addWidget(model_label1)
        layout_model.addWidget(model_label2)
        layout.addLayout(layout_model)
        layout.addWidget(test_label)
        layout.addWidget(test_data)
        layout.addWidget(predict_label)
        layout.addWidget(predict_data)
        layout.setStretch(0,1)
        layout.setStretch(1,1)
        layout.setStretch(2,5)
        layout.setStretch(3,1)
        layout.setStretch(4,5)
        self.setLayout(layout)