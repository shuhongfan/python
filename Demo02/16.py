"""
@Time ： 2021/11/2 16:05
@Auth ： 021321752215舒洪凡
@File ：16.py
@IDE ：PyCharm
"""
import string

def checkPWD(password):
    dig = 0
    lCase = 0
    hCase = 0
    punnctuation = 0

    if len(password) <= 8:
        return ("密码强度弱")
    else:
        for ch in password:
            if ch in string.digits:
                dig = 1
            elif ch in string.ascii_lowercase:
                lCase = 1
            elif ch in string.ascii_uppercase:
                hCase = 1
            elif ch in string.punctuation:
                punnctuation = 1
        if dig + lCase + hCase + punnctuation == 2:
            return("密码强度中")
        elif dig + lCase + hCase + punnctuation == 3:
            return("密码强度强")
        elif dig + lCase + hCase + punnctuation == 4:
            return("密码强度极强")
        else:
            return(str(dig) + str(lCase) + str(hCase) + str(punnctuation))



password = input("请输入密码：")
msg = checkPWD(password)
print(msg)
