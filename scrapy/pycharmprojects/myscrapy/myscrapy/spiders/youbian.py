# -*- coding: utf-8 -*-
import scrapy
from myscrapy.items import YouBianItem
from lxml import etree

class YoudianSpider(scrapy.Spider):
    name = 'youbian'
    allowed_domains = ['ip138.com']
    start_urls = ['http://www.ip138.com/post/']

    def parse(self, response):
        content = response.body.decode('gbk')

        tree = etree.HTML(content)

        tbody = tree.xpath('//table[@class="t4"]')

        for tr in tbody:

            item = YouBianItem()

            td_address = tr.xpath('.//a/text()')
            item['address'] = td_address

            td_url = tr.xpath('.//a/@href')[0]

            url = 'http://www.ip138.com/post'
            full_url = url + td_url
            item['url'] = full_url

            yield item
            print(item)