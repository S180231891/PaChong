# -*- coding= utf-8 -*-
# @Time : 2021-05-06 14:42
# @Author : baoguo
# @File : Day19-淘宝模拟登录.py
# @Software : PyCharm
from time import sleep
from selenium import webdriver

# TODO：为解决滑动验证问题

bro = webdriver.Chrome('chromedriver.exe')
bro.maximize_window()  # 设置窗口最大化
bro.get('https://login.taobao.com/')

bro.find_element_by_id('fm-login-id').send_keys('XXXXX')
bro.find_element_by_id('fm-login-password').send_keys('XXXXX')
bro.find_element_by_class_name('fm-button').click()