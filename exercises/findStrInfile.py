import os 
path = r"D:\py3-study-master\exercises\username.txt"

with open(path,"r+") as f :
	index = 0
	lines = f.readlines()  #读取文件所有行的数据 返回一个list
	for line in lines:
		if line.find("10002") >=0 :
			lines[index]= "dengzh,10002\n"
			f.seek(0) # 使文件指针移动到开头
			f.truncate() #清空文件，指针必须指向文件开头
			f.writelines( lines )
		index+=1