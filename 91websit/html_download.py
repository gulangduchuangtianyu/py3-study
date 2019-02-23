import requests
from bs4 import BeautifulSoup
import json

start_url = "https://92.p04.space/video.php?category=rf"
params = {'session_language':'cn_CN'} # post请求提交的参数

def downLoadHtml():
	response = requests.post(start_url,data = params)
	html = response.text
	soup = BeautifulSoup(html,"html.parser")
	listchannel = soup.find("div",attrs={"id":"videobox"}).find_all('div',attrs={"class":"listchannel"})

	for i in listchannel :
		'''contents 获取子节点'''
		videoD = {}
		videoD['video_href'] = i.contents[1].find("a").get("href")
		videoD['video_tile'] = i.find("span").get_text().replace('...','')

		with open('video_info.text', mode='a+',encoding="utf-8") as f:

			f.write(json.dumps(videoD)+'\n')	

def readFileInfo():
	with open("video_info.text", "r") as f:
		data = f.read().splitlines()  # 去掉 \n
		return data

def requestVideoHref():
	listVideoHref = readFileInfo()
	for i in listVideoHref:
		videoPlayUrl = {}
		video_href = json.loads(i)['video_href']
		videoPlayUrl['video_tile'] = json.loads(i)['video_tile']

		videoPlayUrl['video_url'] = getVideoUrl(video_href)

		with open('video_play_url.text', mode='a+',encoding="utf-8") as f:

			f.write(json.dumps(videoPlayUrl)+'\n')

def getVideoUrl(url):
	response = requests.get(url)
	html = response.text
	soup = BeautifulSoup(html,"html.parser")
	if soup.find("source") is None :
		return '找不到视频播放连接'
	else :
		return soup.find("source").get('src')

if __name__ == '__main__':
	url = "https://92.p04.space/view_video.php?viewkey=5dd934ceb5f3bf5474bc&page=1&viewtype=basic&category=rf"
	requestVideoHref()