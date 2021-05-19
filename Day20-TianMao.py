# -*- coding= utf-8 -*-
# @Time : 2021-05-08 10:32
# @Author : baoguo
# @File : Day20-TianMao.py
# @Software : PyCharm
from selenium import webdriver
import time
import urllib.request, urllib.parse
import requests
from lxml import etree
import xlwt
from selenium.webdriver import ActionChains  # 导入动作链
from selenium.webdriver.chrome.options import Options  # 实现无可视化界面(无头浏览器)
from selenium.webdriver import ChromeOptions  # 实现规避检测
import random


# 无头浏览器的设置


def main():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')

    # 实现selenium规避被检测到的风险
    option = ChromeOptions()
    option.add_experimental_option('excludeSwitches', ['enable-automation'])
    bro = webdriver.Chrome(executable_path='./chromedriver.exe', chrome_options=chrome_options, options=option)

    bro.get('https://www.jd.com/?cu=true&utm_source=haosou-search')

    keyword = input("请输入要搜索的产品名称：")

    key = urllib.parse.quote(keyword)
    bro.find_element_by_id('key').send_keys(keyword)
    time.sleep(5)
    bro.find_element_by_class_name('button').click()
    getData(key)


def getData(key):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 "
                      "Safari/537.36 "
    }

    url = "https://search.jd.com/Search?keyword={}"

    new_url = url.format(key)

    res = urllib.request.Request(url=new_url, headers=headers)
    resp = urllib.request.urlopen(res)

    html = resp.read().decode("utf-8")

    tree = etree.HTML(html)

    link_url = tree.xpath('//*[@id="J_goodsList"]/ul/li//div[@class="p-img"]/a/@href')

    link_Img = tree.xpath('//*[@id="J_goodsList"]/ul/li//div[@class="p-img"]/a/img/@src')

    price = tree.xpath('//*[@id="J_goodsList"]/ul/li//div[@class="p-price"]//i/text()')

    for i in link_url:
        print(i)


if __name__ == '__main__':
    main()
