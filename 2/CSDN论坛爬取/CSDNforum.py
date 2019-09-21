import requests
from bs4 import BeautifulSoup


URL = "https://bbs.csdn.net/forums/spark?page="
FILE_URL = '/Users/appti/Downloads/GitHub项目/Python_Crawler/2/CSDN论坛爬取/论坛.txt'


def set_pages(pages):
    for i in range(1,pages + 1):
        get_page_content(str(i))


def get_page_content(pageNumber):
    res = requests.get(URL + pageNumber)
    strs = res.text
    # print(strs)

    soup = BeautifulSoup(strs, 'html.parser')
    table = soup.find('tbody')
    topics = table.find_all('tr')
    for topic in topics:
        text = ""
        tds = topic.find_all('td')
        state = tds[0]
        points = tds[1]
        title = tds[2]
        author = tds[3]
        replysAndViews = tds[4]
        replysAndViewsList = replysAndViews.contents[1].text.split("/")

        text ="话题状态："+ state.contents[1].text + "\n" + "赏分："+points.contents[1].text + "\n" + "主体："+title.contents[1].text + "\n" + "作者："+author.contents[1].text+"\n"+ "时间："+author.contents[3].text + "\n" + "回复数："+replysAndViewsList[0] + "\n" + "浏览数:"+ replysAndViewsList[1]+"-----------------------------\n\n"
        write_in_file(FILE_URL,text)

        # print("话题状态：",state.contents[1].text)
        # print("赏分：",points.contents[1].text)
        # print("主体：",title.contents[1].text)
        # print("作者：",author.contents[1].text)
        # print("时间：",author.contents[3].text)
        # print("回复数：",replysAndViewsList[0])
        # print("浏览数:",replysAndViewsList[1])
        # print("-----------------------------")

def write_in_file(FILE_URL,final_txt):
    with open(FILE_URL, 'a', encoding='utf-8') as f:
        f.write(final_txt)



if __name__ == '__main__':
    set_pages(10)