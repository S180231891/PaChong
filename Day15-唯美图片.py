# -*- coding= utf-8 -*-
# @Time : 2021-04-26 18:52
# @Author : baoguo
# @File : Day15-唯美图片.py
# @Software : PyCharm
import requests
import urllib.request
from urllib.request import urlretrieve
from lxml import etree
'''
    反爬机制太强
'''

def main():
    url = "https://www.vmgirls.com/12985.html"
    html = askURL(url)
    print(html)


def askURL(url):
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/88.0.4324.150 Safari/537.36 "
    }
    res = urllib.request.Request(url, headers=header)
    res = urllib.request.urlopen(res)
    resp = res.read().decode("utf-8")
    return resp


if __name__ == '__main__':
    main()
