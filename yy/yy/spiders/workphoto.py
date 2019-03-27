# -*- coding: utf-8 -*-
import scrapy
from yy.items import TaskItem
from selenium import webdriver
import re
from lxml import etree


class WorkphotoSpider(scrapy.Spider):
    name = 'workphoto'
    allowed_domains = ['mofcom.gov.cn']
    start_urls = ['http://liyangzhe.mofcom.gov.cn/article/collection/',
                  'http://wangbingnan.mofcom.gov.cn/article/collection/',
                  'http://lichenggang.mofcom.gov.cn/article/collection/',
                  'http://renhongbin.mofcom.gov.cn/article/collection/',
                  ]
    for p in range(2,6):
        wangbingnan_url = 'http://wangbingnan.mofcom.gov.cn/article/collection/?{}'.format(p)
        start_urls.append(wangbingnan_url)

    for p in range(2,5):
        lichenggang_url = 'http://lichenggang.mofcom.gov.cn/article/collection/?{}'.format(p)
        start_urls.append(lichenggang_url)

    for p in range(2,3):
        renhongbin_url = 'http://renhongbin.mofcom.gov.cn/article/collection/?{}'.format(p)
        start_urls.append(renhongbin_url)


    def parse(self, response):


        info_list = response.xpath('//table[@class="category"]//td')

        for info in info_list:
            item = TaskItem()
            # #图片集锦详情页url
            info_url = info.xpath('./p/a/@href').extract()[0]
            info_url = response.urljoin(info_url)
            item['detail_url'] = info_url
            # 图片集锦详情页title
            info_title = info.xpath('./p/a/text()').extract()[0]
            item['title'] = info_title

            yield scrapy.Request(url=info_url,callback=self.info_parse,meta={'data':item},dont_filter=False)

    def info_parse(self,response):
        driver = webdriver.PhantomJS(executable_path=r'd:\Desktop\phantomjs-2.1.1-windows\bin\phantomjs.exe')

        driver.get(url=response.url)

        organization = re.findall('var source = "(.*?)"',driver.page_source)
        publish_time = re.findall('var tm = "(.*?)"',driver.page_source)


        item = response.meta.get('data')
        content = response.xpath('//div[@id="zoom"]/p[last()]/text()').extract()

        if content == []:
            item['content'] = '没有内容'
            item['abstract'] = '没有摘要'
        else:
            item['content'] = content[0]
            abstract = content[:-20]
            item['abstract'] = abstract

        item['publish_time'] = publish_time[0]

        crawl_time = '2019年3月12日'
        item['crawl_time'] = crawl_time

        classify = 1
        item['classify'] = classify

        item['organization'] = organization[0]

        keyword = re.findall('http://(.*?)\.mofcom.gov.cn', response.url)
        item['keyword'] = keyword[0]

        yield item

