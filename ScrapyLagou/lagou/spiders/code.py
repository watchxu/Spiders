# -*- coding: utf-8 -*-
import scrapy
from urllib import parse
from lagou.items import LagouItem
import json
import time




class CodeSpider(scrapy.Spider):
    name = 'code'
    allowed_domains = ['www.lagou.com']



    def parse(self, response):
        result = json.loads(response.text)
        if result.get("content"):
        # print(result)
            results = result["content"]["positionResult"]["result"]
            for id in results:
                item = LagouItem()
                item['city'] = id.get("city")
                item['companyFullName'] = id.get("companyFullName")
                item['companyLabelList'] = id.get("companyLabelList")
                item['companySize'] = id.get("companySize")
                item['createTime'] = id.get("createTime")
                item['district'] = id.get("district")
                item['education'] = id.get("education")
                item['financeStage'] = id.get("financeStage")
                item['firstType'] = id.get("firstType")
                item['formatCreateTime'] = id.get("formatCreateTime")
                item['industryLables'] = id.get("industryLables")
                item['jobNature'] = id.get("jobNature")
                item['lastLogin'] = id.get("lastLogin")
                item['linestaion'] = id.get("linestaion")
                item['positionAdvantage'] = id.get("positionAdvantage")
                item['positionName'] = id.get("positionName")
                item['salary'] = id.get("salary")
                item['workYear'] = id.get("workYear")
                item['url'] = "https://www.lagou.com/jobs/%s.html" % id.get("positionId")
                yield item
        else:
            pass





    def parse_html(self):
        pass


    def start_requests(self):

        base_url = 'https://www.lagou.com/jobs/positionAjax.json?'


        data = {
            "city": "北京",
            "needAddtionalResult":"false"
        }
        url = base_url + parse.urlencode(data)

        for page in range(1,31):
            body = {
                "first": "false",
                "pn": str(page),
                "kd": "python爬虫"
            }

            yield scrapy.FormRequest(url,method="POST",formdata=body,callback=self.parse)







