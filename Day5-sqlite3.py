# -*- coding= utf-8 -*-
# @Time : 2021-04-14 10:09
# @Author : baoguo
# @File : Day5-sqlite3.py
# @Software : PyCharm
import sqlite3

# 连接数据库
conn = sqlite3.connect("PaChong.bd")  # 打开或创建数据库文件

c = conn.cursor()  # 获取游标

# 创建数据表
# sql = '''
#     create table company
#         (id int primary key not null,
#         name text not null,
#         age int not null,
#         address char(50),
#         salary real);
# '''

# 插入数据
# sql = '''
#     insert into company(id, name, age, address, salary)
#         values(1, "张保国", 25, "重庆", 10000)
# '''

# 查询数据: 需要接收返回值
sql = '''
    select * from company;
'''
# c.execute(sql)  # 非查询时使用
select = c.execute(sql)  # 查询时执行sql
for i in select:
    print(i)

conn.commit()  # 提交

conn.close()  # 关闭
