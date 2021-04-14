# -*- coding= utf-8 -*-
# @Time : 2021-04-13 18:53
# @Author : baoguo
# @File : Day4-xlwt.py
# @Software : PyCharm
import xlwt

workbook = xlwt.Workbook(encoding="utf-8")  # 创建对象
worksheet = workbook.add_sheet("sheet1")  # 创建工作表
for i in range(1, 10):
    t = 1
    while t <= i:
        worksheet.write(i - 1, t - 1, "%d*%d=%d" % (i, t, i * t))
        t += 1
workbook.save("students.xls")
