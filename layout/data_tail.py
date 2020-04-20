# author:Xdmony
# contact: jerkyadmon@gmail.com
# datetime:2020/4/16 10:17 下午
# software: PyCharm
# description:

"""
文件说明：数据集详情
"""
import sys

from PyQt5 import QtCore
import pandas as pd
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QTableView, QFormLayout, QLabel, QComboBox, QPushButton,\
    QApplication
import global_var

class PandasModel(QtCore.QAbstractTableModel):
    def __init__(self, df = pd.DataFrame(), parent=None):
        QtCore.QAbstractTableModel.__init__(self, parent=parent)
        self._df = df

    def headerData(self, section, orientation, role=QtCore.Qt.DisplayRole):
        if role != QtCore.Qt.DisplayRole:
            return QtCore.QVariant()

        if orientation == QtCore.Qt.Horizontal:
            try:
                return self._df.columns.tolist()[section]
            except (IndexError, ):
                return QtCore.QVariant()
        elif orientation == QtCore.Qt.Vertical:
            try:
                return self._df.index.tolist()[section]
            except (IndexError, ):
                return QtCore.QVariant()

    def data(self, index, role=QtCore.Qt.DisplayRole):
        if role != QtCore.Qt.DisplayRole:
            return QtCore.QVariant()

        if not index.isValid():
            return QtCore.QVariant()

        return QtCore.QVariant(str(self._df.ix[index.row(), index.column()]))

    def setData(self, index, value, role):
        row = self._df.index[index.row()]
        col = self._df.columns[index.column()]
        if hasattr(value, 'toPyObject'):
            # PyQt4 gets a QVariant
            value = value.toPyObject()
        else:
            # PySide gets an unicode
            dtype = self._df[col].dtype
            if dtype != object:
                value = None if value == '' else dtype.type(value)
        self._df.set_value(row, col, value)
        return True

    def rowCount(self, parent=QtCore.QModelIndex()):
        return len(self._df.index)

    def columnCount(self, parent=QtCore.QModelIndex()):
        return len(self._df.columns)

    def sort(self, column, order):
        colname = self._df.columns.tolist()[column]
        self.layoutAboutToBeChanged.emit()
        self._df.sort_values(colname, ascending= order == QtCore.Qt.AscendingOrder, inplace=True)
        self._df.reset_index(inplace=True, drop=True)
        self.layoutChanged.emit()


class DataCol(QWidget):
    def __init__(self):
        super(DataCol,self).__init__()
        self.dataColBox = QComboBox()
        colList = global_var.currentDataSet.data.columns.tolist()
        colList.insert(0, "")
        for col in colList:
            self.dataColBox.addItem(col)
        layout = QHBoxLayout()
        layout.addWidget(self.dataColBox)
        self.setLayout(layout)


class DataTail(QWidget):
    add_ = pyqtSignal(str)

    def __init__(self):
        super(DataTail,self).__init__()
        self.dataTable = QTableView()
        # self.dataTable.setModel(PandasModel(data))
        layout = QHBoxLayout()
        layout.addWidget(self.dataTable)
        layout_tail = QFormLayout()
        self.data_x1 = DataCol()
        self.data_x2 = DataCol()
        self.data_x3 = DataCol()
        self.data_x4 = DataCol()
        self.data_y = DataCol()
        layout_tail.addRow(QLabel("X1:"), self.data_x1)
        layout_tail.addRow(QLabel("X2:"), self.data_x2)
        layout_tail.addRow(QLabel("X3:"), self.data_x3)
        layout_tail.addRow(QLabel("X4:"), self.data_x4)
        layout_tail.addRow(QLabel("Y:"), self.data_y)
        btn_add = QPushButton("添加到任务")
        btn_add.clicked.connect(self.btn_click)
        layout_tail.addRow(btn_add)
        layout.addLayout(layout_tail)
        layout.setStretch(0,5)
        layout.setStretch(1,1)
        self.setLayout(layout)

    def btn_click(self):
        X = list()
        if self.data_x1.dataColBox.currentText()!="":
            X.append(self.data_x1.dataColBox.currentText())
        if self.data_x2.dataColBox.currentText() != "":
            X.append(self.data_x2.dataColBox.currentText())
        if self.data_x3.dataColBox.currentText()!="":
            X.append(self.data_x3.dataColBox.currentText())
        if self.data_x4.dataColBox.currentText()!="":
            X.append(self.data_x4.dataColBox.currentText())
        y = self.data_y.dataColBox.currentText()
        data = pd.DataFrame()
        for i in X:
            data[i] = global_var.currentDataSet.data[i]
        data[y] = global_var.currentDataSet.data[y]
        global_var.taskData.X = X
        global_var.taskData.y = y
        global_var.taskData.data = data
        global_var.taskData.dataSet = global_var.currentDataSet
        txt = global_var.taskData.dataSet.name
        global_var.taskList[global_var.taskData.dataSet.name] = global_var.taskData     #保存任务数据到taskList字典
        self.add_.emit(txt)

class DataTail_Out(QWidget):
    add_ = pyqtSignal(str)

    def __init__(self):
        super(DataTail_Out,self).__init__()
        self.dataTable = QTableView()
        # self.dataTable.setModel(PandasModel(data))
        layout = QHBoxLayout()
        layout.addWidget(self.dataTable)
        # layout_tail = QFormLayout()
        # self.data_x1 = DataCol()
        # self.data_x2 = DataCol()
        # self.data_x3 = DataCol()
        # self.data_x4 = DataCol()
        # self.data_y = DataCol()
        # layout_tail.addRow(QLabel("X1:"), self.data_x1)
        # layout_tail.addRow(QLabel("X2:"), self.data_x2)
        # layout_tail.addRow(QLabel("X3:"), self.data_x3)
        # layout_tail.addRow(QLabel("X4:"), self.data_x4)
        # layout_tail.addRow(QLabel("Y:"), self.data_y)
        # btn_add = QPushButton("添加到任务")
        # btn_add.clicked.connect(self.btn_click)
        # layout_tail.addRow(btn_add)
        # layout.addLayout(layout_tail)
        # layout.setStretch(0,5)
        # layout.setStretch(1,1)
        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    datatail = DataTail()
    datatail.show()
    sys.exit(app.exec_())