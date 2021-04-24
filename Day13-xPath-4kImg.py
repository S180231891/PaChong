# -*- coding= utf-8 -*-
# @Time : 2021-04-24 8:31
# @Author : baoguo
# @File : Day13-xPath-4kImg.py
# @Software : PyCharm
import requests
from lxml import etree
import time
import urllib.request
from urllib.request import urlretrieve


def main():
    url = "https://pic.netbian.com/4kmeinv/"
    savePath = "./4KImg/"
    getxPath(url, savePath)
    for i in range(2, 20):
        url = "https://pic.netbian.com/4kmeinv/index_{}.html"
        new_url = url.format(i)
        getxPath(new_url, savePath)


def getxPath(url, savePath):
    html = askURL(url)
    tree = etree.HTML(html)
    Img_urls = tree.xpath('//div[@class="slist"]/ul/li/a/img/@src')
    Img_text = tree.xpath('//div[@class="slist"]/ul/li/a/img/@alt')
    for key, img in enumerate(Img_urls):
        new_img = "https://pic.netbian.com/" + img
        title = str(Img_text[key]).strip().replace(" ", "")
        path = savePath + str(title)+".jpg"
        urlretrieve(new_img, path)


def askURL(url):
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/88.0.4324.150 Safari/537.36 "
    }
    res = urllib.request.Request(url, headers=header)
    res = urllib.request.urlopen(res)
    resp = res.read().decode("gbk")
    return resp


if __name__ == '__main__':
    main()
