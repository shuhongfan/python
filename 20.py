def common_mutiple(x,y):
    if x>y:
        bigger=x
    else:
        bigger=y
    while 1:
        if(bigger%x==0) and (bigger%y==0):
            cm=bigger
            break
        bigger+=1

    return cm

num1=int(input('请输入第一个正整数：'))
num2=int(input('请输入第二个正整数：'))
print(num1,'和',num2,'的最小公倍数是',common_mutiple(num1,num2))