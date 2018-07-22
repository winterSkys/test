# coding=utf-8
# 抓取筷来财项目数据 ZD

import urllib.request
import ssl
from bs4 import BeautifulSoup

# 获取页面html内容


def get_html(get_url):

    page = urllib.request.urlopen(get_url)
    my_html = page.read()
    my_html = my_html.decode('utf-8')
    return my_html

# 获取指定DIV里面的数据


def get_div(html_data):

    soup = BeautifulSoup(html_data, 'lxml')
    a_list = soup.findAll('div', {'class': 'project-title'})

    project = []

    for a in a_list:

        # 获取数据并且去除空白符合

        project.append(a.get_text().strip())
    return project


ssl._create_default_https_context = ssl._create_unverified_context


url = "https://www.58klc.com/Borrow/index"
html = get_html(url)

project_list = get_div(html)

print('筷来财项目数据:')
print(project_list)
