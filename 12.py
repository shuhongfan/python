age=10
while True:
    ipt = float(input('请输入年龄'))
    if(ipt>age):
        print('超过')
    elif(ipt<age):
        print('太小')
    else:
        print('你猜对了')
        break