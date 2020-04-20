# author:Xdmony
# contact: jerkyadmon@gmail.com
# datetime:2020/4/20 12:36 下午
# software: PyCharm
# description:

"""
文件说明：执行任务时调用
"""

import global_var
import data_mining.linear_regression as lr
from data_mining.linear_regression_out import LR_out

def task_run():
    data = global_var.taskData.data     #任务数据（pandas DataFrame）
    pretreat = global_var.taskData.pretreat     #预处理
    data_mining = global_var.taskData.data_mining       #数据挖掘
    visual = global_var.taskData.visual     #数据可视化

    #根据taskData确定任务流
    if pretreat!="" and pretreat!=None:
        pass
    elif data_mining!="" and data_mining!=None:
        if data_mining==global_var.associationBtnList[0]:
            pass
        elif data_mining==global_var.classificationBtnList[0]:
            pass
        elif data_mining==global_var.clusterBtnList[0]:
            pass
        elif data_mining==global_var.regressionBtnList[0]:
            lr.linear_regression(data,global_var.scale)
            tab = LR_out()
            return tab,global_var.regressionBtnList[0]
    elif visual!="" and visual!=None:
        pass