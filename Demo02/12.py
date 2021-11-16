"""
@Time ： 2021/11/2 15:12
@Auth ： 021321752215舒洪凡
@File ：12.py
@IDE ：PyCharm
"""
origin="C:/Users/SHF/AppData/Local/Programs/Python/Python39/python.exe D:/DEMO/python/Demo02/11.py"
print("origin=",origin)
userInput=input("请按照原始字符串输入：")
if len(origin)<len(userInput):
    print("输入字符串和原始字符串长度不一致！")
right=sum(1 for oc,uc in zip(origin,userInput) if oc==uc)
rate=right/len(origin)
print("正确率为 ",round(rate*100,2)," %")