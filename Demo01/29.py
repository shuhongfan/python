class ClassMsg:
    def __init__(self,clsNum,clsName,clsTea,clslocal):
        self.clsNum=clsNum
        self.clsName=clsName
        self.clsTea=clsTea
        self.__clslocal=clslocal
    def showClsMsg(self):
        return print('课程编号：%d, 课程名称： %s ,任课老师： %s, 上课地点： %s'%
                     (self.clsNum,self.clsName,self.clsTea,self.__clslocal))

classinfo=ClassMsg(123,'计算机基础','张三','湖北武汉')
classinfo.showClsMsg()