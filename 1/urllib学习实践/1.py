import urllib.request

# 向指定的url地址发送请求并返回服务器响应的数据（文件的对象）
response = urllib.request.urlopen("http://www.baidu.com")

# 读取文件的全部内容，会把读到的东西赋值给一个字符串变量
data = response.read()
print(data)  # 读取得到的数据
print(type(data))  # 查看数据类型

# 读取一行
data = response.readline()

# 读取文件的全部内容，赋值给一个列表变量，优先选择
data = response.readlines()
# print(data)
print(type(data))
# print(type(data.decode("utf-8")))  # 转字符串
print(len(data))

# 将爬取到的网页写入文件
with open(r"/Users/appti/Downloads/GitHub项目/Python_Crawler/1/webcontent/file1.html", "wb") as f:
    f.write(data)


# response 属性

# 返回当前环境的有关信息
print(response.info())

# 返回状态码
print(response.getcode())
# 200为正常，304位为有缓存

# 返回当前正在爬取的url地址
print(response.geturl())

url = "https://www.sogou.com/sgo?query=凯哥学堂&hdq=sogou-wsse-16bda725ae44af3b-0099&lxod=0_16_1_-1_0&lxea=2-1-D-9.0.0.2502-3-CN1307-0-0-2-E96F3D19F4C66A477CE71FD168DD223D-62&lxoq=kaigexuetang&lkx=0&ie=utf8"
url2 = r"https%3A//www.sogou.com/sgo%3Fquery%3D%E5%87%AF%E5%93%A5%E5%AD%A6%E5%A0%82%26hdq%3Dsogou-wsse-16bda725ae44af3b-0099%26lxod%3D0_16_1_-1_0%26lxea%3D2-1-D-9.0.0.2502-3-CN1307-0-0-2-E96F3D19F4C66A477CE71FD168DD223D-62%26lxoq%3Dkaigexuetang%26lkx%3D0%26ie%3Dutf8"

newurl = urllib.request.quote(url)  # 将含汉字的编码
print(newurl)
newurl2 = urllib.request.unquote(url2)  # 解码
print(newurl2)


# 端口号，http  80
# https  443