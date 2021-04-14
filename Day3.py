# -*- coding= utf-8 -*-
# @Time : 2021-04-13 9:29
# @Author : baoguo
# @File : Day3.py
# @Software : PyCharm

# 函数学习
'''
# 函数定义
def printinfo():
    print("----------------------------")
    print("      Python用起来还可以")
    print("----------------------------")


# 函数调用
printinfo()


# 返回多值函数
def divid(a, b):
    s = a // b
    y = a % b
    return s, y


s, y = divid(5, 10)
print(s, y)
'''

# 全局变量和局部变量  若有定义局部  用局部  若无局部  则全局
'''
a = 100


def test1():
    global a  # 声明全局变量的标识符global
    a = 200  # 修改全局变量
    print(a)


def test2():
    print(a)

test1()
test2()
'''

# 文件操作
# a: 追加  r:只读  w: 创建文件,覆盖已有的数据
# readlines：读取所有
# readline：每次读取一行
# TODO:os 文件处理模块
'''
import os

os.rename("a.txt", "b.txt")
'''

# 异常处理模块
'''
try:
    print(num)  # 异常捕获需要类型一致
    f = open("a.txt", "r")
    print(f.readlines())
    f.close()
except Exception as result:  # 异常捕获
    print(result)
'''

