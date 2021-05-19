# -*- coding= utf-8 -*-
# @Time : 2021-05-03 11:09
# @Author : baoguo
# @File : Day18-iframe-动作链.py
# @Software : PyCharm
"""
    - selenium处理iframe
            若定位的标签在iframe中，则必须先定位iframe，在及进行需求标签的访问获取switch_to.frame(id)
            动作链进行页面的拖动： from selenium.webdriver import ActionChains
                实例化动作链：action = ActionChains(bro)
                长按点击操作：action.click_and_hold(btn)
                进行页面的移动，设置移动像素： action.move_by_offset(17, 0)
                立即执行动作链：action.move_by_offset(17, 0).perform()
                释放动作链：action.release()
"""
from selenium import webdriver

from selenium.webdriver import ActionChains  # 导入动作链

from time import sleep

bro = webdriver.Chrome('chromedriver.exe')

bro.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')

bro.switch_to.frame("iframeResult")

btn = bro.find_element_by_id("draggable")

action = ActionChains(bro)

action.click_and_hold(btn)  # 点击长按指定的标签

for i in range(5):
    action.move_by_offset(17, 0).perform()  # 立即执行动作链操作

    sleep(0.3)
action.release()  # 释放动作链

bro.quit()
