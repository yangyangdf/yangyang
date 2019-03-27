# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TaskItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()          #标题
    content = scrapy.Field()        #正文
    abstract = scrapy.Field()       #摘要
    publish_time = scrapy.Field()   #发布时间
    crawl_time = scrapy.Field()     #爬虫时间
    classify = scrapy.Field()       #归类
    organization = scrapy.Field()   #信源
    detail_url = scrapy.Field()     #url地址
    keyword = scrapy.Field()        #关键字--可用人工标注后的

