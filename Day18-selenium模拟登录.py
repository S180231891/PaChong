# -*- coding= utf-8 -*-
# @Time : 2021-05-03 10:47
# @Author : baoguo
# @File : Day18-selenium模拟登录.py
# @Software : PyCharm
"""
QQ空间模拟登录
"""
from selenium import webdriver

from time import sleep

bro = webdriver.Chrome('chromedriver.exe')


url = "https://qzone.qq.com/"

bro.get(url=url)



bro.switch_to.frame('login_frame')  # iframe标签获取, 切换浏览器标签定位 的作用域

btn = bro.find_element_by_id("switcher_plogin")

btn.click()

userName = bro.find_element_by_id('u')
passWord = bro.find_element_by_id('p')

userName.send_keys("1064470580@qq.com")
passWord.send_keys("baoguo123")

submit = bro.find_element_by_id("login_button")

submit.click()

sleep(10)

bro.quit()
