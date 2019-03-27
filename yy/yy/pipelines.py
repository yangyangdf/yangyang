# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
class WorkPipeline(object):
    def __init__(self):
        self.client = pymongo.MongoClient('localhost')
        self.db = self.client['yy']
        self.work = self.db['work']

    def process_item(self, item, spider):

        self.work.insert(dict(item))

        return item


class WorkPhotoPipeline(object):
    def __init__(self):
        print('==============================')
        self.client = pymongo.MongoClient('localhost')
        self.db = self.client['yy']
        self.work = self.db['work']

    def process_item(self, item, spider):
        self.work.insert(dict(item))
        print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        return item