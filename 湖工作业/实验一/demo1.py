from datetime import datetime

name= input("请输入您的姓名：")
year= input("请输入您的出生年份：")
print("您好！{}。 您 {} 岁。".format(name,datetime.now().year-int(year)))
