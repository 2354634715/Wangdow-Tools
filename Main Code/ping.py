import tkinter as tk
import ping3

window=tk.Tk()
window.iconphoto(True,tk.PhotoImage(file='icon.png'))
window.title("网络测试")
def ping():
    texta="    "
    
    back=ping3.ping("www.baidu.com",size=1024,timeout=1)
    
    if back == None:
        
        texta="网络不正常"
    else:
        
        texta="网络正常\n如有问题请配置DNS"
    lb2=tk.Label(window,text=texta)
    lb2.grid(column=0,row=2)


lb1=tk.Label(window,text="点击按钮测试网络")
lb1.grid(column=0,row=0)
bt1=tk.Button(window,text="测试网络",command=ping)
bt1.grid(column=0,row=1)

window.mainloop()