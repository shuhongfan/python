"""
@Time ： 2021/11/12 18:27
@Auth ： 021321752215舒洪凡
@File ：21.py
@IDE ：PyCharm
"""
import re

s="ha"
print("ha",2*s)

x='abcd'
y='abcde'

print([i==j for i,j in zip(x,y)])

print(list(str([1,2,3]))==[1,2,3])

x,y,z=map(str,range(3))
# print(x)
print(y)
# print(z)

print(sorted([13,1,237,89,100],key=lambda x:len(str(x))))

def demo(x,y,op):
    return eval(str(x)+op+str(y))
print(demo(3,5,'+'))

g=lambda x,y=3,z=5:x*y*z
print(g(1,2))

print(list(filter(lambda x:len(x)>3,['a','b','abcd'])))

print(list(map(lambda x:x+5,[1,2,3,4,5])))

def demo1(*p):
    return sum(p)
print(demo1(1,2,3,4))

d={'abc':1,'qwe':2,'zxc':3}
print(len(d))

print(list(map(str,[1,2,3])))

print(isinstance('abcdefg',str))

a='aAsmr3idd4bgs7Dlsf9eAF'
print([s for s in a if s.isdigit()])
print(''.join([s for s in a if s.isdigit()]))
print(''.join(re.findall(r'\d+',a)))
print(re.sub(r'\D','',a))

print('aaasdf'.lstrip('as'))
print('aaasdf'.lstrip('af'))
print('aaasdf'.strip('af'))
print('aaasdf'.rstrip('af'))