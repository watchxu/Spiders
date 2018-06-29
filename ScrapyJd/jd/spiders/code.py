# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
import json
from jd.items import JdItem

class CodeSpider(scrapy.Spider):

    name = 'code'
    allowed_domains = ['search.jd.com/Search?keyword=ipad']
    page = 1
    url = 'http://search.jd.com/Search?keyword=ipad&page='
    start_urls = [url + str(page)]



    def parse(self, response):
        items = response.css('.gl-warp.clearfix > li.gl-item')
        for item in items:
            dic = JdItem()
            name = item.css('.p-name a i::text').extract_first()
            image = item.css('.p-img a img::attr(source-data-lazy-img)').extract_first()
            price = item.css('.p-price i::text').extract_first()
            deal = item.css('.p-commit strong a::text').extract_first()
            shop = item.css('.p-shop a::text').extract_first()
            dic['name'] = name
            dic['image'] = image
            dic['price'] = price
            dic['deal'] = deal
            dic['shop'] = shop
            yield dic


        # for page in range(2,101):
        #     url = self.start_urls[0] + '&page=%s' % page
        #
        #     yield scrapy.Request(url=url, callback=self.parse)
        if self.page <= 100:
            self.page += 1
            yield scrapy.Request(self.url+str(self.page),callback=self.parse,dont_filter = True)
