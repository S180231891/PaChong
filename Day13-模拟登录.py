"""
    模拟登录：
        - 爬取基于用户登录的信息
    需求：
        - 对人人网进行模拟登录
        - 模拟用户名和密码的填写，模拟验证码的填写
        - post请求进行参数传递
        - TODO:存在的问题：验证码是通过Math.random随机生成的，获取的连接中只包含random,获取不到对应的参数
"""
import urllib.request
from lxml import etree
from urllib.request import urlretrieve
from CJY import Chaojiying_Client
import random


def main():
    url = "http://www.renren.com/SysHome.do"
    imgName = "renrencode.jpg"
    code = getImgCode(url, imgName)
    LoginUrl = "http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=2021361516537"
    getImgCode(LoginUrl, code)


def getLogin(url, code):
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/88.0.4324.150 Safari/537.36 "
    }
    userName = "15320293056"
    data = {
        "email": userName,
        "icode": code,
        "origURL": "http://www.renren.com/home",
        "captcha_type": "web_login",
        "password": "0a09f22e0ccbe5f09fbef8bd07ddc643c0d5b7dadfa08ff4318ceefdd585dd58",
        "rkey": "8e9d4a0ad6579040c975655e2071a5f3",
        "f": ""
    }
    res = urllib.request.Request(url=url, headers=head, data=data)
    html = ""
    try:
        resp = urllib.request.urlopen(res)
        html = resp.read().decode('utf-8')
    except Exception as result:
        print(result)
    return html


def getImgCode(url, imgName):
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/88.0.4324.150 Safari/537.36 "
    }
    res = urllib.request.Request(url, headers=head)
    try:
        resp = urllib.request.urlopen(res)
        html = resp.read().decode('utf-8')
        tree = etree.HTML(html)
        img = tree.xpath('//*[@id="verifyPic_login"]/@src')[0]
        rand = str(img).split("&")[0]
        img = rand + "rand=" + str(random.random())
        urlretrieve(img, imgName)
        code = Chaojiying_Client.get_code(imgName)
        print(code)
        return code['pic_str']
    except Exception as result:
        print(result)


if __name__ == '__main__':
    main()
