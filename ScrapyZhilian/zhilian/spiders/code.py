# -*- coding: utf-8 -*-
import scrapy
from urllib import parse
import json
from zhilian.items import ZhilianItem

class CodeSpider(scrapy.Spider):
    name = 'code'
    allowed_domains = ['sou.zhaopin.com']


    def parse(self, response):
        result = json.loads(response.text)
        if result.get("data"):
            results = result["data"]["results"]
            for i in results:
                item = ZhilianItem()
                item["city"] = i["city"]
                item["companyLogo"] = i["companyLogo"]
                item["createDate"] = i["createDate"]
                item["eduLevel"] = i["eduLevel"]
                item["emplType"] = i["emplType"]
                item["endDate"] = i["endDate"]
                item["positionURL"] = i["positionURL"]
                item["salary"] = i["salary"]
                item["updateDate"] = i["updateDate"]
                item["welfare"] = i["welfare"]
                item["workingExp"] = i["workingExp"]
                yield item




    def start_requests(self):
        base_url = "https://fe-api.zhaopin.com/c/i/sou?"

        for start in [0,60]:
            data = {
                "start":str(start),
                "pageSize":"60",
                "cityId":"530",
                "workExperience": "-1",
                "education": "-1",
                "companyType": "-1",
                "employmentType": "-1",
                "jobWelfareTag": "-1",
                "kw": "python爬虫",
                "kt": "3"
            }
            url = base_url + parse.urlencode(data)
            yield scrapy.FormRequest(url,method="GET",callback=self.parse)