import pymysql
 
# 打开数据库连接
db = pymysql.connect("localhost","root","root","testdb" )
 
# 使用cursor()方法获取操作游标 
cursor = db.cursor()
 
# SQL 查询语句
sql = "SELECT COUNT(id) FROM student  WHERE score >=90"
 # 执行SQL语句
cursor.execute(sql)