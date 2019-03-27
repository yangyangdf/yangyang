# -*- coding: utf-8 -*-
import scrapy
from myscrapy.items import MeiJuItem

class MeijuSpider(scrapy.Spider):
    name = 'meiju'
    allowed_domains = ['meijutt.com']
    start_urls = ['https://www.meijutt.com/new100.html']


    def parse(self, response):
        li_list = response.xpath('//ul[@class="top-list  fn-clear"]/li')

        for li in li_list:
            item = MeiJuItem()
            #排名
            rank = li.xpath('./div[1]/i/text()').extract()[0]
            item['rank'] = rank
            # #美剧名称
            title = li.xpath('./h5/a/text()').extract()[0]
            item['title'] = title
            # #状态
            state = li.xpath('./span/font/text()').extract()[0]
            item['state'] = state
            #小分类
            subclass = li.xpath('./span[2]/text()').extract()
            item['subclass'] = subclass
            # #电视台
            tv = li.xpath('./span[3]/text()').extract()[0]
            item['tv'] = tv
            # #更新时间
            updatetime = li.xpath('./div[2]//text()').extract()[0]
            item['updatetime'] = updatetime
            #详情页url
            href = li.xpath('./h5/a/@href').extract()[0]
            detail_url = response.urljoin(href)
            item['detail_url'] = detail_url

            # print(item)

            yield scrapy.Request(url=detail_url,callback=self.detail_parse,meta={'data':item},dont_filter=False)

    def detail_parse(self, response):
        item = response.meta.get('data')
        li_list = response.xpath('//div[@class="o_r_contact"]/ul/li')
        # print('===========================================')

        # 原名
        oldname = li_list[1].xpath('.//text()').extract()
        item['oldname'] = oldname

        # 别名
        alias = li_list[2].xpath('.//text()').extract()
        item['alias'] = alias
        # 编剧
        scriptwriter = li_list[2].xpath('.//text()').extract()
        item['scriptwriter'] = scriptwriter
        # 导演
        director = li_list[3].xpath('.//text()').extract()
        item['director'] = director
        # 主演
        star = li_list[4].xpath('.//text()').extract()
        item['star'] = star
        # 首播时间
        onetime = li_list[5].xpath('.//text()').extract()
        item['onetime'] = onetime

        yield item