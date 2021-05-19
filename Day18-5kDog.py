# -*- coding= utf-8 -*-
# @Time : 2021-05-03 9:58
# @Author : baoguo
# @File : Day18-5kDog.py
# @Software : PyCharm
"""
    5k动物壁纸爬取：
        url: https://www.zhuoku.org/animals/
"""
import urllib.request, urllib.parse

from lxml import etree

import re

from urllib.request import urlretrieve

import time


def main():
    url = "https://www.zhuoku.org/animals/list-{}.html"

    for i in range(1, 2):
        time.sleep(2)
        new_url = url.format(i)
        img, title = saveImg(new_url)
        for key, i in enumerate(img):
            path = "./4kImg/" + str(title[key]) + '.' + str(i).split(".")[-1]
            urlretrieve(i, path)
            print("第%d张图片爬取成功！！" % key)


def saveImg(url):
    html = askURL(url)
    tree = etree.HTML(html)
    img = tree.xpath('//div[@class="wb_listbox"]/div[@class="wb_ppic"]//img/@src')
    title = tree.xpath('//div[@class="wb_listbox"]/div[@class="wb_ppic"]//img/@title')
    return img, title


def askURL(url):
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/88.0.4324.150 Safari/537.36 "
    }
    res = urllib.request.Request(url, headers=head)
    html = ""
    try:
        resp = urllib.request.urlopen(res)
        html = resp.read().decode('utf-8')
    except Exception as result:
        print(result)
    return html


if __name__ == '__main__':
    main()
