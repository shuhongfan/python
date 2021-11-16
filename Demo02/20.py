"""
@Time ： 2021/11/9 16:16
@Auth ： 021321752215舒洪凡
@File ：20.py
@IDE ：PyCharm
"""

def Sum(v):
    s = 0
    for i in v:
        s+=i
    return s

def Max(v):
    max = v[0]
    for i in v:
        if i>max:
            max = i
    return max

def Min(v):
    min = v[0]
    for i in v:
        if i<min:
            min = i
    return min

def demo(*v):
    print(v)
    print('Sum=',Sum(v))
    print('Max=',Max(v))
    print('Min=',Min(v))

num = [1, 231, 9, 3, 78, 6, 25, 87, 69, 13]
demo(*num)