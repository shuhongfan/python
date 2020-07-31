def triangle(a,b,c):
    if(a+b>c) and (a+c>b) and (b+c>a):
        return '这三条边能构建一个三角形'
    else:
        return '这三条边不能构建一个三角形'

result=triangle(1,2,3)
print(result)

result=triangle(3,4,5)
print(result)