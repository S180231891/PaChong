# -*- coding= utf-8 -*-
# @Time : 2021-04-27 14:32
# @Author : baoguo
# @File : Day16-线程池的使用.py
# @Software : PyCharm
import urllib.request
import requests
from urllib.request import urlretrieve
from lxml import etree
import re
from multiprocessing.dummy import Pool
import random
import time

'''
    梨视频爬虫相关步骤和反爬方案及解决办法
    爬虫相关步骤：
        1 通过url获取网页：askURL()
        2 通过正则或xpath进行相关数据的获取：获取网页上视频所在的页面链接    getVidio()
        3 存储视频的页面中，视频相关数据存储在ajax中，且使用了rmd设置随机参数    jsonURL()
            解决办法：
                在传headers时， 将Referer进行传递(通过Referer进行跳转的页面)
                并传递参数params,获取jsp中的json数据
        4 通过正则获取json数据中视频链接数据     videoMd5()
            此处获得的视频链接数据是假的url数据， 需要进行链接的处理(进行拼接和修改)才可进行真正的访问
        5 进行视频存储   完成梨视频网页视频数据的爬取
'''


def main():
    url = "https://www.pearvideo.com/category_130"
    getVidio(url)


def getVidio(url):
    html = askURL(url)
    tree = etree.HTML(html)
    video_list = tree.xpath('//div[@class="listvideo-list-bd"]/ul/li/div[@class="vervideo-bd"]/a/@href')
    video_name = tree.xpath(
        '//div[@class="listvideo-list-bd"]/ul/li/div[@class="vervideo-bd"]/a/div[@class="vervideo-title"]/text()')
    path = './video/'
    video_url = []
    for id, i in enumerate(video_list):
        time.sleep(1)
        link = path + str(video_name[id]) + '.mp4'
        video = "https://www.pearvideo.com/" + str(i)
        cmd = str(i).split('_')[-1]
        data = jsonURL(video, cmd)
        text = data['videoInfo']['videos']
        res = text['srcUrl']
        true_url = videoMd5(res, cmd)
        print(true_url)
        urlretrieve(true_url, link)


def videoMd5(video_url, cmd):
    true_url = ""
    s_list = str(video_url).split('/')
    for i in range(0, len(s_list)):
        if i < len(s_list) - 1:
            true_url += s_list[i] + '/'
        else:
            ss_list = s_list[i].split('-')
            for j in range(0, len(ss_list)):
                if j == 0:
                    true_url += 'cont-' + cmd + '-'
                elif j == len(ss_list) - 1:
                    true_url += ss_list[j]
                else:
                    true_url += ss_list[j] + '-'
    return true_url


def jsonURL(url, cmd):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/83.0.4103.116 Safari/537.36",
        "Referer": url
    }
    params = {
        "contId": cmd,
        "mrd": str(random.random())
    }
    new_url = "https://www.pearvideo.com/videoStatus.jsp"
    response = requests.get(url=new_url, headers=headers, params=params)
    data = response.json()
    return data


def askURL(url):
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/88.0.4324.150 Safari/537.36 "
    }
    res = urllib.request.Request(url, headers=header)
    res = urllib.request.urlopen(res)
    resp = res.read().decode("utf-8")
    return resp


if __name__ == '__main__':
    main()
