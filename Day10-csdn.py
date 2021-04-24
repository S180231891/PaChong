# -*- coding= utf-8 -*-
# @Time : 2021-04-21 16:41
# @Author : baoguo
# @File : Day10-csdn.py
# @Software : PyCharm
'''
    需求：CSDN排行榜
    url: https://blog.csdn.net/rank/list/total
'''
import requests
import re
import xlwt
import time


def main():
    url = "https://blog.csdn.net/phoenix/web/blog/allRank?page={}&pageSize=20"
    data = getData(url)
    print(len(data))
    saveData(data, 'csdnTop100.xls')


data_list = []


def saveData(data_list, savePath):
    book = xlwt.Workbook(encoding="utf-8")
    seet = book.add_sheet("CSDN-TOP100", cell_overwrite_ok=True)
    cols = ("排名", "名称", "粉丝数", "获赞数", "博客等级", "综合指标")
    for i in range(0, len(cols)):
        seet.write(0, i, cols[i])
    for id, text in enumerate(data_list):
        for index in range(len(text)):
            seet.write(id + 1, index, text[index])
        print("第%d条数据保存成功！！！" % (id + 1))
    book.save(savePath)


def getData(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 "
                      "Safari/537.36 "
        
    }

    for i in range(5):
        time.sleep(2)
        json_ids = requests.get(url=url.format(i), headers=headers).json()
        data = json_ids['data']
        for text in data['allRankListItem']:
            t_data = []
            currentRank = text['currentRank']
            t_data.append(currentRank)
            nickName = text['nickName']
            t_data.append(nickName)
            fansCount = text['fansCount']
            t_data.append(fansCount)
            diggCount = text['diggCount']
            t_data.append(diggCount)
            level = text['level']
            t_data.append(level)
            hotRankScore = text['hotRankScore']
            t_data.append(hotRankScore)
            data_list.append(t_data)
    return data_list


if __name__ == '__main__':
    main()