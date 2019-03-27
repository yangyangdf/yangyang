# -*- coding: utf-8 -*-
import scrapy
from lxml import etree
from myscrapy.items import QSBKItem


class SQiushibaikeSpider(scrapy.Spider):
    name = 's_qiushibaike'
    allowed_domains = ['qiushibaike.com']
    start_urls = []

    base_url = 'https://www.qiushibaike.com/hot/page/%d/'
    for page in range(1,2):
        url = base_url%page
        start_urls.append(url)

    def parse(self, response):
        content = response.body.decode('utf-8')

        tree = etree.HTML(content)

        # print(content)

        joker_list = tree.xpath('//*[@id="content-left"]')
        for joker in joker_list:
            item = QSBKItem()

            username = joker.xpath('./div/div/a[2]/h2/text()')
            content = joker.xpath('./div/a/div/span/text()')

            item['username'] = username
            item['content'] = content

            # print('==========================================')
            # print(content)

            yield item