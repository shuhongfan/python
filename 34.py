# 定义一个学生类，
# 该类的属性有：
# 姓名（name）、年龄（age）、成绩（scores）
# （语文，数学，英语)[每课成绩的类型为整数]，
# 类的方法有：
# 1）、 获取学生的姓名：get_name( )，返回类型:str
# 2）、获取学生的年龄：get_age( )，返回类型:int
# 3）、返回3门科目中最高的分数：get_course ( )，返回类型:int
# 定义完类以后，可生成如下的对象进行测试:

# 网络18304 舒洪凡 1801305764
# 定义一个学生类
class Student():
    # 初始化name, age, scores
    def __init__(self, name, age, scores):
        self.name = name
        self.age = age
        self.scores = scores
    # 定义学生类方法 get_name 获得姓名 并返回 返回类型:str
    def get_name(self):
        return self.name
    # 定义学生类方法 get_age 获得年龄 并返回 返回类型:int
    def get_age(self):
        return self.age
    # 定义学生类方法 get_course 获得3门科目中最高的分数 并返回 返回类型:int
    def get_course(self):
        return max(self.scores)

# 创建Student类 对象 并传入初始值
shf = Student('舒洪凡', 20, [60, 70, 55])

# 调用get_name方法 并用name接收返回值
name = shf.get_name()
# 打印name的返回值 并输出类型
print('学生的姓名:', name, type(name))

# 调用get_age方法 并用age接收返回值
age = shf.get_age()
# 打印age的返回值 并输出类型
print('学生的年龄:', age, type(age))

# 调用get_course方法 并用age接收返回值
course = shf.get_course()
# 打印course的返回值 并输出类型
print('3门科目中最高的分数:', course, type(course))