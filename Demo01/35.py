# 随机生成0~100之间20个整数的列表，
# 然后将前10个元素升序排列，后10个元素降序排列，并输出结果


# 网络18304 舒洪凡 1801305764
# 导入 random 模块
import random
# 新建list数组和2个临时过渡数组
list = []
temp1 = []
temp2 = []

# for循环20次
for i in range(20):
    # 使用random 模块 随机生成 0-100整数
    num = random.randint(0, 100)
    # 插入到list数组中
    list.append(num)
# 打印随机整数列表
print('随机整数列表为：', list, len(list))

# 获取前10个数字放到temp1中
temp1 = list[0:10]
# 获取后10个数字放到temp2中
temp2 = list[10:20]

# 前10个（temp1）升序排序
temp1.sort()

# 后10个(temp2)降序排序 先升序数组 然后翻转数组 从而形成降序
temp2.sort()
temp2.reverse()

# 列表合并
# 把temp1和temp2拼接在一起 生成新的list数组
list = temp1 + temp2

# 打印排序后的列表list
print('排序后的列表为：', list, len(list))