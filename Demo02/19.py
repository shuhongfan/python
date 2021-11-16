"""
@Time ： 2021/11/9 15:59
@Auth ： 021321752215舒洪凡
@File ：19.py
@IDE ：PyCharm
"""

import re
x = 'This is is a red cheese. Hello Hello world!'
print("oldStr="+x)
pattern = re.compile(r'\b(\w+)(\s+\1){1,}\b')
matchResult = pattern.search(x)
x = pattern.sub(matchResult.group(1),x)
print("newStr="+x)

