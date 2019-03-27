# -*- coding: utf-8 -*-
import scrapy
from myscrapy.items import TenCentItem

class TencentSpider(scrapy.Spider):
    name = 'tencent'
    allowed_domains = ['hr.tencent.com']
    start_urls = []
    for page in range(1):
        base_url = 'https://hr.tencent.com/position.php?lid=&tid=&keywords=python&start=%d#a'
        url = base_url%page
        start_urls.append(url)


    def parse(self, response):
        tr_list = response.xpath('//table[@class="tablelist"]/tr')
        tr_list.pop()
        tr_list.pop(0)
        for tr in tr_list:
            item = TenCentItem()

            #职位名称
            name = tr.xpath('./td[1]/a/text()').extract()[0]
            # print(name)
            item['name'] = name
            # #职位类型
            type1 = tr.xpath('./td[2]/text()').extract()[0]
            item['type1'] = type1

            #人数
            nub = tr.xpath('./td[3]/text()').extract()[0]
            item['nub'] = nub

            #地点
            address = tr.xpath('./td[4]/text()').extract()[0]
            item['address'] = address

            #时间
            time = tr.xpath('./td[4]/text()').extract()[0]
            item['time'] = time

            #详情页链接
            detail = tr.xpath('td[1]/a/@href').extract()[0]
            full_url = response.urljoin(detail)
            item['full_url'] = full_url

            yield scrapy.Request(url=full_url,callback=self.detail_parse,meta={'data':item,'phjs':True},dont_filter=False)

    def detail_parse(self, response):
        item = response.meta['data']
        url_list = response.xpath('//ul[@class="squareli"]')
        duty = url_list[0].xpath('./li/text()').extract()
        skill = url_list[1].xpath('./li/text()').extract()

        item['duty'] = duty
        item['skill'] = skill

        yield item