# 021321752215舒洪凡
# 2021年10月26日16:06:52

firstWeekMoney=input("请输入第一周存入的金额：")
while not firstWeekMoney.isdigit():
    firstWeekMoney = input("请输入数字！！！请输入第一周存入的金额：")
firstWeekMoney=int(firstWeekMoney)

weekGAPMoney=input("请输入每周递增的金额：")
while not weekGAPMoney.isdigit():
    weekGAPMoney=input("请输入数字！！！请输入每周递增的金额：")
weekGAPMoney=int(weekGAPMoney)

weeks=input("请输入总周数：")
while not weeks.isdigit():
    weeks=input("请输入数字！！！请输入总周数：")
weeks=int(weeks)
TotalMoney=0

for i in range(1,weeks+1):
    if i != 1:
        firstWeekMoney+=weekGAPMoney
    TotalMoney += firstWeekMoney
    print("第",i,'周，存入金额：',firstWeekMoney,"总金额：",TotalMoney)

print("TotalMoney=",TotalMoney)