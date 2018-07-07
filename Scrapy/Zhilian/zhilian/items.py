# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhilianItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    city = scrapy.Field()
    companyLogo = scrapy.Field()
    createDate = scrapy.Field()
    eduLevel = scrapy.Field()
    emplType = scrapy.Field()
    endDate = scrapy.Field()
    positionURL = scrapy.Field()
    salary = scrapy.Field()
    updateDate = scrapy.Field()
    welfare = scrapy.Field()
    workingExp = scrapy.Field()


