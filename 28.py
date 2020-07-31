class Student:
    def __init__(self,name,age,YWgrade,SXgrade,YYgrade):
        self.name=name
        self.age=age
        self.YWgrade=YWgrade
        self.SXgrade=SXgrade
        self.YYgrade=YYgrade
    def getName(self):
        return print(self.name)
    def getAge(self):
        return print(self.age)
    def MaxGrade(self):
        return print(max(self.SXgrade,self.YWgrade,self.YYgrade))

student=Student('小米',19,99,55,66)
student.getName()
student.getAge()
student.MaxGrade()

print('*'*20)

class Student1:
    def __init__(self,name,age,scores):
        self.name=name
        self.age=age
        self.scores=scores
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def get_course(self):
        return max(self.scores)

stu1=Student1('毛毛姐', 20 ,[56,80,44])
print('姓名:%s'%(stu1.get_name()))
print('年龄:%s'%(stu1.get_age()))
print('语文数学英语三门课中最高分是:%s'%(stu1.get_course()))