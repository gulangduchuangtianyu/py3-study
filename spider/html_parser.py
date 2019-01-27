import random  #生成随机字符串
import os

#python3.*  urllib的引入用法
import urllib.request as urllib2
from bs4 import BeautifulSoup
import mongo

os.makedirs('./images/', exist_ok=True) #创建文件夹

class HtmlParser:
	def __init__(self):

		self.mongo = mongo.MongoDb('27017','localhost','pybase','spiderTable')

	def parser(self,html):
		if html is None :
			return
		soup = BeautifulSoup(html, "html.parser")  # html.parser参数需要安装 HTMLParser 可以不用引入

		return soup

	def save_data(self,soup,articel_num):
		
		# file = open('content.html', mode='a+',encoding="utf-8")  # 打开文件并设置utf8编码 否则会乱码

		title  = soup.find('div',attrs={"class":"article-title"}).find('h3').get_text()

		# file.write('\r\n文章标题：'+title)


		content = soup.find('div',attrs={"class":"article-title"}).find_next_sibling().get_text()

		# file.write('\r\n文章内容：'+content)

		imgUrl = soup.find('div',attrs={"class":"article-title"}).find_next_sibling().find_all('img')

		
		imgDict = ''
		for img in imgUrl:
			imgN = ''.join(random.sample('zyxwvutsrqponmlkjihgfedcba',10)) #随机生成字符串
			imgDict = imgDict+imgN+'.png'
			urllib2.urlretrieve('http://www.liuzaichun.cn/'+img.get('src'), './images/'+imgN+'.png')  #根据图片链接下载保存图片文件

		# print(imgDict);
		self.mongo.insert_one({"title":title,"content":content,"img_list":imgDict})
	 
		# file.close()

		print('第'+str(articel_num)+'篇文章抓取完成')

	
		