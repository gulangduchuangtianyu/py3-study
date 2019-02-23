import tkinter as tk
from tkinter import messagebox
import requests
win = tk.Tk()   #创建主窗口容器

win.title("测试win") #设置窗口名称

'''窗体几何大小'''
win.geometry("500x200")

'''下载事件'''
def startDownLoad(*args):
	videoV = videoAddr.get().strip()
	saveV = saveAddr.get().strip()
	r = requests.get(videoV, stream=True)
	totle = int(r.headers['content-length']) #下载的总内容大小
	csize = 0
	percent = 0
	if videoV =='':
		videoV = '视频地址不能为空'
		messagebox._show("提示",videoV)
		return
	elif saveV =='':
		saveV = '保存路径不能为空'
		messagebox._show("提示",saveV)
		return 
	with open('./videos/test.mp4', "wb") as mp4:
		for chunk in r.iter_content(chunk_size=1024): #每次获取视频字节大小
			if chunk:
				mp4.write(chunk)
			csize +=1024
			percent = round(csize / totle*100,2) #计算百分比，保留两位小数

			if csize==totle:
				print("下载进度：%s" %(str(100)+"%"),end="")
			else :
				print("下载进度：%s" %(str(percent)+"%"),end='\r')  #不换行实时刷新显示

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
saveAddr = tk.Entry(win,width=40,text='') #创建地址输入框

saveAddr.grid(row=2,column=1,sticky=tk.W) #sticky可以选择的值有：N/S/W/E，分别代表上对齐/下对齐/左对齐/右对齐，

tk.Button(win,text="选择文件",fg="black").grid(row=2,column=1,sticky=tk.E)
process = tk.Label(win,text="下载进度:",fg="red",font=("宋体",13)).grid(row=3,pady=8)
tk.Button(win,text="下载",fg="black",width=8,command=startDownLoad).grid(row=4,column=1,pady=3,sticky=tk.S)

''' 进入消息循环'''
win.mainloop()  #显示窗口
