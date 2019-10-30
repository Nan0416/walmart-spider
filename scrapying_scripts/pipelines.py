# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from scrapying_scripts.items import Product, FailedItem
from scrapy.exporters import JsonItemExporter
import pymongo

class SaveProductToFile(object):
    file = None
    def open_spider(self, spider):
        self.file = open('./walmart_products/%s.json' % spider.filename, 'wb')
        self.exporter = JsonItemExporter(self.file, indent=4)
        self.exporter.start_exporting()

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

class SaveProductToMongoDB(object):
    
    @classmethod
    def from_crawler(cls, crawler):
        db_config = crawler.settings.get('DB')
        # print(db_config)
        cls.DB_URL = db_config.get('MONGO_DB_URI')
        cls.DB_NAME = db_config.get('MONGO_DB_NAME')
        cls.COLLECTION_NAME = db_config.get('COLLECTION_NAME')
        return cls()

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.DB_URL)
        self.db = self.client[self.DB_NAME]
        self.collection = self.db[self.COLLECTION_NAME]
        self.collection.create_index([('id', pymongo.ASCENDING)], unique=True)

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        if isinstance(item, Product):
            product = dict(item)
            try:
                self.collection.insert_one(product)
            except pymongo.errors.DuplicateKeyError:
                print('Duplicated: ' + item.get('id'))
                print(item.get('url'))
        return item
    
class SaveFailedProductToMongoDB(object):
    @classmethod
    def from_crawler(cls, crawler):
        db_config = crawler.settings.get('DB')
        # print(db_config)
        cls.DB_URL = db_config.get('MONGO_DB_URI')
        cls.DB_NAME = db_config.get('MONGO_DB_NAME')
        cls.COLLECTION_NAME = db_config.get('FAILED_ITEM_COLLECTION_NAME')
        return cls()

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.DB_URL)
        self.db = self.client[self.DB_NAME]
        self.collection = self.db[self.COLLECTION_NAME]
        self.collection.create_index([('url', pymongo.ASCENDING)], unique=True)

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        if isinstance(item, FailedItem):
            product = dict(item)
            try:
                self.collection.insert_one(product)
            except pymongo.errors.DuplicateKeyError:
                pass
        return item
    
