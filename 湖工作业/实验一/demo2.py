num=int(input("请输入数字："))
sum=0
while num>0:
    sum+=num%10;
    num//=10;
print('各位数字之和为：{}'.format(sum))