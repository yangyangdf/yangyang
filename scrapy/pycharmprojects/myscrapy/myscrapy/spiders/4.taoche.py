# -*- coding: utf-8 -*-
import scrapy
from myscrapy.spiders.city import CAR_NAME_LIST,CITY_NAME_LIST
from myscrapy.items import TaocheItem

class CitySpider(scrapy.Spider):
    name = 'city'
    allowed_domains = ['taoche.com']
    start_urls = []

    for city in CITY_NAME_LIST:
        for car in CAR_NAME_LIST:
            url = 'https://{}.taoche.com/{}/'.format(city,car)
            start_urls.append(url)

    def parse(self, response):
        max_page = response.xpath('//div[@class="paging-box the-pages"]/div//a[last()-1]/text()').extract()
        print(max_page)
        if max_page == []:
            page = 1
        else:
            page = int(max_page[0])
        for p in range(1, page + 1):
            url = response.url + '?page={}#pagetag'.format(p)
            yield scrapy.Request(url=url, callback=self.list_parse, dont_filter=False)

    def list_parse(self, response):
        car_ul = response.xpath('//div[@id="carlist"]/div[@id="container_base"]//li')
        for li in car_ul:
            item = TaocheItem()
            title = li.xpath('./div[2]/a/span/text()').extract()[0]
            item['title'] = title
            detail_url = 'https:' + li.xpath('./div[2]/a/@href').extract()[0]
            item['detail_url'] = detail_url
            yield scrapy.Request(url=detail_url, callback=self.detail_parse, meta={'data': item}, dont_filter=False)

    def detail_parse(self, response):
        item = response.meta['data']
        # def parse(self, response):
        #     item = TaocheItem()
        price = \
        response.xpath('//div[@class="detail-summary"]//div[@class="summary-price-wrap"]/strong/text()').extract()[0]
        f_pay = response.xpath(
            '//div[@class="detail-summary"]//div[@class="price-zhuans"]/span[1]/b/text()').extract_first()
        m_pay = response.xpath(
            '//div[@class="detail-summary"]//div[@class="price-zhuans"]/span[2]/b/text()').extract_first()
        reg_tim = \
        response.xpath('//div[@class="detail-summary"]//div[@class="summary-attrs"]/dl[1]/dd/text()').extract()[0]
        tab_mil = \
        response.xpath('//div[@class="detail-summary"]//div[@class="summary-attrs"]/dl[2]/dd/text()').extract()[0]
        disp_trans = \
        response.xpath('//div[@class="detail-summary"]//div[@class="summary-attrs"]/dl[3]/dd/text()').extract()[0]
        sale_city = \
        response.xpath('//div[@class="detail-summary"]//div[@class="summary-attrs"]/dl[4]/dd/text()').extract()[0]
        item['price'] = price + '万'
        item['f_pay'] = f_pay
        item['m_pay'] = m_pay
        item['reg_tim'] = reg_tim
        item['tab_mil'] = tab_mil
        item['disp_trans'] = disp_trans
        item['sale_city'] = sale_city
        yield item
        # base_info=response.xpath('//div[@class="row  details-information-list"]//text()').extract()
        # para_config=response.xpath('//div[@class="hide-box"]/div[2]//text()').extract()

