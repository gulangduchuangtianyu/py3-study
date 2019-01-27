#爬取的url管理器
class UrlManager:

	def __init__(self):
		# self.url = url
		pass

	# num :文章ID
	def get_url(self,url,num):
		if url is None:
			return

		return url+str(num)
