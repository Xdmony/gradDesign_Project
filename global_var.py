
"""
@description: 存储所有全局变量
"""

class DataSet():
    def __init__(self):
        self.name=None
        self.data=None
        self.isLocal = True
        self.path = None#本地文件才有路径
        # if not self.isLocal:
        #     self.path = None


#文件路径只在本地读取文件的时候使用，其他模块使用dataSet.path访问本地原始数据
filePath = ""

#数据集列表
dataList = list()

#数据集
dataSetInput = dict()
dataSetOutput = dict()

#数据集
dataSet = DataSet()

#数据集别名
dataMap = dict()

#可选操作配置
preBtnList = ["数据清洗","数据集成","数据变换","特征选择","特征提取"]
associationBtnList = ["apriori关联规则"]
clusterBtnList = ["k-means聚类"]
classificationBtnList = ["决策树分类"]
regressionBtnList = ["线性回归"]
visualBtnList = ["散点图"]

