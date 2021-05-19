import scrapy


class TestSpider(scrapy.Spider):
    name = 'test'  # 爬虫文件名称， 唯一标识
    allowed_domains = ['www.baidu.com']  # 允许的域名:限定列表中哪些url可进行请求发送
    start_urls = ['http://www.baidu.com/']  # 起始的url列表：该列表中的url会自动请求发送

    def parse(self, response):
        pass
