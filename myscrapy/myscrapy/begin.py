from scrapy import cmdline

cmdline.execute(("scrapy crawl testspider --nolog").split())  #--nolog不输出日志信息