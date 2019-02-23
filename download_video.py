import requests
import os,sys
import random  #生成随机字符串
import re 
# print(requests)
print("开始下载")
url = 'http://198.255.82.90//mp43/304122.mp4?st=AeKa-qtzqgYe143fQYFa3w&e=1550975560'

'''
   request = requests.get('http://www.baidu.com')
print('type(request)', type(request))  #响应类型
print('request.status_code', request.status_code) #状态码
print('request.encoding', request.encoding)  #字符集编码
print('request.cookies', request.cookies)   #cookie信息
print('request.text', request.text)         # 获取HTML内容

'''
r = requests.get(url, stream=True)
totle = int(r.headers['content-length']) #下载的总内容大小
csize = 0
percent = 0
pattern = re.compile(r'[:|.|/]')
random_str    = re.sub(pattern,'',url) #正则替换
video_name = ''.join(random.sample(random_str,10))+".mp4"
with open('./videos/'+video_name, "wb") as mp4:
    for chunk in r.iter_content(chunk_size=1024): #每次获取视频字节大小
    	
        if chunk:
            mp4.write(chunk)
        csize +=1024
        percent = round(csize / totle*100,2) #计算百分比，保留两位小数

        if csize==totle:
        	print("下载进度：%s" %(str(100)+"%"),end="")
        else :
        	print("下载进度：%s" %(str(percent)+"%"),end='\r')  #不换行实时刷新显示

