# -*- coding= utf-8 -*-
# @Time : 2021-04-20 9:49
# @Author : baoguo
# @File : Day8-药监局数据爬取.py
# @Software : PyCharm
import requests
import json
import time
import re
import xlwt

'''
    药监局数据爬取：http://scxk.nmpa.gov.cn:81/xk/
        获取XHR中的数据
        使用requests进行数据爬取
'''


def main():
    URL = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList'
    De_URL = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById'
    Ids = askURL(URL)
    json_data = getJsonData(De_URL, Ids)
    text = getData(json_data)
    saveXlwt(text, "NMPA.xls")


def saveXlwt(text, path):
    book = xlwt.Workbook(encoding="utf-8")
    seet = book.add_sheet("国家药品企业数据监督管理局数据", cell_overwrite_ok=True)
    cols = ("企业名称", "许可证编号", "许可项目", "企业住所", "生产地址", "社会信用代码", "法定代表人", "企业负责人", "质量负责人", "发证机关", "签发人", "日常监督管理机构",
            "日常监督股那里人员", "有效期", "发证日期")
    for i in range(0, len(cols)):
        seet.write(0, i, cols[i])
    for id, data in enumerate(text):
        for index in range(len(data)):
            seet.write(id + 1, index, data[index])
        print("第%d条数据保存成功！！！" % (id + 1))
    book.save(path)


def getData(json_data):
    text = []
    for data in json_data:
        data_text = []
        epsName = data['epsName']
        data_text.append(epsName)
        productSn = data['productSn']
        data_text.append(productSn)
        certStr = data['certStr']
        data_text.append(certStr)
        epsAddress = data['epsAddress']
        data_text.append(epsAddress)
        epsProductAddress = data['epsProductAddress']
        data_text.append(epsProductAddress)
        businessLicenseNumber = data['businessLicenseNumber']
        data_text.append(businessLicenseNumber)
        legalPerson = data['legalPerson']
        data_text.append(legalPerson)
        businessPerson = data['businessPerson']
        data_text.append(businessPerson)
        qualityPerson = data['qualityPerson']
        data_text.append(qualityPerson)
        qfManagerName = data['qfManagerName']
        data_text.append(qfManagerName)
        xkName = data['xkName']
        data_text.append(xkName)
        rcManagerDepartName = data['rcManagerDepartName']
        data_text.append(rcManagerDepartName)
        rcManagerUser = data['rcManagerUser']
        data_text.append(rcManagerUser)
        xkDate = data['xkDate']
        data_text.append(xkDate)
        xkDateStr = data['xkDateStr']
        data_text.append(xkDateStr)
        text.append(data_text)
    return text


def getJsonData(url, id_list):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 "
                      "Safari/537.36 "
    }
    data_list = []
    for i in id_list:
        data = {
            'id': i
        }
        json_data = requests.post(url=url, headers=headers, data=data).json()
        data_list.append(json_data)
    return data_list


def askURL(url):
    id_list = []
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 "
                      "Safari/537.36 "
    }
    page_len = 3
    for page in range(1, page_len):
        time.sleep(3)
        data = {
            "on": "true",
            "page": page,
            "pageSize": "15",
            "productName": "",
            "conditionType": "1",
            "applyname": "",
            "applysn": "",
        }
        json_ids = requests.post(url=url, headers=headers, data=data).json()
        for dic in json_ids['list']:
            id_list.append(dic['ID'])
    return id_list


if __name__ == '__main__':
    main()
