# -*- coding= utf-8 -*-
# @Time : 2021-04-15 8:40
# @Author : baoguo
# @File : Day6-小说爬虫实战.py
# @Software : PyCharm
import urllib.request, urllib.error
from bs4 import BeautifulSoup
import xlwt
import re
import sqlite3
import gzip
from io import BytesIO

'''
    需求：小说爬取 
    url = "http://www.biquku.la/0/421/" 
    数据爬取出现UnicodeDecodeError: 
        'utf-8' codec can't decode byte 0x8b in position 1: invalid start byte错误
    是因为Accept-Encoding: gzip, deflate 
    需要通过gzip、BytesIO进行解压缩
    '''


def main():
    url = "http://www.biquku.la/0/421/"
    getData(url)
    # askURL(url)


PageUrl = re.compile(r'<a href="(.*?)">.*</a>')
tName = re.compile(r'<h1>(.*)</h1>', re.S)
tData = re.compile(r'<div id="content">(.*?)</div>')


def getData(url):
    list = getUrl(url)
    for i in range(len(list)):
        newUrl = ""
        newUrl = url + str(list[i])
        html = askURL(newUrl)
        btf = BeautifulSoup(html, "html.parser")
        for item in btf.find_all('div', class_='content_read'):
            item = str(item)
            tname = re.findall(tName, item)[0]
            tdata = re.findall(tData, item)
            with open("DouLuoDaLu/" + tname + '.txt', 'w', encoding='utf-8') as f:
                for data in tdata:
                    data = "".join(data.split())
                    f.write(data.replace('<br/><br/>', '\n').strip())
                    print("%s 下载成功" % tname)
    print("下载成功")


def getUrl(url):
    urlList = []
    html = askURL(url)
    btf = BeautifulSoup(html, "html.parser")
    item = btf.find_all(id="list")
    item = str(item)
    pageurl = re.findall(PageUrl, item)
    for i in pageurl:
        urlList.append(i)
    return urlList


def askURL(url):
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/89.0.4389.90 Safari/537.36 "
    }
    req = urllib.request.Request(url, headers=head)
    html = ""
    try:
        resp = urllib.request.urlopen(req)
        html = resp.read()
        buff = BytesIO(html)
        f = gzip.GzipFile(fileobj=buff)
        html = f.read().decode("utf-8")
    except Exception as result:
        print(result)
    return html


if __name__ == '__main__':
    main()
