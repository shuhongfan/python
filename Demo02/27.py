"""
@Time ： 2021/11/16 19:01
@Auth ： 021321752215舒洪凡
@File ：27.py
@IDE ：PyCharm
"""

import re
test='alpha. beta....gamma delta'
print(re.split('[\.]+',test))
print(re.split('[\.]+',test,maxsplit=1))
