from time import sleep
import random  #生成随机字符串
import os

#python3.*  urllib的引入用法
import urllib.request
from bs4 import BeautifulSoup

os.makedirs('./images/', exist_ok=True)
for n in range(60,67):   #爬取指定范围的文章ID

	#*******URL管理器*******#
	url = "http://www.liuzaichun.cn/index/index/articledetail.html?article_id="+ str(n) #转成字符串后拼接
	# url = "http://www.liuzaichun.cn/index/index/articledetail.html?article_id=64"

	#*******网页下载*******#
	page = urllib.request.urlopen(url)
	# code = page.getcode()  # 返回打开的网页的状态码

	html = page.read()  #读取网页内容即下载网页
	
	#**************常用的网页解析方式******************#

	#*******正则解析方式*******#
	# html = html.decode('utf-8')  #转utf-8编码
	# import re  # 正则
	# imgre = re.compile(r'src="(.+?)"')
	# head = re.findall(imgre,html)

	#*******beautifulsoup解析方式（第三方库更加便捷简单）*******#
	soup = BeautifulSoup(html,'html.parser')  # html.parser参数需要安装 HTMLParser 可以不用引入

	file = open('content.html', mode='a+',encoding="utf-8")  # 打开文件并设置utf8编码 否则会乱码

	#*******异常捕获（防止解析出来的html页面出现不存在需要找的DOM树节点）*******#
	try:

		#*******保存爬取的数据*******#

		title  = soup.find('div',attrs={"class":"article-title"}).find('h3').get_text()

		file.write('\r\n文章标题：'+title)

		content = soup.find('div',attrs={"class":"article-title"}).find_next_sibling().get_text()

		file.write('\r\n文章内容：'+content)

		imgUrl = soup.find('div',attrs={"class":"article-title"}).find_next_sibling().find_all('img')

		for img in imgUrl:
			imgN = ''.join(random.sample('zyxwvutsrqponmlkjihgfedcba',10)) #随机生成字符串
			
			urllib.request.urlretrieve('http://www.liuzaichun.cn/'+img.get('src'), './images/'+imgN+'.png')  #根据图片链接下载保存图片文件
	 
		file.close()

		print('爬取第'+str(n)+'篇文章成功')

			
	except :  # except 后面可以不写错误类型，写了错误类型，出现异常的错误必须要与之相同，否则还是会报错，不会执行 except 下面的语句

		print('未知错误')

sleep(2)  # 2秒执行一次

print('---------------所有文章爬取完成----------------')
