# -*- coding= utf-8 -*-
# @Time : 2021-05-06 19:44
# @Author : baoguo
# @File : Day19-5KImg.py
# @Software : PyCharm
# -*- coding:utf-8 -*-
"""
    url: https://unsplash.com/napi/topics/people/photos?page=1&per_page=10
"""
from urllib.request import urlretrieve
import requests
import json
import time


def main():
    url = "https://unsplash.com/napi/topics/people/photos?page={}&per_page=10"
    path = './4kImg/'
    for i in range(2):
        time.sleep(1)
        new_url = url.format(i)
        jsonObj = askURL(new_url)
        for key, js in enumerate(jsonObj):
            save_path = path + str(i * 10) + str(key) + '.jpg'
            link = js['links']['download']
            # text = requests.get(link).content
            urlretrieve(link, save_path)
            print(save_path)


def askURL(url):
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/88.0.4324.150 Safari/537.36 "
    }
    res = requests.get(url, header).json()
    return res


if __name__ == '__main__':
    main()
