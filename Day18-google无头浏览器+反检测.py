# -*- coding= utf-8 -*-
# @Time : 2021-05-03 11:33
# @Author : baoguo
# @File : Day18-google无头浏览器+反检测.py
# @Software : PyCharm
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options  # 实现无可视化界面(无头浏览器)
from selenium.webdriver import ChromeOptions  # 实现规避检测
# 无头浏览器的设置
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

# 实现selenium规避被检测到的风险
option = ChromeOptions()
option.add_experimental_option('excludeSwitches',['enable-automation'])
bro = webdriver.Chrome(executable_path='./chromedriver.exe',chrome_options=chrome_options, options=option)

bro.get('https://www.baidu.com')

print(bro.page_source)

sleep(2)

bro.quit()