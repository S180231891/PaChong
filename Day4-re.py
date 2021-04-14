# -*- coding= utf-8 -*-
# @Time : 2021-04-13 15:33
# @Author : baoguo
# @File : Day4-re.py
# @Software : PyCharm
import re

'''
    正则表达式：字符串模式，判断字符串的标准
'''
# 创建对象
pat = re.compile("AA")  # 格式
m = pat.search("AACDAADDAA")  # 验证：只寻找第一次查询到的数据并返回
print(m)

# 不创建对象
m = re.search("ASD", "adASDhdg")
print(m)

m = re.findall("[A-Z]+", "ahSkjsuFqdnUyAB")
print(m)

# sub
# 在asc中找到a，用A来替换
print(re.sub("a", "A", "asc")) # sub进行替换

# 在正则表达式中，字符串前面加上r，避免出现转义

