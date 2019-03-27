# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MyscrapyItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    adress = scrapy.Field()

class QSBKItem(scrapy.Item):
    # define the fields for your item here like:
    username = scrapy.Field()
    content = scrapy.Field()

class BossItem(scrapy.Item):
    # define the fields for your item here like:
    position = scrapy.Field()
    address = scrapy.Field()
    salary = scrapy.Field()
    name = scrapy.Field()
    info = scrapy.Field()
    full_url = scrapy.Field()
    jobfun = scrapy.Field()
    company = scrapy.Field()


class YouBianItem(scrapy.Item):
    # define the fields for your item here like:
    address = scrapy.Field()
    url = scrapy.Field()

class TenCentItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    type1 = scrapy.Field()
    nub = scrapy.Field()
    address = scrapy.Field()
    time = scrapy.Field()
    full_url = scrapy.Field()
    duty = scrapy.Field()
    skill = scrapy.Field()


class MeiJuItem(scrapy.Item):
    # define the fields for your item here like:
    rank = scrapy.Field()
    title = scrapy.Field()
    state = scrapy.Field()
    subclass = scrapy.Field()
    tv = scrapy.Field()
    updatetime = scrapy.Field()
    detail_url = scrapy.Field()

    oldname = scrapy.Field()
    alias = scrapy.Field()
    scriptwriter = scrapy.Field()
    director = scrapy.Field()
    star = scrapy.Field()
    onetime = scrapy.Field()

class TongJiItem(scrapy.Item):
    # define the fields for your item here like:
    pro_name = scrapy.Field()
    pro_url = scrapy.Field()

    city_code = scrapy.Field()
    city_name = scrapy.Field()
    city_url = scrapy.Field()

    county_code = scrapy.Field()
    county_name = scrapy.Field()
    county_url = scrapy.Field()

    town_code = scrapy.Field()
    town_name = scrapy.Field()
    town_url = scrapy.Field()

    village_code1 = scrapy.Field()
    village_code2 = scrapy.Field()
    village_name = scrapy.Field()

class TaocheItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    detail_url = scrapy.Field()
    price = scrapy.Field()
    f_pay = scrapy.Field()
    m_pay = scrapy.Field()
    reg_tim = scrapy.Field()
    tab_mil = scrapy.Field()
    disp_trans = scrapy.Field()
    sale_city = scrapy.Field()