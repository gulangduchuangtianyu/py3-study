import os 

local = r"D:\py3-study-master\exercises\a"
copyLocal = r"D:\py3-study-master\exercises\copya"

#文件夹/文件复制
# items =os.listdir(local)  # 遍历目录下所有文件名或文件夹名 返回一个list
# for path in items:
#     item = os.path.join(local,path)
#     if os.path.isdir(item):
#     	targetDir = os.path.join(copyLocal,path)
#     	if not os.path.exists(targetDir) :
#     		os.makedirs(targetDir)

#     elif os.path.isfile(item):
#     	targetFile = os.path.join(copyLocal,path)
        
#     	with open(targetFile, "wb") as t:  #打开文件，操作完自动关闭文件
#     		i = open(item, "rb")
#     		t.write(i.read())
#     		i.close()
    	

#文件重命名

origin   = r"D:\py3-study-master\exercises\a\son.txt"
old_name = r"D:\py3-study-master\exercises\copya\son.txt"
new_name = r"D:\py3-study-master\exercises\copya\first_son.txt"

t = open(old_name, "wb")
i = open(origin, "rb")
t.write(i.read())
i.close()
t.close()
os.rename(old_name,new_name)
