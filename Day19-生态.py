# -*- coding= utf-8 -*-
# @Time : 2021-05-06 16:04
# @Author : baoguo
# @File : Day19-生态.py
# @Software : PyCharm
import urllib.request, urllib.error
from lxml import etree


def main():
    url = "http://gdee.gd.gov.cn/falv/index.html"
    saveData(url)


def saveData(url):
    html = askURL(url)
    tree = etree.HTML(html)
    data = tree.xpath('//div[@class="listimg_data"]/ul/li/div/a/@href')
    data_title = tree.xpath('//div[@class="listimg_data"]/ul/li/div/a/@title')
    f = open('生态.txt', 'a+', encoding='utf-8')
    for key, i in enumerate(data):
        html = askURL(i)
        tree = etree.HTML(html)
        text = tree.xpath('//div[@id="logPanel"]/p/text()')
        data = []
        for j in text:
            res = str(j).strip()
            res = res.replace('\u3000\u3000', '')
            print(res)


def askURL(url):
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/88.0.4324.150 Safari/537.36 "
    }
    res = urllib.request.Request(url, headers=header)
    html = ""
    try:
        resp = urllib.request.urlopen(res)
        html = resp.read().decode('utf-8')
    except Exception as t:
        print(t)
    return html


if __name__ == '__main__':
    main()
