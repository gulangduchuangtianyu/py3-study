import requests
import os,sys
# print(requests)
print("开始下载")
url = 'https://pic.ibaotu.com/00/51/34/88a888piCbRB.mp4'

r = requests.get(url, stream=True)
totle = int(r.headers['content-length']) #下载的总内容大小
csize = 0
percent = 0
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

