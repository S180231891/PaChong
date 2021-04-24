from bs4 import BeautifulSoup
import requests
import urllib.request


def main():
    url = "https://www.baidu.com/"
    Bs4_text(url)


def Bs4_text(url):
    html = askURL(url)
    soup = BeautifulSoup(html, 'lxml')
    print(soup.a)  # 获取对象属性，只获取第一次出现的标签属性
    print(soup.find('a'))  # 和soup.a搜索的结果相同
    print(soup.find('div', class_='s-isindex-wrap'))  # 属性定位
    print(soup.find_all('div', id="lg"))  # 返回符合要求的所有标签，亦可以进行属性定位，返回列表
    print(soup.select('#lg'))  # 可放入选择器， 返回的是一个列表值
    print("===========重点选择器  select===================")
    print(soup.select("#lg > img")[0])  # 层级选择器，成层级定位 "空格"表示多个层级  “>”号表示一个层级

    print("===========获取标签中的文本数据==================")
    print(soup.a.text)  # 获取标签中所有的文本内容
    print(soup.a.string)  # 只获取标签中直系的文本内容
    print(soup.a.get_text())  # 获取标签中所有的文本内容


def askURL(url):
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/88.0.4324.150 Safari/537.36 "
    }
    res = urllib.request.Request(url, headers=header)
    res = urllib.request.urlopen(res)
    resp = res.read().decode("utf-8")
    return resp


if __name__ == '__main__':
    main()
