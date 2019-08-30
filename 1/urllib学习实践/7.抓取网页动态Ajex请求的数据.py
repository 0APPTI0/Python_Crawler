# 经常浏览一些网页会有这种情况，就是首先加载出一个页面的内容，向下滚动还有内容，在最下面会有一个提示下拉获取更多内容这类的东西。这个可以让加载网页的速度更快，毕竟内容少了嘛，再我们想要看到更多信息时候再加载。对于这样的一部分页面爬取其实也很简单，细心观察一下每次多加载一块的页面时，这时候上方的网址变化可以发现，有些是有数字变化的。可以根据里面的具体规律来修改每次请求的信息。


import urllib.request
import ssl
import json


def ajaxCrawler(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10"
    }
    req = urllib.request.Request(url, headers=headers)

    # 使用ssl创建未验证的上下文
    context = ssl._create_unverified_context()  # 访问的是HTTPS

    response = urllib.request.urlopen(req, context=context)
    jsonStr = response.read().decode("utf-8")
    print(type(response.read()))  # byte型
    print(type(response.read().decode("utf-8")))  # json字符串型
    jsonData = json.loads(jsonStr)
    return jsonData


# url = "https://movie.douban.com/j/chart/top_list?type=17&interval_id=100%3A90&action=&start=0&limit=20"
# info = ajaxCrawler(url)
# print(info)

for i in range(1, 11):
    url = "https://movie.douban.com/j/chart/top_list?type=17&interval_id=100%3A90&action=&start=" + \
        str(i * 20) + "&limit=20"
    info = ajaxCrawler(url)
    print(info)
    print(len(info))