"""
@Time ： 2021/11/23 14:23
@Auth ： 021321752215舒洪凡
@File ：28.py
@IDE ：PyCharm
"""

import tkinter
import tkinter.messagebox

filename = r"D:\Develop\upload\users.txt"

# 创建应用程序窗口
root = tkinter.Tk()
root.title("请登录")
# 定义窗口大小
root['height'] = 100
root['width'] = 250

# 在窗口上创建标签组件
labelName = tkinter.Label(root, text='用户名:', justify=tkinter.RIGHT, anchor='e', width=80)
labelName.place(x=10, y=5, width=80, height=20)
varName = tkinter.StringVar(root, value='')
entryName = tkinter.Entry(root, width=80, textvariable=varName)
entryName.place(x=100, y=5, width=80, height=20)

# 创建密码文本框
labelPwd = tkinter.Label(root, text='密码:', justify=tkinter.RIGHT, anchor='e', width=80)
labelPwd.place(x=10, y=30, width=80, height=20)
varPwd = tkinter.StringVar(root, value='')
entryPwd = tkinter.Entry(root, show='*', width=80, textvariable=varPwd)
entryPwd.place(x=100, y=30, width=80, height=20)


# 登录按钮事件处理函数
def login():
    # 获取用户名和密码
    name = entryName.get()
    pwd = entryPwd.get()
    try:
        with open(filename,'r', encoding='utf-8') as fp:
            flag = 0
            while True:
                line = fp.readline()
                if not line:
                    break
                n, p = line.strip().split(':')
                if name == n and pwd == p:
                    tkinter.messagebox.showinfo(title='恭喜', message='登录成功！')
                    flag = 1
                    break
            if flag == 0:
                tkinter.messagebox.showerror(title='警告', message='用户名或密码错误')
    except:
        print('文件无法打开')


# 创建按钮组件，同时设置按钮事件处理函数
buttonOk = tkinter.Button(root, text='登录', command=login)

# 设置按钮的单击事件处理函数
buttonOk.place(x=100, y=60, width=50, height=20)

# 启动消息循环
root.mainloop()
