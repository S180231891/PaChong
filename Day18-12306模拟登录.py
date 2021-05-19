# -*- coding= utf-8 -*-
# @Time : 2021-05-03 14:06
# @Author : baoguo
# @File : Day18-12306模拟登录.py
# @Software : PyCharm
"""
    12306模拟登录
        - 打开登录界面
        - 对页面截图
        - 对截图图片局部裁剪 验证码
            - 将验证码图片和模拟登录一一对应
        - 使用超级鹰识别验证码图片  获取坐标
        - TODO：滑动检验
            12306改版   多了滑动检验反爬策略 项目暂未实现登录
"""
from selenium import webdriver
from time import sleep
from CJY import Chaojiying_Client
from lxml import etree
from PIL import Image
from selenium.webdriver import ActionChains
bro = webdriver.Chrome('chromedriver.exe')
bro.maximize_window()  # 设置窗口最大化
bro.get('https://exservice.12306.cn/excater/index.html')
btn = bro.find_element_by_id('J-btn-login')
btn.click()
btn = bro.find_element_by_class_name('login-hd-account')
btn.click()
bro.save_screenshot('12306.png')  # 对当前页面截图保存
code_img_ele = bro.find_element_by_class_name('touclick-wrapper')  # 验证码所在的标签
# 获取截图中验证码所在的坐标
location = code_img_ele.location  # 返回验证码图片左上角的坐标
size = code_img_ele.size  # 验证码标签对应的长和宽
rangle = (
    int(location['x']), int(location['y']), int(location['x'] + size['width']), int(location['y'] + size['height'])
)
i = Image.open("12306.png")
code_img = "code.png"
frame = i.crop(rangle)
frame.save(code_img)
code = Chaojiying_Client.get_code(code_img)  # 识别验证码
code = code['pic_str']
list = []  # 存储待点击的坐标
if '|' in code:
    list_1 = code.split('|')
    count_1 = len(list_1)
    for i in range(count_1):
        xy_list = []
        x = int(list_1[i].split(',')[0])
        y = int(list_1[i].split(',')[1])
        xy_list.append(x)
        xy_list.append(y)
        list.append(xy_list)
else:
    x = int(code.split(',')[0])
    y = int(code.split(',')[1])
    xy_list = []
    xy_list.append(x)
    xy_list.append(y)
    list.append(xy_list)
# 遍历列表
for j in list:
    x = j[0]
    y = j[1]
    ActionChains(bro).move_to_element_with_offset(code_img_ele, x, y).click().perform()  # 根据坐标点击图片
sleep(5)

bro.find_element_by_id('J-userName').send_keys("xxxxxxxx")
bro.find_element_by_id('J-password').send_keys("xxxxxxxx")
bro.find_element_by_id('J-login').click()
sleep(10)

bro.quit()

