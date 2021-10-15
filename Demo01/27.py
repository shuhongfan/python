class Animal:
    def __init__(self,color):
        self.color=color
    def call(self):
        return print('动物叫')

class Fish(Animal):
    def __init__(self,color):
        super().__init__(color)
        self.tail=True
    def call(self):
        print('%s 的鱼在吐泡泡'%self.color)

fish=Fish('绿色')
fish.call()
# print(fish.tail)