# -*- coding= utf-8 -*-
# @Time : 2021-04-24 9:28
# @Author : baoguo
# @File : Day13-xPath-city.py
# @Software : PyCharm
import requests
from lxml import etree
import time
import urllib.request


def main():
    url = "https://www.aqistudy.cn/historydata/"
    getxPath(url)


def getxPath(url):
    f = open("city.txt", "a+", encoding="utf-8")
    html = askURL(url)
    tree = etree.HTML(html)
    citys = tree.xpath('//div[@class="all"]/div[@class="bottom"]/ul/div[2]/li/a/text()')
    for city in citys:
        f.write(city)
        f.write("\n")


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
