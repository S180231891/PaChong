# -*- coding= utf-8 -*-
# @Time : 2021-04-13 13:16
# @Author : baoguo
# @File : Day4-urlLib.py
# @Software : PyCharm
import urllib.request, urllib.parse

# get请求
'''
response = urllib.request.urlopen("http://www.baidu.com")
print(response.read().decode('utf-8'))  # 对获取到的网页进行解码操作
'''
# post请求: 模拟浏览器发出的请求，需要进行封装
'''
url = "http://httpbin.org/post"
data = bytes(urllib.parse.urlencode({"hello":"world"}), encoding="utf-8")
response = urllib.request.urlopen(url, data=data)
print(response.read().decode("utf-8"))
'''

# 超时处理
'''
try:
        url = "http://httpbin.org/get"
        response = urllib.request.urlopen(url, timeout=1)  # 超时设置
        print(response.read().decode("utf-8"))
except Exception as result:
    print(result)
'''

# 请求头设置
'''
url = "http://www.baidu.com"
response = urllib.request.urlopen(url)
print(response.status)  # 状态码418：发现查重
print(response.getheaders())

url = "http://httpbin.org/post"  # 测试网址
data = bytes(urllib.parse.urlencode({"name": "zhangbaoguo"}), encoding="utf-8")
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) " \
                        "Chrome/89.0.4389.90 Safari/537.36"}
req = urllib.request.Request(url=url, data=data, headers=header, method="POST")
response = urllib.request.urlopen(req)
print(response.read().decode("utf-8"))
'''
# 访问豆瓣
url = "https://www.douban.com"
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) " \
                        "Chrome/89.0.4389.90 Safari/537.36"}
req = urllib.request.Request(url=url, headers=header)
response = urllib.request.urlopen(req)
print(response.read().decode("utf-8"))