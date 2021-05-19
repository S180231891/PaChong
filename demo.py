# -*- coding= utf-8 -*-
# @Time : 2021-04-26 19:55
# @Author : baoguo
# @File : demo.py
# @Software : PyCharm
import requests
import urllib.request
from bs4 import BeautifulSoup
from lxml import etree
# 智联招聘
if __name__ == '__main__':
    url = "https://www.lagou.com/zhaopin/"
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/88.0.4324.150 Safari/537.36 ",
        'cookie': 'privacyPolicyPopup=false; user_trace_token=20210426203449-1851f552-3875-4c2d-b181-f47b6dc7c80a; '
                  '__lg_stoken__'
                  '=ed816a968fd8cc0b61cd93054e57735e4f0bffd794425511a89d8264b2fd04f8f9cea3a18ce8b21a7dfbcd12c61b2fd2eab948eb67388f20f7786b1d2d8f015804f0952fd186; JSESSIONID=ABAAABAABAGABFAC8262990608B01AA20D38001B6584D48; WEBTJ-ID=20210426%E4%B8%8B%E5%8D%888:35:20203520-1790e2d4f0cd16-071cf49cad4771-d7e163f-2073600-1790e2d4f0dabd; PRE_UTM=; PRE_HOST=; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Fzhaopin%2F; sajssdk_2015_cross_new_user=1; sensorsdata2015session=%7B%7D; PRE_SITE=https%3A%2F%2Fwww.lagou.com; _ga=GA1.2.597481936.1619440521; _gid=GA1.2.709101479.1619440521; LGUID=20210426203451-54aa471f-89b0-463b-8295-3b400f21ea6f; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1619440521; LGSID=20210426203451-af392d6d-83b4-43b1-96b2-f9197b86b4e1; gate_login_token=f9448591d21942cd82694d8553525038f700c58836aec7e2c9c5917d599afc4c; LG_LOGIN_USER_ID=79b40907f4a70c2c8f2431571cc88d37964f1c72b62563d8caece67dfcc8a92e; LG_HAS_LOGIN=1; _putrc=598169A236E9EDFE123F89F2B170EADC; login=true; unick=%E5%BC%A0%E4%BF%9D%E5%9B%BD; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=0; privacyPolicyPopup=false; index_location_city=%E5%85%A8%E5%9B%BD; _gat=1; SEARCH_ID=c60980dfb56345139082ccce929e60fb; X_HTTP_TOKEN=a901a247fb7ea8593751449161414ca1f25ae1de90; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1619441603; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2218738370%22%2C%22first_id%22%3A%221790e2d4ffbb1c-0bd9fcd7535d67-d7e163f-2073600-1790e2d4ffccfb%22%2C%22props%22%3A%7B%22%24os%22%3A%22Windows%22%2C%22%24browser%22%3A%22Chrome%22%2C%22%24browser_version%22%3A%2290.0.4430.85%22%2C%22lagou_company_id%22%3A%22%22%7D%2C%22%24device_id%22%3A%221790e2d4ffbb1c-0bd9fcd7535d67-d7e163f-2073600-1790e2d4ffccfb%22%7D; LGRID=20210426205253-507431c0-2f76-4c74-871f-32f197f68d22 '
    }

    res = urllib.request.Request(url, headers=header)
    res = urllib.request.urlopen(res)
    html = res.read().decode("utf-8")
    tree = etree.HTML(html)
    print(tree)
    for i in range(1, 10):
        path = '//*[@id="s_position_list"]/ul/li['+str(i)+']/@data-positionname'
        data = tree.xpath(path)
        print(data)