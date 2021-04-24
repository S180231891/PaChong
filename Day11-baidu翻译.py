# -*- coding= utf-8 -*-
# @Time : 2021-04-22 9:19
# @Author : baoguo
# @File : Day11-baidu翻译.py
# @Software : PyCharm
import requests
import json


def main():
    url = "https://fanyi.baidu.com/sug"
    keyword = input("请输入要查找的单词：")
    data = askURL(url, keyword)
    text = open('saveJson.json', 'w', encoding='utf-8')
    json.dump(data, fp=text, ensure_ascii=False)  # 直接保存为json数据


def askURL(url, KeyWord):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 "
                      "Safari/537.36 "
    }

    data = {
        'kw':KeyWord
    }
    data = requests.post(url, headers=headers, data=data).json()
    return data


if __name__ == '__main__':
    main()
