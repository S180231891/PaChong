# -*- coding= utf-8 -*-
# @Time : 2021-04-26 10:11
# @Author : baoguo
# @File : Day14-IP代理.py
# @Software : PyCharm
"""
    IP代理网站：
        快代理
        西祠代理
        http://www.goubanjia.com/
    代理IP的匿名程度：
        - 透明：服务器知道该次请求使用了代理， 知道请求对应的真实IP
        - 匿名：服务器知道请求使用了代理， 但不知道请求的真实IP
        - 高匿名：不知道使用了代理， 不知道真实IP
"""
import requests
if __name__ == '__main__':
    url = "https://qifu.baidu.com/api/sme/aladdin/ip/query"
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/88.0.4324.150 Safari/537.36 "
    }
    res = requests.get(url, head, proxies={"http": "124.205.155.153:9090"})
    html = requests.get(url, head, proxies={"http": "124.205.155.153:9090"}).text
    print(html)
    ""
    with open("id.html", 'w', encoding="utf-8") as t:
        t.write(html)
