# 021321752215舒洪凡
# 2021年10月26日15:14:06

num = input("请输入任意整数：")
while not num.isdigit():
    num = input("类型不合法请重新输入！！！请输入任意整数：")
num = int(num)
result = []

for i in range(2, num):
    flag = True
    for j in range(2, i):
        if i % j == 0:
            flag = False
            break
    if flag:
        result.append(i)

print(result)
