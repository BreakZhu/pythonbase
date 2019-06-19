# /usr/bin/python
# -*- encoding:utf-8 -*-

import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.cluster import KMeans, SpectralClustering, DBSCAN
import pandas as pd
import matplotlib.colors
import matplotlib.pyplot as plt

from sklearn.manifold import TSNE
from sklearn import metrics


def show_accuracy(a, b, tip):
    acc = a.ravel() == b.ravel()
    acc_rate = 100 * float(acc.sum()) / a.size
    # print '%s正确率：%.3f%%' % (tip, acc_rate)
    return acc_rate


def expand(a, b):
    d = (b - a) * 0.1
    return a - d, b + d


def load_data(file_name, is_train):
    data = pd.read_csv(file_name, index_col="PassengerId")  # 数据文件路径
    # print data.describe()
    # 性别
    data['Sex'] = data['Sex'].map({'female': 0, 'male': 1}).astype(int)
    # 补齐船票价格缺失值
    if len(data.Fare[data.Fare.isnull()]) > 0:
        fare = np.zeros(3)
        for f in range(0, 3):
            fare[f] = data[data.Pclass == f + 1]['Fare'].dropna().median()
        for f in range(0, 3):  # loop 0 to 2
            data.loc[(data.Fare.isnull()) & (data.Pclass == f + 1), 'Fare'] = fare[f]
    # 年龄：使用均值代替缺失值
    # mean_age = data['Age'].dropna().mean()
    # data.loc[(data.Age.isnull()), 'Age'] = mean_age
    if is_train:
        # 年龄：使用随机森林预测年龄缺失值
        print('随机森林预测缺失年龄：--start--')
        data_for_age = data[['Age', 'Survived', 'Fare', 'Parch', 'SibSp', 'Pclass']]
        age_exist = data_for_age.loc[(data.Age.notnull())]  # 年龄不缺失的数据
        age_null = data_for_age.loc[(data.Age.isnull())]
        # print age_exist
        x = age_exist.values[:, 1:]
        y = age_exist.values[:, 0]
        rfr = RandomForestRegressor(n_estimators=1000)
        rfr.fit(x, y)
        age_hat = rfr.predict(age_null.values[:, 1:])
        # print age_hat
        data.loc[(data.Age.isnull()), 'Age'] = age_hat
        print('随机森林预测缺失年龄：--over--')
    else:
        print('随机森林预测缺失年龄2：--start--')
        data_for_age = data[['Age', 'Fare', 'Parch', 'SibSp', 'Pclass']]
        age_exist = data_for_age.loc[(data.Age.notnull())]  # 年龄不缺失的数据
        age_null = data_for_age.loc[(data.Age.isnull())]
        # print age_exist
        x = age_exist.values[:, 1:]
        y = age_exist.values[:, 0]
        rfr = RandomForestRegressor(n_estimators=1000)
        rfr.fit(x, y)
        age_hat = rfr.predict(age_null.values[:, 1:])
        # print age_hat
        data.loc[(data.Age.isnull()), 'Age'] = age_hat
        print('随机森林预测缺失年龄2：--over--')
    # 起始城市
    data.loc[(data.Embarked.isnull()), 'Embarked'] = 'S'  # 保留缺失出发城市
    embarked_data = pd.get_dummies(data.Embarked)
    embarked_data = embarked_data.rename(columns=lambda x: 'Embarked_' + str(x))
    data = pd.concat([data, embarked_data], axis=1)
    print(data.describe())
    data.to_csv('./KMeanNew_Data.csv')
    # y = None
    # if 'Survived' in data:
    #     y = data['Survived']
    # if is_train:
    #    return x, y
    return data[
        ['Pclass', 'Survived', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked_C',
         'Embarked_Q', 'Embarked_S', 'Embarked_U']]


def kmeans_cluster(train_data):
    # get KMeans
    cluster_model = KMeans(n_clusters=6, init='k-means++', n_jobs=6, max_iter=500)
    cluster_model.fit(train_data)
    # 简单打印结果
    r1 = pd.Series(cluster_model.labels_).value_counts()  # 统计各个类别的数目
    r2 = pd.DataFrame(cluster_model)  # 找出聚类中心
    r = pd.concat([r2, r1], axis=1)  # 横向连接(0是纵向), 得到聚类中心对应的类别下的数目
    r.columns = list(train_data.columns) + [u'类别数目']  # 重命名表头
    matplotlib.rcParams['font.sans-serif'] = [u'SimHei']
    matplotlib.rcParams['axes.unicode_minus'] = False
    print(r)
    plot_cluster_data(cluster_model.labels_, train_data)


def plot_cluster_data(labels, train_data):
    # 详细输出原始数据及其类别
    r = pd.concat([train_data, pd.Series(labels, index=train_data.index)], axis=1)  # 详细
    # 输出每个样本对应的类别
    r.columns = list(train_data.columns) + [u'聚类类别']  # 重命名表头
    r.to_excel(outputfile)  # 保存结果
    # 聚类可视化降维
    tsne = TSNE()
    tsne.fit_transform(train_data)  # 进行数据降维
    tsne = pd.DataFrame(tsne.embedding_, index=train_data.index)  # 转换数据格式
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
    # 不同类别用不同颜色和样式绘图
    d = tsne[r[u'聚类类别'] == 0]
    plt.plot(d[0], d[1], 'r.')
    d = tsne[r[u'聚类类别'] == 1]
    plt.plot(d[0], d[1], 'go')
    d = tsne[r[u'聚类类别'] == 2]
    plt.plot(d[0], d[1], 'b*')
    d = tsne[r[u'聚类类别'] == 3]
    plt.plot(d[0], d[1], 'mp')
    d = tsne[r[u'聚类类别'] == 4]
    plt.plot(d[0], d[1], 'yh')
    d = tsne[r[u'聚类类别'] == 5]
    plt.plot(d[0], d[1], 'kd')
    plt.show()


def db_scan(train_data):
    colrs = ('r.', 'go', 'b*', 'mp', 'yh', 'kd', 'rv', 'g<', 'b-', 'md', 'y*', 'kp')
    # 数据1的参数：(epsilon, min_sample)
    params = ((0.2, 5), (0.2, 10), (0.2, 15), (0.3, 5), (0.3, 10), (0.3, 15))
    # # 数据2的参数：(epsilon, min_sample)
    # params = ((0.5, 3), (0.5, 5), (0.5, 10), (1., 3), (1., 10), (1., 20))
    matplotlib.rcParams['font.sans-serif'] = [u'SimHei']
    matplotlib.rcParams['axes.unicode_minus'] = False
    for i in range(6):
        eps, min_samples = params[i]
        model = DBSCAN(eps=eps, min_samples=min_samples)
        model.fit(train_data)
        y_hat = model.labels_
        # 详细输出原始数据及其类别
        r = pd.concat([train_data, pd.Series(model.labels_, index=train_data.index)], axis=1)  # 详细
        # 输出每个样本对应的类别
        r.columns = list(train_data.columns) + [u'聚类类别']  # 重命名表头
        r.to_excel(outputfile)  # 保存结果
        # 聚类可视化降维
        tsne = TSNE()
        tsne.fit_transform(train_data)  # 进行数据降维
        tsne = pd.DataFrame(tsne.embedding_, index=train_data.index)  # 转换数据格式
        plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
        plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
        y_unique = np.unique(y_hat)
        for y_ in y_unique:
            d = tsne[r[u'聚类类别'] == y_]
            plt.plot(d[0], d[1], colrs[y_])
        # ur
        plt.title('$\epsilon$ = %.1f  m = %d，聚类数目：%d' % (eps, min_samples, len(np.unique(y_hat))), fontsize=16)
        plt.show()


def spectral_cluster(train_data):
    matplotlib.rcParams['font.sans-serif'] = [u'SimHei']
    matplotlib.rcParams['axes.unicode_minus'] = False
    # for index, gamma in enumerate((0.01, 0.1, 0.2, 0.3, 1, 10)):
    #     for index, k in enumerate((3, 4, 5, 6)):
    #         y_pred = SpectralClustering(n_clusters=k, gamma=gamma).fit_predict(train_data)
    #         print("Calinski-Harabasz Score with gamma=", gamma, "n_clusters=", k, "score:",\
    #               metrics.calinski_harabaz_score(train_data, y_pred))
    y_ = SpectralClustering(n_clusters=5, gamma=0.1).fit_predict(train_data)
    cluster_label = np.unique(y_)
    print(cluster_label)
    print("Calinski-Harabasz Score", metrics.calinski_harabaz_score(train_data, y_))
    r = pd.concat([train_data, pd.Series(y_, index=train_data.index)], axis=1)  # 详细
    r.columns = list(train_data.columns) + [u'聚类类别']  # 重命名表头
    print(r)
    plot_cluster_data(y_, train_data)


if __name__ == "__main__":
    outputfile = "TitanicCluster_data.xls"
    data = load_data('ClusterTitanic.train.csv', True)
    # kmeans_cluster(data)
    # db_scan(data)
    spectral_cluster(data)
