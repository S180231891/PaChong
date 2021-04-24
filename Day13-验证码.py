# -*- coding= utf-8 -*-
# @Time : 2021-04-24 11:00
# @Author : baoguo
# @File : Day13-验证码.py
# @Software : PyCharm
"""
    验证码识别：
        反爬机制：验证码用来识别图片中的数据， 用于模拟登录操作

        验证码识别操作类别：
            - 人工肉眼识别
            - 第三方自动识别 (推荐使用)
                - 超级鹰：
                    1 注册登陆后，选择 开发文档-python
                    2 下载python的SDK 超级鹰图像识别python语言Demo下载
                    3 软件ID生成：
                        进入用户中心-软件ID-填写软件名称-生成软件ID
                    4 获取代码后，更改代码中get_code()函数
                        更改用户名、密码、及软件ID
                        放入验证码， 填写验证类型：在价格体系中选择合适的验证类型
                    5 前提条件：你要有账户题分才可进行验证码验证，1元=1000题分
                    6 验证码验证成功

    需求：识别古诗文网中登录界面的验证码
    TODO:古诗文登陆失败
"""
from CJY import Chaojiying_Client
import urllib.request
import requests
from lxml import etree
from urllib.request import urlretrieve


def main():
    url = "https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx"
    img = "gushi.jpg"
    code = getImg(url, img)
    LoginUrl = "https://so.gushiwen.cn/user/login.aspx?from=http%3a%2f%2fso.gushiwen.cn%2fuser%2fcollect.aspx"
    html = getLogin(LoginUrl, code)
    print(html)


def getLogin(url, code):
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/88.0.4324.150 Safari/537.36 "
    }
    userName = "15320293056"
    data = {
        "__VIEWSTATEGENERATOR": "C93BE1AE",
        "from": "http://so.gushiwen.cn/user/collect.aspx",
        'email': '1064470580@qq.com',
        "pwd": "baoguo123",
        "code": code,
        "denglu": "登录"

    }
    response = requests.post(url=url, headers=head, data=data)
    starts = response.status_code
    print(starts)
    html = response.text
    return html


def getImg(url, img_name):
    html = askURL(url)
    tree = etree.HTML(html)
    img = tree.xpath('//div[@class="mainreg2"][3]/img/@src')[0]
    n_img = "https://so.gushiwen.cn/" + img
    urlretrieve(n_img, img_name)
    code = Chaojiying_Client.get_code(img_name)
    print(code)
    str = code['pic_str']
    return str


def askURL(url):
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/88.0.4324.150 Safari/537.36 "
    }
    res = urllib.request.Request(url, headers=head)
    html = ""
    try:
        resp = urllib.request.urlopen(res)
        html = resp.read().decode('utf-8')
    except Exception as result:
        print(result)
    return html


if __name__ == '__main__':
    main()
