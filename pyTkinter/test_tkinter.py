import tkinter as tk
from tkinter import messagebox

win = tk.Tk()   #创建主窗口容器

win.title("测试win") #设置窗口名称

'''窗体几何大小'''
win.geometry("500x150")

'''下载事件'''
def dowload(*args):
	messagebox._show("提示","哈哈 你点对了")

'''   grid布局方式   '''

     ##创建lab标签
# tk.Label(win,text="配置",bg='Azure',font=("宋体",11)).grid(row=0) #默认column值为0，
# tk.Label(win,text="列表",bg='Azure',font=("宋体",11)).grid(row=0,column=1)

# e1 = tk.Entry(win)  # 类似于HTML的 input输入框
# e2 = tk.Entry(win)

# e1.grid(row=1)
# e2.grid(row=2)


'''用frame创建子容器'''
# frmLT = tk.Frame(width=500, height=320, bg='white')   #显示区
# frmLC = tk.Frame(width=500, height=150, bg='white')     #输入区
# frmRT = tk.Frame(width=200, height=500)               #右侧区
# frmLB = tk.Frame(width=500, height=30)                #按钮区

# '''利用padx，pady 可以将子容器边界区分开 在插件内部填充 类似HTML padding'''
# frmLT.grid(row=0, column=0,padx=1,pady=3)
# frmLC.grid(row=1, column=0,padx=1,pady=3)
# frmRT.grid(row=0, column=1,rowspan=3,padx=2,pady=3)
# frmLB.grid(row=2, column=0)

# tk.Button(frmLB,text="确定",command=dowloacd).grid(row=0,column=0)
# tk.Button(frmLB,text="取消").grid(row=0,column=1)
# tk.Label(frmRT,text="联系人",bg="green",font=("宋体",13)).grid(row=0,column=2)

tk.Label(win,text="视频下载",fg="red",font=("宋体",13)).grid(row=0,columnspan=2,padx=5,pady=8)

tk.Label(win,text="视频地址：",fg="green",font=("宋体",13)).grid(row=1,column=0)
videoAddr = tk.Entry(win,width=50) #创建地址输入框
videoAddr.grid(row=1,column=1)

tk.Label(win,text="保存地址：",fg="green",font=("宋体",13)).grid(row=2,pady=8)
saveAddr = tk.Entry(win,width=40) #创建地址输入框

saveAddr.grid(row=2,column=1,sticky=tk.W) #sticky可以选择的值有：N/S/W/E，分别代表上对齐/下对齐/左对齐/右对齐，

tk.Button(win,text="选择文件",fg="black").grid(row=2,column=1,sticky=tk.E)

tk.Button(win,text="下载",fg="black",width=8,).grid(row=3,column=1,pady=3,sticky=tk.S)

''' 进入消息循环'''
win.mainloop()  #显示窗口
