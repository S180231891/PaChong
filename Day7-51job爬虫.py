# -*- coding= utf-8 -*-
# @Time : 2021-04-16 9:49
# @Author : baoguo
# @File : Day7-51job爬虫.py
# @Software : PyCharm
"""
    异步爬取：抓取json
    数据分类：
        数据分析  950   ：https://search.51job.com/list/000000,000000,0000,00,9,99,%25E6%2595%25B0%25E6%258D%25AE%25E5%2588%2586%25E6%259E%2590,2,1.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare=
        前端     950   ：https://search.51job.com/list/000000,000000,0000,00,9,99,%25E5%2589%258D%25E7%25AB%25AF,2,1.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare=
        python  950   : https://search.51job.com/list/000000,000000,0000,00,9,99,python,2,1.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare=
        ui      950   ：https://search.51job.com/list/000000,000000,0000,00,9,99,UI,2,1.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare=
"""
import json
import urllib.request, urllib.error
import xlwt
import re
import time
import pymysql
import sqlite3


def main():
    URL = "https://search.51job.com/list/000000,000000,0000,00,9,99,%25E6%2595%25B0%25E6%258D%25AE%25E5%2588%2586%25E6%259E%2590,2,{}.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare="
    # 避免反爬机制：1时间间隔   2代理
    dataList = getData(URL)
    print(dataList)
    exit()
    saveDataList(dataList)
    # path = "51job.xls"
    # saveXlwt(dataList, path)


def getData(url):
    dataList = []
    for i in range(1, 5):
        time.sleep(2)
        newUrl = url.format(i)
        html = askURL(newUrl)
        jsonData = re.findall(r'"engine_search_result":(.+?),"jobid_count"', str(html))
        jsonObj = json.loads(jsonData[0])
        for item in jsonObj:
            text = []
            text.append(item['job_name'])
            text.append(item['company_name'])
            text.append(item['providesalary_text'])
            text.append(item['workarea_text'])
            text.append(item['companytype_text'])
            text.append(item['issuedate'])
            text.append(item['jobwelf'])
            text.append(str(item['attribute_text']).replace('[', '').replace(']', '').replace("'", ''))
            text.append(item['companysize_text'])
            text.append(item['companyind_text'])
            dataList.append(text)
    return dataList


# xls
def saveXlwt(dataList, path):
    book = xlwt.Workbook(encoding="utf-8")
    seet = book.add_sheet("51job-数据分析", cell_overwrite_ok=True)
    col = ("职位名称", "企业", "薪资", "地点", "公司类型", "招聘时间", "福利待遇", "招聘信息", "公司规模", "公司性质")
    for i in range(0, len(col)):
        seet.write(0, i, col[i])
    for id, data in enumerate(dataList):
        for idx in range(len(data)):
            seet.write(id + 1, idx, data[idx])
        print("第%d条数据保存成功" % (id + 1))
    book.save(path)  # 保存数据


# MySql
def saveDataList(dataList):
    conn = pymysql.connect(host='localhost', user='root', passwd='123456', db='pcdata', port=3306, charset='utf8')
    cursor = conn.cursor()  # 定义光标对象
    temp = 1
    for data in dataList:
        print("当前保存第%d条数据" % temp)
        for index in range(len(data)):
            data[index] = '"' + data[index] + '"'
        sql = '''
            insert into 51job(name, company, salary, address, type, date, jobwelf, attribute, companysize, companyind)
            values(%s)
        ''' % ",".join(data)
        try:
            cursor.execute(sql)
            conn.commit()
            print("第%d条数据保存成功" % temp)
        except:
            conn.rollback()
        temp += 1
    cursor.close()
    conn.close()  # 关闭数据库连接
    print("51job数据爬取完毕!!!")


def askURL(url):
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/89.0.4389.90 Safari/537.36 "
    }
    req = urllib.request.Request(url, headers=head)
    html = ""
    try:
        resp = urllib.request.urlopen(req)
        html = resp.read().decode("gbk")
    except Exception as result:
        print(result)
    return html


if __name__ == '__main__':
    main()
