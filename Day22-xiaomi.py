# -*- coding= utf-8 -*-
# @Time : 2021-05-30 9:17
# @Author : baoguo
# @File : Day22-xiaomi.py
# @Software : PyCharm
import urllib.request, urllib.error
from urllib.request import urlretrieve
from lxml import etree
import time
import requests
import os


def main():
    url = "https://www.xiaomi.cn/board/17862742"
    html = askURL(url)
    print(html)


def askURL(url):
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/90.0.4430.93 Safari/537.36 ",
    }
    res = urllib.request.Request(url, headers=header)
    html = ""
    try:
        resp = urllib.request.urlopen(res)
        html = resp.read().decode("utf-8")
    except Exception as t:
        return t
    return html


if __name__ == '__main__':
    main()
