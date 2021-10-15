# 创建一个普通列表
movies=['花木兰','我和我的祖国','致命女人']
print(movies)
# 创建一个混合列表
mix_list=[1,2,3,'无耻之徒',[1,2,3,4]]
print(mix_list)
# 空列表
empty=[]
print(empty)


# 访问列表中的元素
print(movies[0])
# 访问列表中多个值 切片
print(movies[:])
print(movies[0:2])

# 列表添加新元素
movies.append('越狱')
print(movies)
# 添加多个
movies.extend([1,2,3,58])
print(movies)
# 指定位置 添加元素
movies.insert(0,'破产姐妹')
print(movies)

movies.insert(1,'权利与游戏')
print(movies)


# 删除列表中的元素
movies.remove(1)
print(movies)

movies.pop()
print(movies)

movies.pop(2)
print(movies)

del movies[3]
print(movies)
# 删除整个列表
del movies
# print(movies)


name='xiaoming'
print(list(name))
list=[1,2,3,4,5,6]
print(list)
# print(list(name))

# 列表的操作符
# 比较操作符
list1=[1]
list2=[2]
print(list1>list2)
print(list1<list2)

list3=[1,2]
list4=[2,1]
print(list3>list4)
print(list3<list4)

# 重复操作符
list5=[1,2,3]
print(list5*3)
print(list5)

# 成员关系操作符
list6=[1,2,3]
print(1 in list6)
print(33 in list6)
print(33 not in list6)

list7=[1,2,3,['北京','武汉']]
print(1 in list7)
print('北京' in list7)
print('北京' in list7[3])

list1=[9,8,7,6,5,4,3,2,1]
list2=list1
print(list2)
list3=list1[:2]
print(list3)
list1.sort()
print(list1)
print(list2)
print(list3)
list1.reverse()
print(list1)
list1.sort(reverse=True)
print(list1)

tuple=(1,2,3,4)
print(type(tuple))
print(tuple)

tuple2=1,2,3,4,5
print(tuple2)

tuple3=()
print(tuple3)

tuple4=(1,)
print(tuple4)

tuple5=1,
print(tuple5)