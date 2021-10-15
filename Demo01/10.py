i=0
for num1 in range(1,5):
    for num2 in range(1,5):
        for num3 in range(1,5):
            if num1 != num2 and num2 != num3 and num1 != num3:
                num = 100*num1+num2*10+num3
                print(num)
                i=i+1

print(i)