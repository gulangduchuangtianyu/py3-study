import sys
sys.path.append('../')  # 引入目录上层的块 才能引入a.py模块
import a

import pg.pb_module # 把目录做成一个包来引用  也可以这样引入 from ba import c

c = {'xing':'wagnli','niece':'2345'}
a.aValue()
# print(sys.path)  // 主程序以及引入模块所在路径列表
pg.pb_module.pbModule()