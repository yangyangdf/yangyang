# -*- coding: utf-8 -*-
import scrapy
from myscrapy.items import BossItem

class BossSpider(scrapy.Spider):
    name = 'boss'
    allowed_domains = ['zhipin.com']
    start_urls = []

    base_url = 'https://www.zhipin.com/c101010100/?query=python&page=%d'

    for page in range(1,10):
        url = base_url%page
        start_urls.append(url)

    def parse(self, response):

        position_list = response.xpath('//div[@class="job-list"]/ul/li')

        for p in position_list:
            item = BossItem()

        ##岗位名称：
            position = p.xpath('.//div[@class="job-title"]/text()').extract()[0]
            item['position'] = position
        #工作地址：
            address = p.xpath('.//div[@class="info-primary"]/p/text()').extract()[0]
            item['address'] = address
        #薪水：
            salary = p.xpath('.//span[@class="red"]/text()').extract()[0]
            item['salary'] = salary
        #公司名称：
            name = p.xpath('.//div[@class="company-text"]//h3[@class="name"]/a/text()').extract()[0]
            item['name'] = name
        #公司信息：
            info = p.xpath('.//div[@class="company-text"]//p//text()').extract()
            item['info'] = info
        #详情页：
            detail_url = p.xpath('.//div[@class="info-primary"]/h3/a/@href').extract()[0]
            url = 'https://www.zhipin.com'
            full_url = url + detail_url
            item['full_url'] = full_url

            yield scrapy.Request(url = full_url,callback=self.parse_detail,meta={'data':item})

    def parse_detail(self,response):
        item = response.meta.get('data')

        content = response.xpath('//div[@class="detail-content"]')

        jobfun = content.xpath('./div[1]//text()').extract()
        company = content.xpath('./div[3]//text()').extract()

        jobfun = ''.join(jobfun)
        company = ''.join(company)


        item['jobfun'] = jobfun
        item['company'] = company

        yield item



