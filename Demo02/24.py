"""
@Time ： 2021/11/16 15:18
@Auth ： 021321752215舒洪凡
@File ：24.py
@IDE ：PyCharm
"""

class MyArray:
    def __init__(self,x,y,z):
        self.__x = x
        self.__y = y
        self.__z = z
    def add(self,a):
        x = self.__x + a.__x
        y = self.__y + a.__y
        z = self.__z + a.__z
        print("add=({},{},{})".format(x,y,z))
    def sub(self,a):
        x = self.__x - a.__x
        y = self.__y - a.__y
        z = self.__z - a.__z
        print("sub=({},{},{})".format(x, y, z))
    def mul(self,a):
        x = self.__x * a
        y = self.__y * a
        z = self.__z * a
        print("mul=({},{},{})".format(x, y, z))
    def div(self,a):
        x = self.__x / a
        y = self.__y / a
        z = self.__z / a
        print("div=({},{},{})".format(x, y, z))
    def length(self):
        a = pow(pow(self.__x, 2) + pow(self.__y, 2) + pow(self.__z, 2), 0.5)
        print("长度为：{}".format(round(a, 3)))

print('请输入6个数a,b,c,d,e,f:')
a,b,c,d,e,f=map(int,input().split())
print('N1:',(a,b,c))
print('N2:',(d,e,f))
n1=MyArray(a,b,c)
n2=MyArray(d,e,f)

n1.add(n2)
n1.sub(n2)
n1.mul(2)
n1.div(2)
n1.length()
