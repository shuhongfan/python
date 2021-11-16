"""
@Time ： 2021/11/2 15:29
@Auth ： 021321752215舒洪凡
@File ：14.py
@IDE ：PyCharm
"""

x = 'This is is a red cheese. Hello Hello world!'
def unique_list(l):
    ulist = []
    [ulist.append(x) for x in l if x not in ulist]
    return ulist
y=' '.join(unique_list(x.split()))
print("oldStr="+x)
print("newStr="+y)

