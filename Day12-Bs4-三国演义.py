from bs4 import BeautifulSoup
import requests
import urllib.request, urllib.parse
import re


def main():
    keyword = "三国演义"
    keyword = urllib.parse.quote(keyword)
    url = "https://so.gushiwen.org/search.aspx?type=guwen&page={0}&value={1}"
    for i in range(1, 15):
        print("第%d章节开始爬取" % i)
        new_url = url.format(i, keyword)
        text = Bs4(new_url)
        getData(text, new_url)
        print("over!!!")


def getData(data_list, url):
    with open("三国演义.txt", 'a+', encoding='utf-8') as df:
        for link in data_list:
            html = askURL(link)
            soup = BeautifulSoup(html, 'lxml')
            for text in soup.select(".left > .sons > .cont"):
                word = text.get_text()
                word = word.strip('\t')
                df.write(word)


def Bs4(url):
    text = []
    html = askURL(url)
    soup = BeautifulSoup(html, 'lxml')
    top = 0
    for item in soup.select(".left > .sons > .cont > p > a "):
        text_url = re.findall(r'<a href="(.*?)".*?', str(item))
        n_text_url = "https://so.gushiwen.org" + text_url[0]
        if top % 2 == 0:
            text.append(n_text_url)
        top += 1
    return text


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
