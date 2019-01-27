import html_downloader,html_parser,url_manager
from time import sleep
class MainProgram:

	def start_grab(self, url):
		try:
			for n in range(60,70):
				get_url = url_manager.UrlManager().get_url(url,n)

				html    = html_downloader.HtmlDownloader().downloader(get_url)
				soup    = html_parser.HtmlParser().parser(html)
				save_data = html_parser.HtmlParser().save_data(soup,n)

				sleep(3) #3秒抓取一次
		except:
			print('未知错误')

if __name__ == '__main__':
	url = "http://www.liuzaichun.cn/index/index/articledetail.html?article_id="

	main = MainProgram().start_grab(url)