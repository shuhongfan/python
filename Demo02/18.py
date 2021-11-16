"""
@Time ： 2021/11/9 14:48
@Auth ： 021321752215舒洪凡
@File ：18.py
@IDE ：PyCharm
"""

from collections import Counter
from jieba import cut

def frequency(word):
    return Counter(cut(word))

word="为用户练习时输入的内容，要求用户输入的内容长度不能大于原始内容的长度，如果对应位置的字符一致则认为正确，否则判定输入错误。最后成绩为：正确的字符数量/原始字符串长度，按百分制输出，要求保留2 位小数。"
print(frequency(word))
