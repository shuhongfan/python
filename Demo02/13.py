"""
@Time ： 2021/11/2 15:23
@Auth ： 021321752215舒洪凡
@File ：13.py
@IDE ：PyCharm
"""

words_dic = {}
word="hello world nihao world hey hello java world hi python yeoman word".split(" ")
for k in word:
    if k in words_dic:
        words_dic[k] += 1
    else:
        words_dic[k] = 1

print(words_dic)
