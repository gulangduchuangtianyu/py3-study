# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import mongo,os,csv

#爬虫字段数据信息保存的类
class MyscrapyPipeline(object):
	def __init__(self):

		self.mongo = mongo.MongoDb('27017','localhost','pybase','spiderTable')

		# csv 文件
		# store_file = os.path.dirname(__file__)+"/content.csv"

		# self.file = open(store_file,"a+",newline='',encoding="utf-8")

		# self.writer = csv.writer(self.file)

	def process_item(self, item, spider):
		'''存为csv文件'''
		# try:
		# 	self.writer.writerow((
		# 		item["article_tile"],
		# 		item["article_content"],
				
		# 	))
		# except:

		# 	print('unerror!!!')



		# return item
		# print(item)
		self.mongo.insert_one(dict(item))
