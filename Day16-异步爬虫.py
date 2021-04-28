# -*- coding= utf-8 -*-
# @Time : 2021-04-27 10:51
# @Author : baoguo
# @File : Day16-异步爬虫.py
# @Software : PyCharm
from multiprocessing.dummy import Pool
import time

start_time = time.time()


def get_page(str):
    print("正在下载: ", str)
    time.sleep(2)
    print("下载成功 ", str)


name_list = ["zbg", 'xg', 'dc', 'zh']

# 实例化线程池对象
pool = Pool(4)
# 将列表中每一个列表元素传递给get_page进行处理
pool.map(get_page, name_list)

# for i in range(len(name_list)):
#     get_page(name_list[i])

end_time = time.time()

print('%d seconde' % (end_time - start_time))

