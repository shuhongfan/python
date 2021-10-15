dct = {"apple":6.0,"banana":7.5,"grape":12.0}

print("1）请循环遍历出所有的key和values；")
for key in dct:
    print(key,"---",dct[key])

print("2）请在字典中增加一个键值对,‘orange’:7.0，输出添加后的字典；")
dct["orange"]=7.0
print(dct)

print("(3）请删除字典中键值对‘apple’:6.0,并输出删除后的结果；")
dct.pop("apple")
print(dct)

print("(4）请删除字典中键'pineapple'对应的键值对，如果字典中不存在键‘pineapple’,则不报错，返回默认值None；")
print(dct.pop("pineapple",None))

print("（5）请获取字典中‘banana’对应的值，然后将其修改为6.5；")
dct["banana"]=6.5
print(dct)

print("(6）现有dct2 = {‘grape’:11,'tomato':3.5}，通过update操作使dct元素直接添加到dict2中，使dct2 = {banana':6.5,'grape':12.0,'tomato':3.5, ’orange':7.0}")
dct2 = {"grape":11,"tomato":3.5}
dct2.update(dct)
print("dct2",dct2)

print("（7）已有列表keys=[‘a’, ‘b’, ‘c’, ‘d’, ‘e’],values=[97,98,99,100,101]，快速生成字典d={‘a’:97, ’b’:98, ‘c’:99,’ d’:100, ’e’:101}")
keys=['a', 'b', 'c', 'd', 'e']
values=[97,98,99,100,101]
d=dict(zip(keys,values))
print("d=",d)

print("（8） 删除字典d")
del d
print(d)