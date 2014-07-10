# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Show(scrapy.Item):
    id = scrapy.Field()
    title = scrapy.Field()
    desc = scrapy.Field()
    airday = scrapy.Field()
    startdate = scrapy.Field()
    #convention for images pipeline
    image_urls = scrapy.Field()
    images = scrapy.Field()
