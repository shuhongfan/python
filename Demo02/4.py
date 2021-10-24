a1=34
a2=str(34)
print(a1+eval(a2))
print(40-3**2+11//3**2*8)
print('{0},{1}'.format('carmen',20))

x=6
y=5
max=y if x>y else x
print(max)

if True:
    pass

dict3={(1,2,3):"users"}
print(dict3)
for key in dict3:
    print(key,dict3[key])

print(i**2 for i in range(10))
print([1,3]*3)
x=list(range(10))
print(x[:5])

x=2
x='abc'
print(x)
print(1,2,9,sep=":")
x=99999**999999
print(x)