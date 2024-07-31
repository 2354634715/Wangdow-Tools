import tkinter as tk
import os

def con():
    os.system("control")
def hx():
    os.system("msinfo32")
def cmd():
    os.system("cmd")
def reg():
    os.system("regedt32")
def tgr():
    os.system("taskmgr")
def exp():
    os.system("explorer")
window=tk.Tk()

window.iconphoto(True,tk.PhotoImage(file='icon.png'))
window.title("系统工具快捷启动")
lbl1=tk.Label(window,text="点击按钮以快捷启动各种系统工具").grid(column=0,row=0,columnspan=6)
btn1=tk.Button(window,text="控制面板",command=con).grid(column=0,row=1)
btn2=tk.Button(window,text="电脑硬件信息",command=hx).grid(column=1,row=1)
btn3=tk.Button(window,text="cmd(无效)",command=cmd).grid(column=2,row=1)
btn4=tk.Button(window,text="注册表编辑器（reg）",command=reg).grid(column=3,row=1)
btn5=tk.Button(window,text="任务管理器",command=tgr).grid(column=4,row=1)
btn6=tk.Button(window,text="文件",command=exp).grid(column=5,row=1)
window.mainloop()