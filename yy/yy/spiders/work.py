# -*- coding: utf-8 -*-
import scrapy
import re
from yy.items import TaskItem
from selenium import webdriver

class WorkSpider(scrapy.Spider):
    name = 'work'

    allowed_domains = ['mofcom.gov.cn']


    start_urls = ['http://liyangzhe.mofcom.gov.cn/article/activities/',
                  'http://liyangzhe.mofcom.gov.cn/article/speeches/',
                  'http://wangbingnan.mofcom.gov.cn/article/activities/',
                  'http://wangbingnan.mofcom.gov.cn/article/speeches/',
                  'http://lichenggang.mofcom.gov.cn/article/activities/',
                  'http://renhongbin.mofcom.gov.cn/article/activities/'
                  ]
    for p in range(2, 4):
        liyangzhe_url = 'http://liyangzhe.mofcom.gov.cn/article/activities/?{}'.format(p)
        start_urls.append(liyangzhe_url)
    for p in range(2, 6):
        wangbingnan_url = 'http://wangbingnan.mofcom.gov.cn/article/activities/?{}'.format(p)
        start_urls.append(wangbingnan_url)

    for p in range(2, 5):
        lichenggang_url = 'http://lichenggang.mofcom.gov.cn/article/activities/?{}'.format(p)
        start_urls.append(lichenggang_url)

    for p in range(2, 3):
        renhongbin_url = 'http://renhongbin.mofcom.gov.cn/article/activities/?{}'.format(p)
        start_urls.append(renhongbin_url)


    def parse(self, response):
        li_list = response.xpath('//ul[@class="list-ul tol m-t-6"]/li').extract()

        for li in li_list:
            try:
                item = TaskItem()
                #获取标题
                title = re.findall('<a.*?>(.*?)</a>',li)
                #获取发布时间
                publish_time = re.findall('<span>(.*?)</span>',li)
                #获取文章链接
                detail_url = re.findall('.*? href="(.*?)".*?',li)

                if title:
                    item['title'] = title[0]
                    item['publish_time'] = publish_time[0]


                if detail_url:
                    detail_url = response.urljoin(detail_url[0])
                    item['detail_url'] = detail_url


                yield scrapy.Request(url=detail_url, callback=self.detail_parse, meta={'data': item}, dont_filter=False)
            except:
                pass


    def detail_parse(self, response):


        item = response.meta.get('data')

        driver = webdriver.PhantomJS(executable_path=r'd:\Desktop\phantomjs-2.1.1-windows\bin\phantomjs.exe')
        driver.get(url=response.url)
        # with open('work.html','a',encoding='utf-8')as f:
        #     f.write(driver.page_source)
        organization = re.findall('var source = "(.*?)"',driver.page_source)

        content = response.xpath('//div[@id="zoom"]/p/text()').extract()
        if content == []:
            item['content'] = '没有内容'
            item['abstract'] = '没有摘要'
        else:
            content = ''.join(content[0])
            item['content'] = content

            abstract = content[:20]
            item['abstract'] = abstract

        crawl_time = '2019年3月12日'
        item['crawl_time'] = crawl_time

        classify = 1
        item['classify'] = classify

        item['organization'] = organization[0]

        keyword = re.findall('http://(.*?)\.mofcom.gov.cn',response.url)
        item['keyword'] = keyword[0]

        yield item



