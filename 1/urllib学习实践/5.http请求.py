# 有些网站还需要先登录之类的，也就是不仅仅从上面获取信息，还需要上传一些东西，下面介绍一下发送请求的两种方法。

'''
使用场景：进行客户端与服务端之间的消息传递时使用
GET: 通过url网址传递信息，可以直接在url网址上添加要传递的信息（不安全）
POST: 可以向服务器提交数据，是一种比较流行，安全的数据传递方式
PUT: 请求服务器存储一个资源，通常要指定存储的位置
DELETE: 请求服务器删除一个资源
HEAD: 请求获取对应的http报头信息
OPTIONS: 可以获取当前url所支持的请求类型
'''

'''
get请求：
特点：把数据拼接到请求路径后面传递给服务器
优点：速度快
缺点：承载的数据量小，不安全
'''

'''
post请求：
特点：把参数进行打包，单独传输
优点：数量大，安全（当对服务器数据进行修改时建议使用post）
缺点：速度慢
'''
import urllib.request
import urllib.parse  # 对请求打包的库

url = "http://www.baidu.com"
# 将要发送的数据合成一个字典
# 字典的键去网址里找，一般为input标签的name属性的值
data = {
    "username": "xiaoxiao",
    "passwd": "999"
}
# 对要发送的数据进行打包
postdata = urllib.parse.urlencode(data).encode("utf-8")

# 请求体
req = urllib.request.Request(url, data=postdata)

# 请求
response = urllib.request.urlopen(req)
print(response.read())