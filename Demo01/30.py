import math
class Circle:
    def __init__(self,tup,radius,color):
        self.tup=tup
        self.radius=radius
        self.color=color
    def perimeter(self):
        return print('周长:',math.pi*2*self.radius)
    def area(self):
        return print('面积:',math.pi*pow(self.radius,2))

circle=Circle((0,0),5,'黑色')
circle.perimeter()
circle.area()