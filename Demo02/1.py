from decimal import Decimal

print("shf " * 30)

print(type(int("123")))
print(type(float("123")))

print(0b10101111)
print(0o10101111)

n1 = 1.1
n2 = 2.2
print(n1 + n2)

print(Decimal(n1) + Decimal(n2))

str11 = """123

5
"""
print(str11)

print(11 // 5)

print(2 ** 2)

a, b, c = 20, 30, 40
print(a, b, c)

a, b = 10, 20
print(a, b)
a, b = b, a
print(a, b)

a = 10
b = 10
print(a == b)
print(a is b)

lst1 = [11, 22, 33, 44]
lst2 = [11, 22, 33, 44]
print(lst1 == lst2)
print(id(lst1))
print(id(lst2))
print(lst1 is lst2)
print(lst1 is not lst2)

s = 'hello'
print('p' in s)

print(4 & 8)
print(4 | 8)
print(4 << 2)
print(4 >> 2)

# money=1000
# s=int(input("请输入取款余额"))
# if money>=s:
#     money=money-s
#     print("取款成功，余额为：",money)

# num=int(input('请输入数字：'))
# if num%2==0:
#     print("偶数");
# else:
#     print("奇数")

# score=int(input('请输入一个成绩：'))
# if score>=90 and score<=100:
#     print("A")
# elif score>=80 and score<90:
#     print("B")
# elif score>=70 and score<80:
#     print("C")
# elif score>=60 and score<70:
#     print("D")
# else:
#     print("E")

# score=int(input('请输入一个成绩：'))
# if 90<=score<=100:
#     print("A")
# elif 80<=score<90:
#     print("B")
# elif 70<=score<80:
#     print("C")
# elif 60<=score<70:
#     print("D")
# else:
#     print("E")


# answer=input('您是会员吗？y/n')
# money=int(input('请输入您的购物金额：'))
# if answer=='y':
#     if money >=200:
#         print('打8折，付款金额为：',money*0.8)
#     elif money>=100:
#         print('打9折，付款金额为：',money*0.9)
#     else:
#         print('不打折，付款金额为：',money)
# else:
#     if money>=200:
#         print('打9.5折，付款金额为：',money*0.95)
#     else:
#         print('不打折，付款金额为:',money)

# num1=int(input('请输入第一个整数：'))
# num2=int(input('请输入第二个整数：'))
#
# if num1>=num2:
#     print(num1,'大于',num2)
# else:
#     print(num1,'小于',num2)
#
# print(str(num1)+'大于'+str(num2) if num1>=num2 else str(num1)+'小于'+str(num2))

# answer=input("您是会员吗？y/n")
# if answer:
#     pass

r = range(10)
print(r)
print(list(r))

r = range(1, 10, 2)
print(list(r))

print(10 in r)
print(10 not in r)

# a = 1
# while a < 10:
#     print(a)
#     a += 1
#
# a=1
# sum=0
# while a<10:
#     sum+=a
#     a+=1
# print(sum)


# a=1
# sum=0
# while a<100:
#     if a%2:
#         sum+=a
# print(sum)


for item in 'python':
    print(item)

for i in range(10):
    print(i)

for _ in range(10):
    print('人生苦短，我用Python')

sum=0
for item in range(1,100):
    if item%2:
        sum+=item
print(sum)

for i in range(100,1000):
    ge=i%10
    shi=i//10%10
    bai=i//100
    # print(ge,shi,bai)
    if ge**3+shi**3+bai**3==i:
        print(i)

# for i in range(3):
#     pwd=input('input password:')
#     if pwd=='8888':
#         print('密码正确')
#         break
#     else:
#         print('密码不正确')
# else:
#     print('3次密码均输入错误')

# for i in range(1,51):
#     if i%5==0:
#         print(i)

for i in range(1,51):
    if i%5!=0:
        continue
    print(i)

a=range(1,4)
print(list(a))


for i in range(1,4):
    for i in range(1,5):
        print('*',end='\t')
    print()

for i in range(1,10):
    for j in range(1,i+1):
        print("*",end=' ')
    print("\n")

for i in range(1,10):
    for j in range(1,i+1):
        print(i,'*',j,'= ',(i*j),end='  ')
    print()

for i in range(5):
    for j in range(1,11):
        if j%2==0:
            continue
        print(j,end='\t')
    print()

a=10
lst=['hello','world',98]
print(id(lst))
print(type(lst))
print(lst)

lst2 = list(['hello', 'world', 98])
print(lst2)
print(lst2[2])
print(lst2[-2])
lst2.append({'fs',"dsf"})
lst2.append('world')
print(lst2)

print(lst2.index('world'))
# print(lst2.index('hello',1,4))
print(lst2[-2])

lst3=lst2[1:6]
print(lst3)

print(lst2[::-1])
print(lst2[3::-1])

print(98 in lst2)

for i in lst2:
    print(i)

lst2.append(lst3)
print(lst2)

lst2.extend(lst3)
print(lst2)


lst2.remove(98)
print(lst2)

lst2.pop(-2)
print(lst2)

# 不指定参数 删除最后一个
lst2.pop()
print(lst2)

newList=lst2[1:6]
print("原列表：",lst2)
print("切片后列表：",newList)

lst2[1:3]=[]
print(lst2)

lst=[10,20,30,40]
lst[2]=100
print(lst)

lst[1:3]=[300,400,500,600]
print(lst)

lst=[20,40,10,98,54]
lst.sort()
print(lst)
lst.sort(reverse=True)
print(lst)

lst=[10,20,30,40]
newList=sorted(lst,reverse=True)
print(newList)
print(lst)

lst=[i*i for i in range(1,10)]
print(lst)

lst=[i*2 for i in range(1,11)]
print(lst)

scores={'张三':100,'李四':98,'王五':45}
print(scores)
print(type(scores))

student=dict(name='jack',age=20)
print(student)

d={}
print(d)

print(scores['张三'])
print(scores.get('张三'))
print(scores.get('sd',88))
print('张三' in scores)

del scores['张三']
scores.clear()
scores['陈留']=100
print(scores)

keys=scores.keys()
print(keys)
print(list(keys))

values=scores.values()
print(values)
print(list(values))

items=scores.items()
print(items)
print(list(items))

for i in scores:
    print(i,scores[i],scores.get(i),scores[i])

d={'name':'张三','name':'李四'}
print(d)

items=['Fruits','Books','Others']
prices=[96,78,85]
d={i:p for i,p in zip(items,prices)}
print(d)

s='hello'
print(id(s))
s+='world'
print(id(s))

t='Ptyhon','world',98
print(t)
print(type(t))

t1=tuple(('python','world',98))
print(t1)

# 空列表
lst=[]
# 空字典
d={}
# 空元组
t=()

t=(10,[20,30],9)
print(t)
print(t[0],type(t[0]),id(t[0]))
print(t[1],type(t[1]),id(t[1]))
print(t[2],type(t[2]),id(t[2]))

for i in t:
    print(i)

s={2,3,4,5,5,6,7,7}
print(s)

s1=set(range(6))
print(s1)

s2=set([1,2,3,4,5,6,6])
print(s2)

s3=set((1,2,3,4,4,5,65,5))
print(s3,type(s3))


s={10,20,30,405,60}
print(10 in s)
print(100 in s)
s.add(50)
print(s)
s.update({200,400,300})
print(s)

# s.remove(100)
# s.remove(50)

s={10,20,30,40}
s2={30,40,20,10}
print(s==s2)
print(s!=s2)
print(s2.issubset(s1))
print(s3.issubset(s1))

lst=[i*i for i in range(6)]
print(lst)

s={i*i for i in range(6)}
print(s)

print([2**i for i in range(64)])