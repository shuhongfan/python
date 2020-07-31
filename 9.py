for i in range(10):
    print('*'*(i+1))

for j in range(10):
    print(' '*(10-j),end='')
    print('*'*(j+1),end='')
    print('*'*j)

for k in range(5):
    print(' ' * (5 - k), end='')
    print('*' * (k + 1), end='')
    print('*' * k)
for k in range(5):
    print(' ' * (k+1), end='')
    print('*' * (5-k-1),end='')
    print('*' * (5-k))
