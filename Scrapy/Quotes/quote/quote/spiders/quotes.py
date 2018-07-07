# -*- coding: utf-8 -*-
import scrapy
from quote.items import QuoteItem

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        # print(response.text)  #打印抓取网页源代码
        quotes = response.css('.quote')
        for quote in quotes:
            item = QuoteItem()
            text = quote.css('.text::text').extract_first()  #extract_first获取第一个
            author = quote.css('.author::text').extract_first()
            tags = quote.css('.tags .tag::text').extract()  #类似于find和findall
            item['text'] = text
            item['author'] = author
            item['tags'] = tags
            yield item

        next = response.css('.pager .next a::attr(href)').extract_first()
        url = response.urljoin(next)

        yield scrapy.Request(url=url, callback=self.parse)