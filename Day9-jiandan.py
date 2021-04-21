# -*- coding= utf-8 -*-
# @Time : 2021-04-21 8:18
# @Author : baoguo
# @File : Day9-jiandan.py
# @Software : PyCharm
"""
  url：http://jandan.net/girl
"""
import urllib.request
from urllib.request import urlretrieve
import re
from bs4 import BeautifulSoup
import pymysql
import xlwt


def main():
    url = "http://jandan.net/girl/MjAyMTA0MjEtMTEy#comments"
    data = getData(url, 0)
    savePath = "./jiandanImg/"
    saveImg(data, savePath)


data_list = []
name = re.compile(r'<div class="author"><.*?>(.*?)</strong>')
img = re.compile(r'<img.*?src="(.*?)".*?/>', re.S)


def getData(url, rst):
    html = askURL(url)
    soup = BeautifulSoup(html, "html5lib")
    item = soup.find_all("div", id="comments")
    item = str(item)
    data = []
    url_next = re.findall(r'<a class="previous-comment-page" href="(.*?)" title="Older Comments">', item)[0]
    if url_next != "" and rst < 10:
        t_name = re.findall(name, item)
        t_img = re.findall(img, item)
        data.append(t_name)
        data.append(t_img)
        data_list.append(data)
    else:
        return "结束图片爬取"
    rst = rst + 1
    url_next = "http:" + url_next
    print(url_next)
    getData(url_next, rst)
    return data_list


def saveImg(data_list, svaepath):
    for data in data_list:
        for id, img in enumerate(data[1]):
            n_img = "http:" + img
            print(n_img)
            print(img.split('.')[-1])
            urlretrieve(n_img, svaepath + str(id) + "_girl." + img.split('.')[-1])


def askURL(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/86.0.4240.183 "
                      "Safari/537.36 "
    }
    res = urllib.request.Request(url, headers=headers)
    html = ""
    try:
        resp = urllib.request.urlopen(res)
        html = resp.read().decode('utf-8')
    except Exception as result:
        print(result)
    return html


if __name__ == '__main__':
    main()
