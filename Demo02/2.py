'''
p=open("D:/test.txt","a+")
print("helloworld",file=fp)
fp.close()
'''
import random

usd_str=100

print('美元金额为：',usd_str)
# print('美元金额为：'usd_str)
print('美元金额为：,usd_str')

print(40-3**2+11//3**2*8)
print(11//3**2)

print('{0},{1}'.format('carmen',20))

a="hellopython3.8"
print(a[-1:])

a=[1,2,3]
b=[3,4,5]
print(a+b)

x=[1,2,3,4]
x.append(5)
x.reverse()
print(x)
x.pop(1)
total=sum(x)
print(total)

# dict1={}
# dict2 = {2:6}
# dict3={[1,2,3]:"users"}
# dict4={(1,2,3):"users"}
# print(dict3)

a={'1':2,'2':3}
a[1]=5
print(a)

print(sorted([1,5,8],reverse=True))
print(reversed([1,5,8]))
print(sorted([1,5,8],reverse=True)==reversed([1,5,8]))

x=[3,7,5]
x=sorted(x,reverse=True)
print(x)

x=list(range(10))
print(x[:-5])

a=3
b=4
a,b=b,a
print(a,b)

t=a;
a=b;
b=t;
print(a,b)


a=a+b
b=a-b
a=a-b
print(a,b)


a=a-b
b=a+b
a=a+b
print(a,b)

# x=99999**9999999
# print(x)

print(1,2,9,sep=":")
