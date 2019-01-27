import urllib.request as urllib2
class HtmlDownloader:

	def downloader(self,url):
		if url is None :
			return

		page = urllib2.urlopen(url)
		code = page.getcode()  # 返回打开的网页的状态码
		if code !=200:
			return 
			
		return  page.read()    #读取网页内容即下载网页