class Turtle:
    def __init__(self):
        print('这是一个初始化的方法')
        self.name='托尼'
    def __str__(self):
        return '这里是自定义对象变量的输出内容'

tony = Turtle()
print(tony)