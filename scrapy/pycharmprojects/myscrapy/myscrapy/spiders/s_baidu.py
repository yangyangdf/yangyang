#coding:utf-8
import scrapy

class BaiduSpider(scrapy.Spider):

    name = "s_baidu"

    allowed_domains = ['baidu.com']

    start_urls = ['http://www.baidu.com']


    def parse(self, response):
        with open('baidu.html','w',encoding='utf-8')as f:
            f.write(response.body.decode('utf-8'))
