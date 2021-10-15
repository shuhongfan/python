print("（1）创建一个列表lst[Jack,Rock,Jerry,Kehan,Peiqi,Blackbird]。")
lst=["Jack","Rock","Jerry","Kehan","Peiqi","Blackbird"]
print(lst)

print("（2）往lst列表里Blackbird前面插入一个Blue。")
lst.insert(lst.index("Blackbird"),"Blue")
print(lst)

print("（3）把lst列表中Kehan的名字改成中文“可汗”。")
lst[lst.index("Kehan")]="可汗"
print(lst)

print("（4）往lst列表中Rock后面插入一个子列表[“oldboy”,“oldgirl”]。")
lst.insert(lst.index("Rock"),["oldboy","oldgirl"])
print(lst)

print("（5）返回lst列表中Peiqi的索引值（下标）。")
print(lst.index("Peiqi"))

print("（6）取出lst列表中索引4-7的元素。")
subList= lst[4:7]
print(subList)

print("（7）	取出lst列表中索引2-10的元素，步长为2。")
subList2= lst[2:10:2]
print(subList2)

print("（8） 取出lst列表中最后3个元素。")
subList3 = lst[-3:]
print(subList3)

print("（9）使用del命令删除lst列表的第三个元素。")
del lst[2]
print(lst)

print("（10）请使用enumerate输出列表lst元素和序号（序号从 100 开始）")
for k,v in enumerate(lst,100):
    print(k,v)

print("（11）请将列表lst所有的元素按长度递减排序，并给出排序后的列表；")
lst.sort(key=lambda item:len(str(item)), reverse=True)
print(lst)

print("（12）创建新列表lst1[13,118,23,4,4,4,2,115,1113,4,4,13,13,19，2000]，合并到lst列表中。")
lst1 = [13,118,23,4,4,4,2,115,1113,4,4,13,13,19,2000]
lst.extend(lst1)
print(lst)

print("（13）删除lst1列表中重复元素4。")
n=lst1.count(4)
for i in range(0,n):
    lst1.remove(4)
print(lst1)

print("（14）输出列表lst1的总和和平均值。")
summ = sum(lst1)
lenth = len(lst1)
average = summ / lenth
print("总和：",summ)
print("平均值：",average)

print("（15）将列表lst1原地按升序排序后输出。")
print(sorted(lst1))

print("（16）输出列表lst1按字符串顺序的最小值。")
print(min(lst1))

print("（17）计算列表lst1长度并输出。")
print(len(lst1))

print("（18）将列表lst1逆序并输出（两种方式）.")
print(lst1[::-1])
lst1.reverse()
print(lst1)

print("（19）统计列表lst1中13出现的次数。")
print(lst1.count(13))

print("（20）列表lst1中重复元素去掉（多种方法，尽量不改变顺序）")
# import numpy as np;
# print(np.unique(lst1))
print("old=",lst1)
lst2=list(set(lst1))
lst2.sort(key=lst1.index)
lst1=lst2
print("new=",lst1)

print("（21）用列表推导式生成100以内的偶数列表x。")
print([i for i in range(100) if not(i%2==1)])

print("（22）把列表x转换为元组.")
print(tuple(lst1))
