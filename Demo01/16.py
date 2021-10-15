name=[1,2,3,4]
sign=['a','b','c']
dict1=dict(zip(name,sign))
print(dict1)

tuple1=(1,2,3)
sign1=[1,2,3]
dict2={tuple1:sign1}
print(dict2)

dict3={1:100,2:200}
for item in dict3.items():
    print(item)

set1=['星期一','星期二','星期三']
print(set1)