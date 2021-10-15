import random
x=[random.randint(1,100) for i in range(40)]
a=sorted(x[:20])
b=sorted(x[20:],reverse=True)
x=a+b
print(x)