# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class Product(scrapy.Item):
    url = scrapy.Field()
    id = scrapy.Field()
    category = scrapy.Field()
    name = scrapy.Field()
    image_urls = scrapy.Field()
    price = scrapy.Field()
    review_num = scrapy.Field()
    brand = scrapy.Field()
    rating = scrapy.Field()
    department = scrapy.Field()

class FailedItem(scrapy.Item):
    url = scrapy.Field()
    reason = scrapy.Field()