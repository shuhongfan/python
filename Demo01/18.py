def getMax():
    num1 = int(input('请输入数字1-->'))
    num2 = int(input('请输入数字2-->'))
    num3 = int(input('请输入数字3-->'))
    max = 0
    if num1>num2:
        max=num1
    else:
        max=num2

    if max>num3:
        return '三个数中最大的是：'+str(max)
    else:
        return '三个数中最大的是：' + str(num3)

maxVal=getMax()
print(maxVal)