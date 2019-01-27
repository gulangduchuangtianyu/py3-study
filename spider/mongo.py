import pymongo

class MongoDb:
	
	def __init__(self, port,addr,db,col):

		myclient   = pymongo.MongoClient('mongodb://'+addr+':'+port+'/')
		mydb       = myclient[db]
		self.mycol = mydb[col]

	def insert_one(self,dic):

		insert_res = self.mycol.insert_one(dic)

		return insert_res
	def insert_many(self,diclist):

		insert_resList = self.mycol.insert_many(diclist)

		return insert_resList

	def delete_one(self,deldic):

		del_res = self.mycol.delete_one(deldic)

		return del_res
	def delete_many(self,deldiclist):  #删除多个值，用正则匹配 用 for x in dic 删除多个指定的字段值
		del_resList = self.mycol.delete_many(deldiclist)

		return del_resList

	def update_one(self,convalue,newvaluse):
		update_res = self.mycol.update_one(convalue,newvaluse)

		return update_res
	def update_many(self,convalue,newvaluse): #更新多个值，用正则匹配 用 for x in dic 更新多个指定的字段值
		update_resList = self.mycol.update_many(convalue,newvaluse)

		return update_resList

	def find_one(self):
		res = self.mycol.find_one()
		return res

	def find_many(self,limit=None):
		dicList = []

		if limit is None :
			resList = self.mycol.find()
		else:
			resList = self.mycol.find().limit(limit)

		for x in resList:
			dicList.append(x)

		return dicList

	def find_field(self,fields):
		resList = self.mycol.find({},fields)
		dicList = []

		for x in resList:
			dicList.append(x)

		return dicList

	def find_by_field(self,dicfield):
		resList = self.mycol.find(dicfield)
		dicList = []

		for x in resList:
			dicList.append(x)

		return dicList

# m = MongoDb('27017','localhost','pybase','spiderTable')

# myclient = pymongo.MongoClient('mongodb://localhost:27017/')

# 	# dblist = myclient.list_database_names() #获取所有数据库名
# mydb     = myclient['pybase']
# 	# collist = mydb.list_collection_names() #获取指定数据库所有的集合
# mycol    = mydb['spiderTable']

# mydict = {"name": "FTMMANAGE","url": "https://www.ftm.com" }
 
# x = m.insert_one(mydict)

# print(x.inserted_id)


# mydict = {"name": "测试数据123334", "createtime": "20190124", "url": "https://www.runoob.com" }
# print(m.insert_one(mydict))

# mylist = [
#   { "_id": 1, "name": "RUNOOB", "cn_name": "菜鸟教程"},
#   { "_id": 2, "name": "Google", "address": "Google 搜索"},
#   { "_id": 3, "name": "Facebook", "address": "脸书"},
#   { "_id": 4, "name": "Taobao", "address": "淘宝"},
#   { "_id": 5, "name": "Zhihu", "address": "知乎"}
# ]
# print(m.insert_many(mylist))

# mydict = {"_id":2}
# print(m.delete_one(mydict))
# print(m.delete_many({}))
# old = {"_id":3}
# new ={ "$set":{"name": "update after"}}
# print(m.update_one(old,new))

# myquery = { "name": { "$regex": "^F" } } # 匹配所有name值以F开头的
# newvalues = { "$set": { "alexa": "123" } }
# print(m.update_many(myquery,newvalues))

# field = {'name':1,'cn_name':1}
# print(m.find_field(field))

# field = {'_id':10}
# print(m.find_by_field(field))
