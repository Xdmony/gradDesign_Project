# author:Xdmony
# contact: jerkyadmon@gmail.com
# datetime:2020/4/19 6:09 下午
# software: PyCharm
# description:

"""
文件说明：线性回归实现部分,使用skl的线性回归model
"""

from sklearn import linear_model,model_selection
import pandas as pd
import global_var

def linear_regression(data,scale):
    model = linear_model.LinearRegression()
    feature_list = data.columns.tolist()
    length = len(feature_list)
    X = data[feature_list[0:-1]].values.reshape(-1,length-1)
    y = data[feature_list[-1]].values.reshape(-1,1)
    X_train,X_test,y_train,y_test = model_selection.train_test_split(X,y,test_size=eval(scale))
    model.fit(X_train,y_train)
    y_predict = model.predict(X_test)
    data_in = pd.DataFrame(columns=feature_list[0:-1])
    data_out = pd.DataFrame(columns=feature_list[0:-1])
    for i in range(len(X_test)):
        data_in.loc[i] = X_test[i]
        data_out.loc[i] = X_test[i]
    data_in[feature_list[-1]] = y_test    #训练集
    global_var.data_test = data_in
    data_out[feature_list[-1]] = y_predict     #预测值
    global_var.data_predict = data_out
    #保存数据
    global_var.taskData.model = model       #线性回归model保存
    global_var.taskData.data_in = data_in
    global_var.taskData.data_out = data_out
