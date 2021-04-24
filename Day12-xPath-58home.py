"""
    xPath解析：
        - 实例化一个etree对象
        - 调用etree对象中的方法，结合表达式实现属性的定位和数据的获取
        - xpath表达式：
            / 从根节点开始定位 一个"/"表示一个层级
            // 表示多个层级 从任意位置进行标签的定位
        - 属性定位
            //div[@class="song]  定位到class=song的div
        - 索引定位：索引从1开始
            //div[@class="song]/p[3]  定位到class=song的div中的第三个p标签中的数据
        - 取文本: 在标签后添加text()获取文本内容  列表显示
            tree.xpath("//div[@class="tang"]//li[5]/a/text()")[0]
            /text:获取标签中直系的文本内容
            //text:获取标签中非直系的文本内容
        - 取属性
            tree.xpath('//div[@class="song"]/img/@src') 获取div中class=song标签下img标签中src属性的值



"""
from lxml import etree
import urllib.request
import time


def main():
    url = "https://www.baidu.com/"
    for i in range(10):
        time.sleep(3)
        new_url = "https://cn.58.com/ershoufang/p{}/?PGTID=0d100000-008d-2fc5-c264-02b8abe2780f," \
                  "0d30000c-0000-1755-06e2-014305e4bdea&ClickID=1 "
        xPath(new_url)


def xPath(url):
    # 本地html导入
    # etree.parse('test.html')
    f = open('51home.txt', 'a+', encoding='utf-8')
    html = askURL(url.format(1))
    print(html)
    tree = etree.HTML(html)
    data_list = tree.xpath('//section[@class="list-main"]//div[@class="property-content-title"]/h3/text()')
    for data in data_list:
        f.write(data)
        f.write('\n')


def askURL(url):
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/88.0.4324.150 Safari/537.36 "
    }
    res = urllib.request.Request(url, headers=header)
    resp = urllib.request.urlopen(res)
    html = resp.read().decode('utf-8')
    return html


if __name__ == '__main__':
    main()
