# -*- coding= utf-8 -*-
# @Time : 2021-04-28 15:55
# @Author : baoguo
# @File : Day17-selenium-taobao.py
# @Software : PyCharm
from selenium import webdriver
from lxml import etree
import time

bro = webdriver.Chrome(executable_path='chromedriver.exe')

bro.get('https://www.taobao.com/')

# 实现标签定位(搜索框定位)
search_input = bro.find_element_by_id('q')

# 标签交互
search_input.send_keys('U盘')  # 需要搜索的产品

# 执行js代码
bro.execute_script('window.scrollTo(0,document.body.scrollHeight)')
time.sleep(2)

# 搜索提交按钮定位
btn = bro.find_element_by_css_selector('.btn-search')

btn.click()  # 点击搜索

bro.get("https://www.baidu.com")
time.sleep(2)
# 浏览器回退
bro.back()

time.sleep(2)

# 浏览器前进
bro.forward()

time.sleep(5)

bro.quit()
