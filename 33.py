# 海滩上有一堆桃子，五只猴子来分。
# 第一只猴子把这堆桃子平均分为五份，多了一个，这只猴子把多的一个扔入海中，拿走了一份。
# 第二只猴子把剩下的桃子又平均分成五份，又多了一个，它同样把多的一个扔入海中，拿走了一份，
# 第三、第四、第五只猴子都是这样做的，问海滩上原来最少有多少个桃子？


# 网络18304 舒洪凡 1801305764
# 控制循环次数 第五只到第一只
i = 0
# 最后一个猴子拿走的桃子个数
j = 1
# 剩余桃子个数
x = 0

while (i < 5):
    # 第五只猴子拿走后海滩剩下桃子的个数
    x = 4 * j
    for i in range(0, 5):
        if(x % 4 != 0):
            break
        else:
            i += 1
        # 上一只猴拿走后海滩剩下桃的个数
        x = x / 4 * 5 + 1
    j += 1
# 输出原来最少桃子个数
print('原来最少桃子个数:', x)
