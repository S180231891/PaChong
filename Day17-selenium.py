# -*- coding= utf-8 -*-
# @Time : 2021-04-28 15:25
# @Author : baoguo
# @File : Day17-selenium.py
# @Software : PyCharm
"""
    selenium作用：
        - 可便捷获取网站中动态加载的数据
        - 便捷实现模拟登录
    selenium定义：
        - 基于浏览器自动化的一个模块
    selenium使用流程：
        - pip install selenium
        - 下载浏览器驱动程序
            - google驱动下载链接： http://chromedriver.storage.googleapis.com/index.html
        - 实例化浏览器对象
        - 编写自动操作代码
            - 发起请求：get
            - 标签定位：find
            - 标签交互(数据交互， 填写数据)：send_keys
            - 执行js：execute_script
            - 前进、后退操作：back() forward()
            - 关闭浏览器：quit()


"""
from selenium import webdriver
from lxml import etree

bro = webdriver.Chrome(executable_path='chromedriver.exe')  # 实例化浏览器对象

bro.set_window_size(480, 800)

url = "http://scxk.nmpa.gov.cn:81/xk/"

bro.get(url=url)  # 让浏览器对象发送请求

# 获取浏览器当前页面源码数据
page_text = bro.page_source

# 解析获取的数据
tree = etree.HTML(page_text)

data = tree.xpath('//*[@id="gzlist"]/li/dl/a/text()')

print(data)

bro.quit()