# -*- coding= utf-8 -*-
# @Time : 2021-04-27 10:28
# @Author : baoguo
# @File : Day16-cqupt.py
# @Software : PyCharm
import requests
from urllib.request import urlretrieve
from lxml import etree
from CJY import Chaojiying_Client


def main():
    url = "http://gs.cqupt.edu.cn/UserLogin.aspx?exit=1"
    code = Img(url)
    print(code)


def Img(url):
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/88.0.4324.150 Safari/537.36 "
    }
    html = requests.get(url, header).text.encode('utf-8')
    tree = etree.HTML(html)
    Link = tree.xpath('//input[@id="ValidateImage"]/@src')
    img_Link = "http://gs.cqupt.edu.cn/" + str(Link)
    print(img_Link)
    exit()
    img_name = "code.jpg"
    urlretrieve(img_Link, img_name)
    data = Chaojiying_Client.get_code(img_name)
    code = data['pic_str']
    return code


if __name__ == '__main__':
    main()
