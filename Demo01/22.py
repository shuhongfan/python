class Turtle:
    color='绿色'
    weight=10
    def eat(self):
        print('海归吃啥...')
    def run(self):
        print('我要一步一步往上爬...')

abc=Turtle()
abc.eat()
python1=Turtle()
python1.run()


class Ball:
    def setName(self,name):
        self.name=name
    def kick(self):
        print('我叫%s，哈哈哈'%self.name)

a=Ball()
a.setName('球A')
a.kick()