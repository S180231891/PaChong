# -*- coding= utf-8 -*-
# @Time : 2021-04-13 10:11
# @Author : baoguo
# @File : Day4-网页爬虫.py
# @Software : PyCharm
"""
    需求分析：
        爬取豆瓣电影Top250的基本信息，包括电影名称、豆瓣评分、评价数、电影概况、电影链接等
        https://movie.douban.com/top250
    有用搜索 ： 百度指数   天眼查
    测试地址：httpbin.org  可对post/get等请求进行测试 看是否伪装浏览器请求成功
    基本流程：
        准备工作：
            分页网址：https://movie.douban.com/top250?start=100  通过start进行分页 (页数-1)*25
            User-Agent:Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36
            引入相关模块(第三方)：添加相应的函数包
                from bs4 import BeautifulSoup
                import re
                import urllib
                import xlwt

        获取数据：
        解析内容：
        保存数据：
"""
from bs4 import BeautifulSoup  # 网页解析， 获取数据
import re  # 正则，进行文字匹配
import urllib.request, urllib.error  # 指定URL，获取网页数据
import xlwt  # 数据存储，存入excel
import sqlite3  # sqlite存储操作


def main():
    # 爬取网页
    # 解析数据
    # 保存数据
    url = "https://movie.douban.com/top250?start="
    datalist = getData(url)
    savepath = r"movie.xls"
    # saveData(datalist, savepath)
    # 保存到数据库中
    dbpath = 'movie.db'
    saveDB2Data(datalist, dbpath)


# 影片链接地址提取规则
findlink = re.compile(r'<a href="(.*?)">')  # 创建正则表达式
# 影片图片的链接地址
findImgSrc = re.compile(r'<img.*src="(.*?)"', re.S)  # 忽略换行符
# 影片片名
findTitle = re.compile(r'<span class="title">(.*)</span>')
# 影片评分
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
# 影片评价人数
findJudge = re.compile(r'<span>(\d*)人评价</span>')
# 影片概况
findInq = re.compile(r'<span class="inq">(.*)</span>')
# 简述
findBd = re.compile(r'<p class="">(.*?)</p>', re.S)


# 1 爬取网页
def getData(url):
    datalist = []
    for i in range(0, 10):  # 获取页面信息
        url = "https://movie.douban.com/top250?start="
        url = url + str(i * 25)
        # print(url)
        html = askURL(url)  # 抓取网页信息
        # 2 逐一解析数据
        soup = BeautifulSoup(html, "html.parser")
        # bs4认真解读
        for item in soup.find_all('div', class_="item"):
            data = []  # 保存电影中所需要获取的信息
            item = str(item)  # 转成字符串进行操作
            link = re.findall(findlink, item)[0]  # 电影的超链接
            data.append(link)

            imgSrc = re.findall(findImgSrc, item)[0]
            data.append(imgSrc)

            titles = re.findall(findTitle, item)
            if len(titles) == 2:
                ctitle = titles[0]
                data.append(ctitle)
                otitle = titles[1].replace("/", "")
                otitle = "".join(otitle.split())  # 去空格\ax0\
                data.append(otitle)
            else:
                data.append(titles[0])
                data.append(" ")

            rating = re.findall(findRating, item)[0]
            data.append(rating)

            judge = re.findall(findJudge, item)[0]
            data.append(judge)

            inq = re.findall(findInq, item)
            if len(inq) != 0:
                inq = inq[0]
                data.append(inq)
            else:
                data.append(" ")

            bd = re.findall(findBd, item)[0]
            bd = re.sub("<br(\s+)?/>(\s+)?", " ", bd)  # 去掉br
            bd = re.sub("/", " ", bd)
            bd = "".join(bd.split())
            data.append(bd.strip())
            datalist.append(data)  # 处理好的数据信息放入list中
    print(len(datalist))
    return datalist


# 得到指定url的网页内容
def askURL(url):
    # 用户代理：告诉服务器我们使用的浏览器能接收什么类型的数据
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/89.0.4389.90 Safari/537.36 "
    }
    req = urllib.request.Request(url, headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(req)
        html = response.read().decode("utf-8")
    except Exception as result:
        print(result)
    return html


def saveData(datalist, savepath):
    book = xlwt.Workbook(encoding="utf-8")  # 创建对象
    sheet = book.add_sheet("豆瓣电影信息Top250", cell_overwrite_ok=True)  # 创建工作表
    col = ("电影链接", "图片链接", "电影中文名", "电影英文名", "评分", "评价数", "概况", "相关信息")
    for i in range(0, 8):
        sheet.write(0, i, col[i])
    for i in range(0, 250):
        print("第%d条" % i)
        data = datalist[i]
        for j in range(0, 8):
            sheet.write(i + 1, j, data[j])

    book.save(savepath)  # 保存数据


def saveDB2Data(datalist, dbpath):
    init_db(dbpath)
    conn = sqlite3.connect(dbpath)
    cursor = conn.cursor()
    for data in datalist:
        for index in range(len(data)):
            data[index] = '"' + data[index] + '"'
        sql = '''
            insert into movie250
            (
            info_link, pic_link, cname, ename, score,  rated, instroduction, info
            )
            values(%s)
            ''' % ",".join(data)
        cursor.execute(sql)
        conn.commit()
    cursor.close()
    conn.close()


def init_db(dbpath):
    sql = '''
        create table movie250
            (
                id integer primary key autoincrement,
                info_link text,
                pic_link text,
                cname varchar,
                ename varchar,
                score numeric,
                rated numeric,
                instroduction text,
                info text
            );
    '''
    conn = sqlite3.connect(dbpath)
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    conn.close()


if __name__ == '__main__':
    main()
    print("爬取完毕！")
