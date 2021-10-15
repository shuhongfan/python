class Person:
    def __init__(self,color='黑色'):
        self.color=color
    def call(self):
        print('***汪汪汪***')

class Dog(Person):
    pass

dog=Dog('白色')
print(dog.color)
dog.call()