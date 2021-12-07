"""
@Time ： 2021/12/7 14:09
@Auth ： 021321752215舒洪凡
@File ：34.py
@IDE ：PyCharm
"""

#在当前文件夹中生成饭店营业额模拟数据文件data.csv
import csv
import random
import datetime
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import numpy as np

fn='D:/DEMO/python/Demo02/34/data.csv'
with open(fn,'w')as fp:
    wr=csv.writer(fp)  #一行一行写入csv文件
    wr.writerow(['日期','销量'])  #写入表头
    startDate=datetime.date(2021,1,1) #生成模拟时间
    for i in range(365):#生成365个模拟数据，写入csv
        amount=300+5*i+random.randrange(100)
        wr.writerow([str(startDate),amount])
        startDate=startDate+datetime.timedelta(days=1)#下一天

matplotlib.rcParams['font.sans-serif']=['SimHei'] #pyplot中文显示
df=pd.read_csv('data.csv',encoding='cp936')
df=df.dropna()#读取数据，丢弃缺失值
#生成天营业额折线图
plt.figure()
df.plot(x='日期')
plt.savefig('D:/DEMO/python/Demo02/34/1.jpg')

#生成月营业额柱状图
plt.figure()
df1=df[:]  #str1.rindex(str2)返回子串 str2 在串str1中最后出现位置，如果没有匹配的字符串会报异常
df1['month']=df1['日期'].map(lambda x:x[:x.rindex('-')])#提取出月份,新建了一个month列出来？？
df1=df1.groupby(by='month',as_index=False).sum() #as_inside=False不把month作为新的index
df1.plot(x='month',kind='bar')
plt.savefig('D:/DEMO/python/Demo02/34/2.jpg')

#查找涨幅最大月份，写入文件
plt.figure()
df2=df1.drop('month',axis=1).diff()#在销量列中每月跟上月相减的差集
m=df2['销量'].nlargest(1).keys()[0]#查找销量列中差集最大的一个数所对应的索引
with open('D:/DEMO/python/Demo02/34/maxMonth.txt','w')as fp:
   fp.write(df1.loc[m,'month'])#索引m对应的month

#生成季度营业额饼状图
plt.figure()
one=df1[:3]['销量'].sum()
two=df1[3:6]['销量'].sum()
three=df1[6:9]['销量'].sum()
four=df1[9:12]['销量'].sum()
y = np.array([35, 25, 25, 15])
plt.pie(y,labels=['one','two','three','four'],
        colors=["#d5695d", "#5d8ca8", "#65a479", "#a564c9"], # 设置饼图颜色
        explode=(0, 0.2, 0, 0), # 第二部分突出显示，值越大，距离中心越远
        autopct='%.2f%%', # 格式化输出百分比
);
plt.title("2021年4个季度的营业额")
plt.savefig('D:/DEMO/python/Demo02/34/3.jpg')
