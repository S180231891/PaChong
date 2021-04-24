# -*- coding= utf-8 -*-
# @Time : 2021-04-22 15:25
# @Author : baoguo
# @File : Day11-数据解析-正则.py
# @Software : PyCharm
"""
    数据解析分类：
        - 正则
        - bs4
        - xpath
    项目需求：使用正则对糗事百科图片进行爬取
    url: https://toutiao.qiushibaike.com/
    抓包抓取的url：https://toutiao.qiushibaike.com/yuedu/api/tuwen?count=30
"""
import requests
from urllib.request import urlretrieve
import re
import os


def main():
    url = "https://toutiao.qiushibaike.com/yuedu/api/tuwen?count=30"
    json_data = askURL(url)
    savePath = "./QuTu"
    getImgURL(json_data, savePath)


def getImgURL(json_data, svaepath):
    count = 1
    for item in json_data['data']:
        for id, img in enumerate(item['urls']):
            print(img)
            # urlretrieve(img, svaepath + str(id) + ".jpg")


def askURL(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 "
                      "Safari/537.36 "
    }
    json_data = requests.get(url, headers).json()
    return json_data


if __name__ == '__main__':
    main()
