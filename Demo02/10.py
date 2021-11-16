"""
@Time ： 2021/11/2 14:48
@Auth ： 021321752215舒洪凡
@File ：10.py
@IDE ：PyCharm
"""

def sum(*nums):
    s=0
    for i in nums:
        s = i + s
    return s

num = [1, 231, 9, 3, 78, 6, 25, 87, 69, 13]
sumResult = sum(*num)
maxResult = max(num)
minResult = min(num)

print("sumResult=",sumResult)
print("maxResult=",maxResult)
print("minResult=",minResult)
