# -*- coding= utf-8 -*-
# @Time : 2021-04-26 9:23
# @Author : baoguo
# @File : Day14-cookie模拟登录.py
# @Software : PyCharm
import requests
from lxml import etree
from urllib.request import urlretrieve
from CJY import Chaojiying_Client


def main():
    url = "https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx"
    LoginUrl = "https://so.gushiwen.cn/user/login.aspx?from=http%3a%2f%2fso.gushiwen.cn%2fuser%2fcollect.aspx"
    html = askURL(url, LoginUrl)
    print(html)


def askURL(url, LoginUrl):
    session = requests.Session()
    ######################## 获取登陆界面 ############################
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/88.0.4324.150 Safari/537.36 "
    }
    html = session.get(url, headers=head).text
    ########################  获取登陆界面 ############################

    ######################## 获取验证码 ############################
    tree = etree.HTML(html)
    img = tree.xpath('//div[@class="mainreg2"][3]/img/@src')[0]
    __VIEWSTATE = tree.xpath('//*[@id="__VIEWSTATE"]/@value')[0]
    __VIEWSTATEGENERATOR = tree.xpath('//*[@id="__VIEWSTATEGENERATOR"]/@value')[0]
    n_img = "https://so.gushiwen.cn/" + img
    img_name = "gushi.jpg"
    urlretrieve(n_img, img_name)
    code = Chaojiying_Client.get_code(img_name)
    print(code)
    code = code['pic_str']
    ######################## 获取验证码 ############################

    ######################## 模拟登录， 自动cookie ############################
    data = {
        "__VIEWSTATE": __VIEWSTATE,
        "__VIEWSTATEGENERATOR": __VIEWSTATEGENERATOR,
        "from": "http://so.gushiwen.cn/user/collect.aspx",
        'email': '1064470580@qq.com',
        "pwd": "baoguo123",
        "code": code,
        "denglu": "登录"
    }
    response = session.post(url=LoginUrl, headers=head, data=data)
    print(response.status_code)
    ######################## 模拟登录， 自动cookie ############################

    next_url = "https://so.gushiwen.cn/user/collectbei.aspx?sort=t"
    # 自动传递参数
    res = session.get(url=next_url, headers=head)
    html = res.text
    return html


if __name__ == '__main__':
    main()
