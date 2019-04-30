#des:输入一串数字并且排序
number = input('请输入一串数字：') 
print(number)  #number字符串将其转换成列表，如下所示：
print(list(number)) 

number_list = list(map(int,list(number)))  #map采用map函数，将字符串列表中的每一个字符转换成数字。
number_list.sort() 

for item in number_list:
	print(item,end=" ")



	
