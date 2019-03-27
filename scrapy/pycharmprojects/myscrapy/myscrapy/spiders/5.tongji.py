# -*- coding: utf-8 -*-
import scrapy
from lxml import etree
import requests
from scrapy.spiders import CrawlSpider, Rule
from myscrapy.items import TongJiItem


class TongjiSpider(scrapy.Spider):
    # name = 'tongji'
    # allowed_domains = ['stats.gov.cn']
    # start_urls = []
    #
    # index_url = 'http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2018/%d.html'
    # for i in range(11,16):
    #     url = index_url%i
    #     try:
    #         if len(requests.request('get',url=url).text)>200:
    #             start_urls.append(url)
    #     except:
    #         pass

    name = 'tongji'
    allowed_domains = ['stats.gov.cn']
    start_urls = ['http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2018/index.html']

    #请求首页所有url
    def parse(self,response):
        content = response.body.decode('gbk')
        pro = etree.HTML(content)
        pro = pro.xpath('//tr[@class="provincetr"]')
        for tr in pro:
            item = TongJiItem()
            #获取首页的省市名称
            prov_name = tr.xpath('./td/a/text()')
            #获取首页的省市base_url
            prov_href = tr.xpath('./td/a/@href')
            for i in range(len(prov_name)):
                pro_name = prov_name[i]
                item['pro_name'] = pro_name
                #获取所有省市url
                pro_url = response.urljoin(prov_href[i])
                item['pro_url'] = pro_url
                yield scrapy.Request(url=pro_url,callback=self.city_parse,meta={'data':item},dont_filter=False)

    #请求所有市的url
    def city_parse(self,response):
        content = response.body.decode('gbk')
        city = etree.HTML(content)
        city = city.xpath('//tr[@class="citytr"]')
        for td in city:
            item = TongJiItem()
            # item = response.meta.get('data')
            #获取所有市的代码号
            city_code = td.xpath('./td[1]/a/text()')
            item['city_code'] = city_code[0]

            #获取所有市的名称
            city_name = td.xpath('./td[2]/a/text()')
            item['city_name'] = city_name[0]
            #获取所有市的baseurl
            city_baseurl = td.xpath('./td[2]/a/@href')
            city_url = response.urljoin(city_baseurl[0])
            item['city_url'] = city_url
            print(city_code)
            print(city_name)
            print(city_url)

            yield scrapy.Request(url=city_url,callback=self.county_parse, meta={'data': item},dont_filter=False)

    #请求所有区的url
    def county_parse(self, response):
        content = response.body.decode('gbk')
        county = etree.HTML(content)
        county = county.xpath('//tr[@class="countytr"]')

        for td in county:
            item = response.meta.get('data')
            #获取所有县的代码号
            county_code = td.xpath('./td[1]/a/text()')
            item['county_code'] = county_code[0]

            #获取所有县的名称
            county_name = td.xpath('./td[2]/a/text()')
            item['county_name'] = county_name[0]
            #获取所有县的baseurl
            county_baseurl = td.xpath('./td[2]/a/@href')
            county_url = response.urljoin(county_baseurl[0])
            item['county_url'] = county_url

            print(county_code)
            print(county_name)
            print(county_url)

            yield scrapy.Request(url=county_url,callback=self.town_parse,meta={'data': item},dont_filter=False)

    def town_parse(self, response):
        content = response.body.decode('gbk')
        town = etree.HTML(content)
        town = town.xpath('//tr[@class="towntr"]')

        for td in town:
            item = response.meta.get('data')
            #获取所有镇的代码号
            town_code = td.xpath('./td[1]/a/text()')
            item['town_code'] = town_code[0]

            #获取所有镇的名称
            town_name = td.xpath('./td[2]/a/text()')
            item['town_name'] = town_name[0]
            #获取所有镇的baseurl
            town_baseurl = td.xpath('./td[2]/a/@href')
            town_url = response.urljoin(town_baseurl[0])
            item['town_url'] = town_url

            print(town_code)
            print(town_name)
            print(town_url)

            yield scrapy.Request(url=town_url,callback=self.village_parse,meta={'data': item},dont_filter=False)

    def village_parse(self, response):
        content = response.body.decode('gbk')
        town = etree.HTML(content)
        town = town.xpath('//tr[@class="villagetr"]')

        for td in town:
            item = response.meta.get('data')
            #获取所有委员会的代码号
            village_code1 = td.xpath('./td[1]/text()')
            item['village_code1'] = village_code1[0]

            #获取所有委员会的城市分类代码
            village_code2 = td.xpath('./td[2]/text()')
            item['village_code2'] = village_code2[0]
            #获取所有委员会的名称
            village_name = td.xpath('./td[3]/text()')
            item['village_name'] = village_name

            print(village_code1)
            print(village_code2)
            print(village_name)

            yield item