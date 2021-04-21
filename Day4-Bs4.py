# -*- coding= utf-8 -*-
# @Time : 2021-04-13 14:08
# @Author : baoguo
# @File : Day4-Bs4.py
# @Software : PyCharm
from bs4 import BeautifulSoup
import re
"""
    BeautifulSoup将复杂的HTML文档转换为一个复杂的树形结构，每个节点都是python对象，所有对象归纳为4种：
    - Tag: 首个标签获取
    - NavigableString: 获取标签内容
    - BeautifulSoup：获取整个文档
    - Comment：
    BeautifulSoup默认支持Python的标准HTML解析库：
        1 Python标准库     BeautifulSoup(html, 'html.parser')
        2 lxml HTML解析库  BeautifulSoup(html, 'lxml')
        3 lxml XML解析库   BeautifulSoup(html, 'lxml')
        4 html5lib解析库   BeautifulSoup(html, 'html5lib')
"""
'''
file = open("baidu.html", "rb")
html = file.read()
bs = BeautifulSoup(html, "html.parser")
# print(bs.prettify())  # 缩进格式

# 获取title标签中的所有内容： 只拿到第一个标签
print(bs.title)
# 获取标签内容
print(bs.title.string)
# 获取标签中的属性
print(bs.a.attrs)
# 获取整个文档
print(type(bs))
# print(bs.head)  # 获取标签中的所有内容

# 获取注释：是一个特殊的NavigableString
print(bs.a.string)

print("============================================")
# 文档的遍历
print(bs.head.contents[0])
# 文档的搜索
# find_all
'''

'''
file = open("baidu.html", "rb")
html = file.read()
bs = BeautifulSoup(html, "html.parser")
# 字符串过滤
t_list = bs.find_all("a")  # 找所有的a标签：字符串过滤


# 正则表达式
a_list = bs.find_all(re.compile(r"a"))


# 方法：传入函数，按要求搜索
def name_is_exists(tag):
    return tag.has_attr("name")


n_list = bs.find_all(name_is_exists)
print(n_list)
'''

# 2.kwargs 参数
file = open("baidu.html", "rb")
html = file.read()
bs = BeautifulSoup(html, "html.parser")
c_list = bs.find_all(id="head")  # 显示所有数据

# 3.text参数
d_list = bs.find_all(text=["地图", "hao123"])
# print(d_list)
e_list = bs.find_all(text = re.compile("\d"))
# print(e_list)
# 4. limit 参数
f_list = bs.find_all("a", limit=3)
# print(f_list)

# CSS选择器
print(bs.select("title"))  # 标签

print(bs.select(".mnav"))  # 类名

print(bs.select("#u1"))  # id查找

