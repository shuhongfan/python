# 021321752215舒洪凡
# 2021年10月26日15:06:38

str=input("请输入一个字符串：")
Big_Num=0
Small_Num = 0
Space = 0
Number = 0
Other = 0

for n in str:
    if n.isupper():
        Big_Num += 1
    elif n.islower():
        Small_Num += 1
    elif n.isspace():
        Space += 1
    elif n.isdigit():
        Number += 1
    else:
        Other += 1

print("大写字母：",Big_Num,",小写字母：",Small_Num,",空格：",Space,",数字：",Number,",其他：",Other)
