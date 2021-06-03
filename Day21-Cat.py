# -*- coding= utf-8 -*-
# @Time : 2021-05-19 19:29
# @Author : baoguo
# @File : Day21-Cat.py
# @Software : PyCharm
import urllib.request, urllib.error
from urllib.request import urlretrieve
from lxml import etree
import time
import requests
import os


def main():
    url = "https://movie.douban.com/subject/4321270/photos?type=S&start={}&sortby=like&size=a&subtype=a"
    save_path = "./4kImg/"
    for key in range(0, 180, 30):
        time.sleep(1)
        new = url.format(key)
        saveJpg(new, save_path, key)


def saveJpg(url, save_path, k):
    html = askURL(url)
    tree = etree.HTML(html)
    link_path = tree.xpath('//*[@id="content"]/div/div[1]/ul/li/div[1]/a/img/@src')
    for key, jpg in enumerate(link_path):
        print(jpg)
        time.sleep(2)
        path = save_path + str(k + key) + ".jpg"
        # urlretrieve(jpg, path)
        with open(path, 'wb') as tf:
            img = requests.get(jpg).content
            tf.write(img)


def askURL(url):
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/90.0.4430.93 Safari/537.36 ",
        "Referer":"https://movie.douban.com/subject/4321270/photos?type=S&start=150&sortby=like&size=a&subtype=a"
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
