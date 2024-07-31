

import tkinter as tk
import os

window=tk.Tk()
window.title("wangdow tools alpha0.1")

menubt=tk.Menu(window)
def mainface():
    lblmain.grid(column=0,row=0,columnspan=5)
    btn1.grid(column=0,row=1)
    btn2.grid(column=1,row=1)
    btn3.grid(column=2,row=1)
    btn4.grid(column=3,row=1)
    btn5.grid(column=4,row=1)
def wbping():
    os.system("ping.exe")
def cau():
    os.system("cau.exe")
def rd():
    os.system("rd.exe")
def sysin():
    os.system("winver")
def qk():
    os.system("qk.exe")

lblmain=tk.Label(window,text="欢迎使用wangdow tools！",font=("微软雅黑",24))
btn1=tk.Button(window,text="测试网络",command=wbping)
btn2=tk.Button(window,text="计算器",command=cau)
btn3=tk.Button(window,text="随机数",command=rd)
btn4=tk.Button(window,text="系统信息",command=sysin)
btn5=tk.Button(window,text="快捷工具",command=qk)
mainface()
menubt.add_command(label="主界面",command=mainface)
menubt.add_command(label="退出",command=window.quit)
window.config(menu=menubt)
window.mainloop()