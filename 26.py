from datetime import datetime
class Medicine:
    name=''
    price=0
    PD=''
    Exp=''
    def __init__(self,name,price,PD,Exp):
        self.name=name
        self.price=price
        self.PD=PD
        self.Exp=Exp

    def get_name(self):
        return print(self.name)

    def get_GP(self):
        start=datetime.strptime(self.PD,'%Y-%m-%d')
        end=datetime.strptime(self.Exp,'%Y-%m-%d')
        return (end-start).days

med=Medicine(name='格列宁',price=25000,PD='2020-5-18',Exp='2022-5-18')
print(med.get_name())
print(med.get_GP())

