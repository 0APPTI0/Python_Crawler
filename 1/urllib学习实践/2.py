# 直接将网页在爬取的同时写入文件

import urllib.request

urllib.request.urlretrieve("http://www.baidu.com",
                           filename=r"/Users/appti/Downloads/GitHub项目/Python_Crawler/1/webcontent/file2.html")

# urlretrieve在执行过程中，会产生一些缓存
# 清除缓存
urllib.request.urlcleanup()