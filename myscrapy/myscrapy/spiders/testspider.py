# -*- coding: utf-8 -*-
import scrapy,sys
from myscrapy.items import MyscrapyItem

class TestspiderSpider(scrapy.Spider):
    name = 'testspider'
    allowed_domains = ['www.liuzaichun.cn']
    start_urls = ['http://www.liuzaichun.cn']
    

    ### 爬虫数据抓取的核心部分
    def parse(self, response):
    	# file = open('../content.text', mode='a+',encoding="utf-8")  # 打开文件并设置utf8编码 否则会乱码
        
    	'''可以用.css选择器选择'''
    	# title= response.css('h3::text').extract() 


    	'''.xpath选择器'''

    	'''      从根（ 根为'/'，）节点下开始匹配单个标签'''
    	# title= response.xpath('/html/head/title/text()').extract() 

    	'''     '//'从下载的网页dom中找到所有匹配的元素，不管在任何位置  但是 ".//" 是从当前标签下找到所有的匹配标签  '''
    	# title= response.xpath("//div[@class='m-portlet__body']/div[1]/h3/text()").extract()[0]  # /text()获取某个标签的文本

    	# content = response.xpath("//div[@class='m-portlet__body']/div[2]//text()").extract() # //text()获取某个标签以及它的所有子标签的文本

    	# 定义爬虫字段信息的类
    	fields = MyscrapyItem()

    	# 将获取的数据交给pipelines，pipelines在settings.py中需要开启 ITEM_PIPELINES
    	# yield fields   #使用yield返回数据，不要使用return。这样子parse就会被当做一个生成器。scarpy将parse生成的数据，逐一返回
    	lis = response.xpath("//div[@class='m-portlet__body']/div[1]//div[@class='ibox-content']")
    	for it in lis:
    		fields['article_tile']   = it.xpath("./h4/a/text()").extract()[0]
    		
    		fields['article_intro']  = ''.join(it.xpath("./div[1]/p/text()").extract()[0].split())

    		t = ''.join(it.xpath("./div[2]/div[1]//text()").extract())

    		fields['article_createtime']  = ''.join(t).split()[0]
    		
    		yield fields

    	next_url = response.css('li.next_page')
    	
    	for  p in range(2,5):
    		next_url = "http://www.liuzaichun.cn/?p="+str(p)

    		yield scrapy.Request(next_url , callback=self.parse)

    	# print(next_url)
    		
