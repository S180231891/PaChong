# -*- coding= utf-8 -*-
# @Time : 2021-04-21 15:13
# @Author : baoguo
# @File : Day10-requests-sogou.py
# @Software : PyCharm
'''
    requests使用流程：
        - 指定url
        - 发起请求
        - 获取响应数据
        - 持久化存储
    需求：
        爬取搜狗首页页面数据
'''
import urllib.parse
import requests
import re
import xlwt
from bs4 import BeautifulSoup


def main():
    url = "https://www.sogou.com/web?"
    keyword = input("请输入关键字：")
    getData(url, keyword)


def getData(url, keyword):
    html = askURL(url, keyword)
    bs = BeautifulSoup(html, 'html.parser')


def askURL(url, key):
    param = {
        "query": key
    }
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 "
                      "Safari/537.36 "
    }
    res = requests.get(url, params=param, headers=headers)
    resp = res.text
    return resp


if __name__ == '__main__':
    main()
