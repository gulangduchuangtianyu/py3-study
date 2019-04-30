import os 
path = r"D:\py3-study-master\exercises\a"

dirList = []
fileList= []

for root, dirs, files in os.walk(path):
	
	if dirs :
		for d in dirs:
			dirList.append(d)
	if files :
		for f in files:
			fileList.append(f)
print(dirList,fileList)