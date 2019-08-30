import random
import urllib.request

url = "http://www.baidu.com"

'''
# 模拟请求头 （这是一种方法，下面使用另一种方法）
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3493.3 Safari/537.36"
}
# 设置一个请求体
req = urllib.request.Request(url, headers=headers)
# 发起请求
response = urllib.request.urlopen(req)
data = response.read()
print(data)
'''

agentsList = [
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60",
    "Opera/8.0 (Windows NT 5.1; U; en)",
    "Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.50",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 9.50",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0 "
]

agentStr = random.choice(agentsList)  # 这里是从列表中随机取出一个浏览器信息来改写请求头，避免被网站发现同一个地址快速持续的访问它而被封掉
req = urllib.request.Request(url)  # 里面添加头要写成键值对
# 向请求体里添加了User-Agent
req.add_header("User-Agent", agentStr)  # 这里添加时传入两个字符串，自动组合

response = urllib.request.urlopen(req)
print(response.read())