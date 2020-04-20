# author:Xdmony
# contact: jerkyadmon@gmail.com
# datetime:2020/4/16 10:18 下午
# software: PyCharm
# description:

"""
文件说明：存储项目全局变量
"""


class DataSet():
    def __init__(self):
        self.name=None          #数据集ID
        self.data=None          #数据
        self.isLocal = True     #是否是本地文件
        self.path = None#本地文件才有路径
        # if not self.isLocal:
        #     self.path = None

class Task():
    def __init__(self):
        self.X = None           #list X
        self.y = None           #String y
        self.dataSet = None     #原始数据集
        self.data = None        #数据集（不能为空），数据处理的输入（DataFrame）
        self.scale = None       #样本占比
        self.pretreat = None    #预处理
        self.data_mining = None #数据挖掘
        self.visual = None      #数据可视化
        self.model = None       #数据挖掘model
        self.data_in = None     #测试集
        self.data_out = None    #预测值
        self.dataTab = None     #输出数据tab
        self.pretreatData = None                        #数据预处理输出数据

#当前使用的数据集
currentDataSet = None

#数据集(currentDataSet)，当前数据集指针
dataSet = DataSet()

#任务流数据          当前任务指针
taskData = Task()

#文件路径只在本地读取文件的时候使用，其他模块使用dataSet.path访问本地原始数据
filePath = ""

#数据集列表
dataList = list()

#输入和输出数据集，数据类型为DataSet {dataName:dataSet}
dataSetInput = dict()
dataSetOutput = dict()


#所有数据集(通过数据集name查询数据)
dataMap = dict()

#可选操作配置，数据预处理、数据挖掘、数据可视化
preBtnList = ["数据清洗","数据集成","数据变换","特征选择","特征提取"]
associationBtnList = ["apriori关联规则"]
clusterBtnList = ["k-means聚类"]
classificationBtnList = ["决策树分类"]
regressionBtnList = ["线性回归"]
visualBtnList = ["散点图"]

#存储任务配置
scale = 0.3 #训练集占比
X_test = None
y_test = None
y_predict = None
data_test = None
data_predict = None

taskList = dict()   #存储任务数据，{dataName:taskData}，根据输出数据集查询
