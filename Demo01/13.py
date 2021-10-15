age=10
index=0
while index<3:
    ipt = float(input('请输入年龄'))
    if(ipt>age):
        print('超过')
    elif(ipt<age):
        print('太小')
    else:
        print('你猜对了')
        break
    index = index + 1
    if(index==3):
        continue1=input('你还想继续猜吗')
        if(continue1!='n'):
            index=0
        else:
            break