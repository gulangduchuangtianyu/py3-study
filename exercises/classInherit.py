class Person:
	"""docstring for Person"""
	name = ''
	age  = ''
	def __init__(self, msg,name,age):
		self.name = name
		self.age  = age
		self.msg  = msg

	def talk(self):
	 	print(self.msg) 


class Chinese(Person):
	"""docstring for ClassName"""
	def __init__(self,msg,name,age):
		Person.__init__(self, msg,name,age)

ch = Chinese("老子是中国人",'Chinese',22)
ch.talk()

class American(Person):
	"""docstring for ClassName"""
	def __init__(self,msg,name,age):
		Person.__init__(self, msg,name,age)

am = American("American is dog",'American',22)
am.talk()
