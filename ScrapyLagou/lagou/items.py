# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LagouItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    city = scrapy.Field()
    companyFullName = scrapy.Field()
    companyLabelList = scrapy.Field()
    companySize = scrapy.Field()
    createTime = scrapy.Field()
    district = scrapy.Field()
    education = scrapy.Field()
    financeStage = scrapy.Field()
    firstType = scrapy.Field()
    formatCreateTime = scrapy.Field()
    industryLables = scrapy.Field()
    jobNature = scrapy.Field()
    lastLogin = scrapy.Field()
    linestaion = scrapy.Field()
    positionAdvantage = scrapy.Field()
    positionName = scrapy.Field()
    salary = scrapy.Field()
    workYear = scrapy.Field()
    url = scrapy.Field()


