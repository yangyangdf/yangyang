# -*- coding: utf-8 -*-
import scrapy
from lxml import etree
from myscrapy.items import MyscrapyItem
import requests

class SMaoyanSpider(scrapy.Spider):
    name = 's_maoyan'
    allowed_domains = ['maoyan.com']
    start_urls = []

    base_url = 'https://maoyan.com/cinemas?offset=%d'
    for page in range(0,2):
        offset = page*12
        try:
            url = base_url % offset
            if len(requests.request('get', url=url).text) > 200:
                start_urls.append(url)
        except:
            pass

        # start_urls.append(url)

    def parse(self, response):
        # print(response)
        content = response.body.decode('utf-8')
        # with open('youbain.html','w',encoding='utf-8')as fp:
        #     fp.write(content)
        #提取数据：
        # print(content)
        tree = etree.HTML(content)

        cell_list = tree.xpath('//div[@class="cinema-cell"]')
        for cell in cell_list:
            #影院名称：
            item = MyscrapyItem()

            name = cell.xpath('./div[@class="cinema-info"]/a/text()')[0]

            item['name'] = name

            #地址：
            adress = cell.xpath('./div[@class="cinema-info"]/p/text()')[0]

            item['adress'] = adress

            yield item


