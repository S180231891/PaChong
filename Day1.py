"""
python是一门解释型、面向对象的高级编程语言
开源、容易维护
可移植
易使用，简单优雅
可扩展、可嵌入
广泛的标准库、功能强大

运行速度慢
代码不能加密
"""
# 输出
'''
print("www","baidu","com", sep=".")
print("hello", end="\t")
print("word", end="\n")
print("zbg")
'''

# 输入
'''
password = input("请输入密码:")
print("输入的密码为: ", password)
a, b = map(int, input().split(","))
c = list(map(int, input().split(",")))
print(a, b)
'''

# 运算符及条件判断语句
'''
import random as rd

print("请随机输入一个0-2之间的数字：剪刀(0), 石头(1), 布(2)")
x = int(input())
if x == 0:
    print("你输入的为: 剪刀")
elif x == 1:
    print("你输入的为: 石头")
else:
    print("你输入的为: 布")
y = rd.randint(0, 2)
print("随机生成的数字是：", y)
if x == y:
    print("平局收场")
elif x > y:
    if x - y == 1:
        print("哈哈，你输了")
    else:
        print("哎呀，大意了！！")
else:
    if y - x == 1:
        print("哎呀，大意了！！")
    else:
        print("哈哈，你输了")
'''

# 循环控制语句
'''
i = 1
sum = 0
while (i <= 100):
    sum += i
    i += 1
else:
    print("i大于100，结束")
print(sum)
'''

# for 和 while循环打印九九乘法表
'''
for i in range(1, 10):
    t = 1
    while t <= i:
        print("%d * %d = %d" % (i, t, i * t), end='\t')
        t += 1
    else:
        print(end='\n')
'''

# 字符串
'''
str = """
张保国
ZhangBaoGuo
BaoGuoNice
"""
print(str)
name = "zhangbaoguo"
print(name[:-1:2])
print("hello\nnice")  # 转义
print(r"hello\nnice")  # 显示原始字符串，不进行转义
'''
