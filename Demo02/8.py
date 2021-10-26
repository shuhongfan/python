# 021321752215舒洪凡
# 2021年10月26日16:06:13

import random
randomNum=random.randint(0,100)
flag=5

for i in range(0,flag):
    print("还剩",flag-i,'次机会')
    num=input("请输入数字：")
    while not num.isdigit():
        num=input("类型不合法请重新输入！！！请输入数字：")
    num=int(num)
    if num>randomNum:
        print("猜大了")
    elif num<randomNum:
        print("猜小了")
    else:
        print("猜对了")
        break

print("随机生成的数字为：",randomNum)