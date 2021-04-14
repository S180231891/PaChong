# -*- coding= utf-8 -*-
# @Time : 2021-04-12 15:33
# @Author : baoguo
# @File : Day2.py
# @Software : PyCharm
import random

'''
name = ["张", 3.56, 1, False]
for i in name:
    print(type(i))
'''

# 数据的增删改查
'''
# 增加
name.append("张三丰")
name.insert(0, "我第一")  # 指定索引，插入数据
name.extend("我最后")  # 拆分extend中的值
print(name)
# 删除
movieName = ["速度与激情", "终极一班", "python", "Java", "终极一班"]
movieName.pop()
del movieName[2]
movieName.remove("终极一班")  # 按先后顺序删除，删除找到的第一个元素
print(movieName)

# 改变数据
name[1] = "无极"
print(name)

# 查找数据
if "无极" in name:
    print("Yes")
else:
    print("No")

a = ['a', 'b', 'c', 'a', 'd']
print(a.index("a", 0, 4))  # 指查找第一个找到的元素，并返回下标，若找不到，会报错
print(a.count("a"))  # 统计元素个数
a = a.reverse()
b = [2, 4, 1, 3, 7]
b.reverse()  # 反转
print(b)
b.sort(reverse=True)  # 倒序
print(b)
'''

# 嵌套
'''
schoolName = [["山东", "路东"], ["q", 'e', 'w'], [1, 23, 45, 67, "erf"]]
print(schoolName[0][1])
'''

# 八个老师随机分配到三个办公室
'''
office = [[], [], []]
teacher = ["A", "B", "C", "D", "E", "F", "G", "H"]
for name in teacher:
    index = random.randint(0, 2)
    office[index].append(name)
print(office)
'''

# 作业练习：
'''
products = [["iphone", 6888], ["MacPro", 14800], ["小米11", 2499], ["Coffee", 31], ["Book", 60], ["Nike", 699]]
dict = {}
for i, prs in enumerate(products):  # 枚举
    print(i, prs[0], prs[1], sep="\t")
    dict[i] = prs[0]
prd = []
for i in range(10):
    print("请问您想购买什么物品：")
    x = input()
    if x.isdigit():
        if int(x) in dict.keys():
            print("购买的物品编号为：%d" %int(x))
            prd.append(dict[int(x)])
            print(prd)
        else:
            print("本店暂无您购买的商品")
    if x == "q":
        print("退出购物")
        break
print(prd)
'''

# 元组tuple学习
tup = ()
tup1 = (50,)
no_tup = (50)
print(type(tup), type(tup1), type(no_tup))

# tuple增删改查
'''
# 增
s1 = (12, 34, 56)
s2 = ("abc", "xyz")
s3 = s1 + s2  # 新增元素  更改地址
print(s3)

# 删
del s1
print(s3)

# 改
info = {"name": "吴彦祖", "age": 18}
print(info["name"])
print(info["age"])
info["nice"] = "BG"
print(info.get("ZG"))  # 寻找字典中是否存在对应的键值，没有则返回None
print(info.get("ZG", "m"))  # 若不存在，设置默认值为m
'''

# 字典的增删改查
'''
info = dict(a=1, b=2, c=3)
# 增加
info['d'] = 4
# 删除
del info["d"]  # 删除d的指定键值对
print(info)

info.clear()  # 清空dict中的所有数据
print(info)

# 改
info['e'] = 5  # 修改和插入相同操作

# 查
print(info.keys())
print(info.values())
print(info.items())
'''

# set是一个集合，无value  常用来去除重复操作

