# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json

class MyscrapyPipeline(object):
    def process_item(self, item, spider):
        f = open('maoyan.json','a',encoding='utf-8')

        json.dump(dict(item),f,ensure_ascii=False)

        return item

class QSBKPipeline(object):
    def process_item(self, item, spider):
        f = open('qiushibaike.json','a',encoding='utf-8')

        json.dump(dict(item),f,ensure_ascii=False)

        return item

class BossPipeline(object):
    def process_item(self, item, spider):
        f = open('Boss.json','a',encoding='utf-8')

        json.dump(dict(item),f,ensure_ascii=False)

        return item

class YouBianPipeline(object):
    def process_item(self, item, spider):
        f = open('YouBian.json','a',encoding='utf-8')

        json.dump(dict(item),f,ensure_ascii=False)

        return item

class TenCentPipeline(object):
    def process_item(self, item, spider):
        f = open('TenCent.json','a',encoding='utf-8')

        json.dump(dict(item),f,ensure_ascii=False)

        return item

class MeiJuPipeline(object):
    def process_item(self, item, spider):
        f = open('MeiJu.json', 'a', encoding='utf-8')
        json.dump(dict(item), f, ensure_ascii=False)
        return item

class TongJiPipeline(object):
    def process_item(self, item, spider):
        f = open('TongJi.json', 'a', encoding='gbk')
        json.dump(dict(item), f, ensure_ascii=False)
        return item

import pymongo

class TaochePipeline(object):
    def __init__(self):
        self.client = pymongo.MongoClient('localhost')
        self.db = self.client['taoche']
        self.car_info = self.db['car_info']
        print('======================')

    def process_item(self, item, spider):
        print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')

        self.car_info.insert(dict(item))

        return item
