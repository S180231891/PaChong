# -*- coding= utf-8 -*-
# @Time : 2021-04-22 10:38
# @Author : baoguo
# @File : Day11-JinDong.py
# @Software : PyCharm
import requests
import re
import json

'''
    练习：
        肯德基搜索数据在线爬取：http://www.kfc.com.cn/kfccda/storelist/index.aspx
'''


def main():
    url = "http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword"
    keyword = input("请输入用餐地址：")
    askURL(url, keyword)


def askURL(url, keyword):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 "
                      "Safari/537.36 "
    }
    fp = open("kfc.json","a+", encoding="utf-8")
    for i in range(1, 5):  # 通过i控制页数
        data = {
            'cname': '',
            'pid': '',
            'keyword': keyword,
            'pageIndex': i,
            'pageSize': '10'
        }
        json_data = requests.post(url, data, headers).json()
        json.dump(json_data, fp=fp, ensure_ascii=False)
        print(json_data)


if __name__ == '__main__':
    main()
