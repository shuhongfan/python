def sum(list):
    total=0
    for i in range(len(list)):
        print(list[i],'+')
        total+=list[i]
    print('=',total)

list=[15,25,35,65]
sum(list)

a=100
def setNumber():
    a=10
    print(a)

setNumber()
print(a)