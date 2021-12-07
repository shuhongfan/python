"""
@Time ： 2021/12/7 14:56
@Auth ： 021321752215舒洪凡
@File ：35.py
@IDE ：PyCharm
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
#coding:utf-8
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签,下一行的u也是为了正常显示中文
courses = [u'C++', u'Python', u'高数', u'大学英语', u'Java', u'软件工程', u'计算机网络', u'数据结构']
scores = [80, 95, 78, 85, 50, 72, 82, 90]
#把圆周分为datalength份
datalength = len(scores)  #数据长度
angles = np.linspace(0, 2 * np.pi, datalength, endpoint=False)
#设置为极坐标格式
fig, ax=plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
#修改网格的标签为courses列表
plt.thetagrids(angles * 180 / np.pi, courses)

#绘制雷达图外部轮廓
plt.plot(angles,scores,'o-',linewidth=1,alpha=0.25)
#填充内部
plt.fill(angles, scores, facecolor='b', alpha=0.2)
plt.show()