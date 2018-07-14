#! /usr/bin/env python
# *_*coding:utf-8 *_*

import requests
import json
from pymongo import MongoClient
import time

client = MongoClient('mongodb://127.0.0.1:27017')
db = client['kuaishou']
collection = db['kuaishou']

class Parse(object):
    def __init__(self,url,currentPage,gameId,pageSize,type):
        self.url = url
        self.currentPage = currentPage
        self.gameId = gameId
        self.pageSize = pageSize
        self.type = type

    def parse_json(self):
        body = {
            "currentPage" : self.currentPage,
            "gameId": self.gameId,
            "pageSize": self.pageSize,
            "type": self.type
        }
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
            "Host": "live.kuaishou.com",
            "Referer": "https://live.kuaishou.com/cate/DQRM/1001"
        }

        response = requests.post(url=self.url,data=json.dumps(body),headers=headers)
        result = json.loads(response.text)
        if result.get("list"):
            for item in result.get("list"):
                yield {
                    "title" : item.get("title"),   #主播的title
                    "gameName": item.get("gameName"),  #抓取的游戏名称
                    "playUrls": item.get("playUrls"),  #直播地址，分别有标清、高清、超清
                    "user": item.get("user"),  #主播的一些基本信息
                    "watchingCount": item.get("watchingCount")  #观看人数
                }

    def save_to_mongo(self,result):

        if collection.insert_one(result):
            print('Saved to Mongo', result)





if __name__ == '__main__':
    url = "https://live.kuaishou.com/liveStream/liveCardList"
    gameId = "1001"
    pageSize = "60"
    type = "DQRM"
    page = input("请输入需要抓取的页数:").strip()
    for index in range(1, int(page) + 1):
        print("开始抓取第%s页" % index)
        currentPage = str(index)
        results = Parse(url, currentPage, gameId, pageSize, type)
        for result in results.parse_json():
            print(result)
            results.save_to_mongo(result)
            time.sleep(1)