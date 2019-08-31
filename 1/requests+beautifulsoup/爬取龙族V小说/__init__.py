import requests
from bs4 import BeautifulSoup

URL = "http://longzu5.co"
FILE_URL = '/Users/appti/Downloads/GitHub项目/Python_Crawler/1/requests+beautifulsoup/爬取龙族V小说/lz.txt'


def get_son_text(strs):
    # 获取文章内容
    soup = BeautifulSoup(strs, 'html.parser')
    body_soup = soup.find('div', 'post-body')
    result = body_soup.find_all('p')
    title = soup.find('h2', 'post-title')
    title = title.text
    final_txt = title + '\n'

    for item in result:
        txt = item.text
        final_txt += txt
    final_txt += '\n\n'
    with open(FILE_URL, 'a', encoding='utf-8') as f:
        f.write(final_txt)


def get_father_text():
    """
    获取文章列表
    :return:
    """
    res = requests.get(URL + "/")
    strs = res.text
    soup = BeautifulSoup(strs, 'html.parser')

    ul_soup = soup.find('ul', 'booklist')
    x = ul_soup.find_all('a')
    section_list = []
    for item in x:
        url = item.get('href')
        section_list.append(url)

    section_list.reverse()
    for url in section_list:
        print(url)
        section = requests.get(url)
        sec_txt = section.text
        get_son_text(sec_txt)


if __name__ == '__main__':
    get_father_text()