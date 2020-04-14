import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QGroupBox


class Opreation(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.resize(300,710)
        self.btn_pre = QPushButton("预处理")
        self.btn_association = QPushButton("关联分析")
        self.btn_cluster = QPushButton("聚类分析")
        self.btn_classification = QPushButton("分类分析")
        self.btn_regression = QPushButton("回归分析")
        self.btn_visual = QPushButton("可视化工具")
        self.box_pre = QGroupBox()
        self.box_association = QGroupBox()
        self.box_cluster = QGroupBox()
        self.box_classification = QGroupBox()
        self.box_regression = QGroupBox()
        self.box_visual = QGroupBox()

        self.btn_pre.clicked.connect(self.pre)
        self.btn_association.clicked.connect(self.association)

        # 预处理
        layout_pre = QVBoxLayout()
        layout_pre.addWidget(self.btn_pre)
        layout_pre.addWidget(self.box_pre)
        layout_pre.setStretch(0, 1)
        layout_pre.setStretch(1, 5)

        layout1 = QVBoxLayout()
        layout1.addLayout(layout_pre)
        layout1.addWidget(self.btn_association)
        layout1.addWidget(self.btn_cluster)
        layout1.addWidget(self.btn_classification)
        layout1.addWidget(self.btn_regression)
        layout1.addWidget(self.btn_visual)
        layout1.setStretch(0, 6)
        layout1.setStretch(1, 1)
        layout1.setStretch(2, 1)
        layout1.setStretch(3, 1)
        layout1.setStretch(4, 1)
        layout1.setStretch(5, 1)

        # 关联规则
        layout_association = QVBoxLayout()
        layout_association.addWidget(self.btn_association)
        layout_association.addWidget(self.box_association)
        layout_association.setStretch(0, 1)
        layout_association.setStretch(1, 5)

        layout2 = QVBoxLayout()
        layout2.addWidget(self.btn_pre)
        layout2.addLayout(layout_association)
        layout2.addWidget(self.btn_cluster)
        layout2.addWidget(self.btn_classification)
        layout2.addWidget(self.btn_regression)
        layout2.addWidget(self.btn_visual)
        layout2.setStretch(0, 1)
        layout2.setStretch(1, 6)
        layout2.setStretch(2, 1)
        layout2.setStretch(3, 1)
        layout2.setStretch(4, 1)
        layout2.setStretch(5, 1)

        #聚类分析
        layout_cluster = QVBoxLayout()
        layout_cluster.addWidget(self.btn_cluster)
        layout_cluster.addWidget(self.box_cluster)
        layout_cluster.setStretch(0,1)
        layout_cluster.setStretch(1,5)

        layout3 = QVBoxLayout()
        layout3.addWidget(self.btn_pre)
        layout3.addWidget(self.btn_association)
        layout3.addLayout(layout_cluster)
        layout3.addWidget(self.btn_classification)
        layout3.addWidget(self.btn_regression)
        layout3.addWidget(self.btn_visual)

        self.w_pre = QWidget()
        self.w_pre.setLayout(layout1)
        self.w_association = QWidget()
        self.w_association.setLayout(layout2)
        self.w_cluster = QWidget()
        self.w_cluster.setLayout(layout3)
        self.layout = QVBoxLayout()
        # self.layout.addLayout(self.layout1)
        self.layout.addWidget(self.w_cluster)
        self.setLayout(self.layout)

    def pre(self):
        # self.setLayout(self.layout1)
        # self.layout.addLayout(self.layout1)
        # self.layout.removeItem(self.layout2)
        # self.layout.removeWidget(self.box_association)
        # self.layout.removeWidget(self.w_association)
        widget = self.layout.widget()
        self.layout.removeWidget(widget)
        self.layout.addWidget(self.w_pre)

    def association(self):
        # self.setLayout(self.layout2)
        # self.layout.addLayout(self.layout2)
        # self.layout.removeItem(self.layout1)
        widget = self.layout.widget()
        self.layout.removeWidget(widget)
        # self.layout.removeWidget(self.w_cluster)
        self.layout.addWidget(self.w_association)

    def cluster(self):
        # self.layout.removeWidget(self.w_pre)
        # self.layout.removeWidget(self.w_association)
        widget = self.layout.widget()
        self.layout.removeWidget(widget)
        self.layout.addWidget(self.w_cluster)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    opreation = Opreation()
    opreation.show()
    sys.exit(app.exec_())
