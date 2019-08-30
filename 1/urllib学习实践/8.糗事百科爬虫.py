import urllib.request
import re

# https://www.qiushibaike.com/text/page/2/


def jokeCrawler(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10"
    }
    req = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(req)

    html = response.read().decode("utf-8")
    # print(type(html))

    pat = r'<div class="author clearfix">(.*?)<span class="stats-vote"><i class="number">'
    re_joke = re.compile(pat, re.S)  # re.S 使可以匹配换行
    divsList = re_joke.findall(html)
    # print(divsList)
    # print(len(divsList))

    dic = {}
    for div in divsList:
        # 用户名
        re_u = re.compile(r"<h2>(.*?)</h2>", re.S)
        username = re_u.findall(div)
        username = username[0].rstrip()
        # print(username)
        # 段子
        re_d = re.compile(r'<div class="content">\n<span>(.*?)</span>', re.S)
        duanzi = re_d.findall(div)
        duanzi = duanzi[0].strip()
        # print(type(duanzi))
        dic[username] = duanzi
    return dic

    # with open(r"F:/python_note/爬虫/file/file2.html", "w") as f:
    #     f.write(html)


url = "https://www.qiushibaike.com/text/page/1/"
info = jokeCrawler(url)
for k, v in info.items():
    print(k + ':\n' + v)