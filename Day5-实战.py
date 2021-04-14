# -*- coding= utf-8 -*-
# @Time : 2021-04-14 8:33
# @Author : baoguo
# @File : Day5-实战.py
# @Software : PyCharm
"""
    # TODO: 存在问题， 无法处理具有换行的HTML：如下
        <span class="pl">(
                    329278人评价
                )</span>
        获取不到数据
"""
import urllib.request, urllib.error
from bs4 import BeautifulSoup
import xlwt
import re
import sqlite3


def main():
    url = "https://book.douban.com/top250?start="
    BookList = getData(url)
    path = "book.xls"
    saveData(BookList, path)
    dbpath = "book.db"
    getDBdata(BookList, dbpath)


bookUrl = re.compile(r'<a class="nbg" href="(.*?)"')
bookImg = re.compile(r'<img src="(.*?)"')
bookName = re.compile(r'<a.*title="(.*)">')
bookAut = re.compile(r'<p class="pl">(.*)</p>')  # 数据需要处理
bookRat = re.compile(r'<span class="rating_nums">(.*)</span>')
# bookPl = re.compile(r'<span class="pl">((\d*)人评价)</span>')
bookInq = re.compile(r'<span class="inq">(.*?)</span>')


def getData(url):
    BookList = []
    for i in range(0, 10):
        url = "https://book.douban.com/top250?start="
        url = url + str(i * 25)
        html = askURL(url)
        btf = BeautifulSoup(html, "html.parser")
        for item in btf.find_all("tr", class_="item"):
            data = []
            item = str(item)
            bookurl = re.findall(bookUrl, item)[0]
            data.append(bookurl)
            bookimg = re.findall(bookImg, item)[0]
            data.append(bookimg)
            bookname = re.findall(bookName, item)[0]
            data.append(bookname)
            bookaut = re.findall(bookAut, item)[0]
            bookaut = bookaut.replace("/", "")
            bookaut = ",".join(bookaut.split())
            data.append(bookaut.strip())
            bookrat = re.findall(bookRat, item)[0]
            data.append(bookrat)
            # bookpl = re.findall(bookPl, item)
            # data.append(bookpl)
            bookinq = re.findall(bookInq, item)
            if len(bookinq) != 0:
                data.append(bookinq[0])
            else:
                data.append(" ")
            BookList.append(data)
    return BookList


def saveData(BookList, savepath):
    wook = xlwt.Workbook(encoding="utf-8")
    seet = wook.add_sheet("优秀书籍Top250", cell_overwrite_ok=True)
    col = ("图书链接", "图片链接", "图书名", "作者", "评分", "概况")
    for i in range(0, 6):
        seet.write(0, i, col[i])
    for i in range(0, 250):
        Book = BookList[i]
        print("第%d条" % i)
        for j in range(0, 6):
            seet.write(i + 1, j, Book[j])
    wook.save(savepath)


def askURL(url):
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/89.0.4389.90 Safari/537.36 "
    }
    request = urllib.request.Request(url, headers=header)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
    except Exception as result:
        print(result)
    return html


def getDBdata(datalist, dbpath):
    init_db(dbpath)
    conn = sqlite3.connect(dbpath)
    cursor = conn.cursor()
    for book in datalist:
        print(book)
        for index in range(len(book)):
            book[index] = '"'+book[index]+'"'
        sql = '''
            insert into book250
            (
            info_link, pic_link, name, author, score, info
            )
            values(%s)
        ''' % ",".join(book)
        cursor.execute(sql)
        conn.commit()
    cursor.close()
    conn.close()


def init_db(dbpath):
    sql = '''
            create table book250
                (
                    id integer primary key autoincrement,
                    info_link text,
                    pic_link text,
                    name varchar,
                    author varchar,
                    score numeric,
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
    print("完成数据爬虫")
