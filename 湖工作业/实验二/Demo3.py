# 导入random模块和string模块
import random
import string

# string.ascii_letters表示26个大小写字母
# string.digits表示10个阿拉伯数字
# string.punctuation表示标点字符
x = string.ascii_letters + string.digits + string.punctuation
# 使用列表推导式循环200次，每次从x里面随机取一个数
y = [random.choice(x) for i in range(200)]
# 使用join函数将取出的数据连接成字符串
z = "".join(y)
new_dict = dict()

# 重点：循环遍历将取出的字符作为key保存到字典，每个字符出现的次数作为value
# 这里要明白“字典.get(参数1，参数2)”所表达的是什么意思
# ->参数1表示:key值，
# ->参数2:如果指定键的值不存在时，返回该默认值(参数2)
for a in z:
    new_dict[a] = new_dict.get(a, 0) + 1
print(new_dict)