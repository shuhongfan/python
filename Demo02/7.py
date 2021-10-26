# 021321752215舒洪凡
# 2021年10月26日15:26:17

# 这段代码试图计算组合数Cni ，但是由于浮点数除法时精度问题导致结果错误。
def cni(n,i):
    minNI = min(i, n-i)
    result = 1
    for j in range(0, minNI):
        result = result * (n-j) // (minNI-j)
    return result
print(cni(5,2))


def NEWcni(n, i):
    minNI = min(i, n - i)
    result = 1
    for j in range(1, minNI + 1):
        print('(', result, '*', n - minNI + j, ')/', j)  # 从最小项开始累乘
        result = (result * (n - minNI + j)) / j  # 为了保证能够整除，先进行乘法后除
    return result
print("改正后：",NEWcni(5, 2))
