# num=int(input("请输入数字："))
# while num>0:
#     print(num%10,end=" ")
#     num//=10

num1=input("请输入一个自然数：")
print(*(map(int,num1)))