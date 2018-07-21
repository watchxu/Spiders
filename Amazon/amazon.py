#! /usr/bin/env python
# *_*coding:utf-8 *_*

import requests
from pyquery import PyQuery as pq
import re

def get_html(page,goods):
    print("Start grabbing the %s page" % page)
    url = 'https://www.amazon.cn/s/ref=nb_sb_noss_1'
    params = {
        "__mk_zh_CN": "亚马逊网站",
        "url": "search-alias=aps",
        "field-keywords": goods,
        "page": page
    }
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
        "Referer": "https://www.amazon.cn/",
        "Host": "www.amazon.cn"
    }

    res = requests.get(url,params=params,headers=headers)
    html = res.text
    return html

def parse(html):
    doc = pq(html)
    items = doc("#s-results-list-atf li").items()
    a = 0
    for item in items:

        r = '\￥[0-9]\d?\,[0-9]\d+\.[0-9]\d+|\￥[0-9]\d+\.[0-9]\d+'
        price = re.findall(r,item.find("div .a-link-normal span").text())
        if price != []:
            result = {
                "image": item.find(".a-link-normal img").attr("src"),
                "title": item.find(".a-link-normal img").attr("alt"),
                "price": price[0]
            }
            if result.get("image") == None:
                continue
            else:
                print(result)

def main():
    goods = input("Please enter the item you want to grab:").strip()
    pages = input("Number of pages seized:").strip()
    for page in range(1,int(pages)+1):
        html = get_html(page,goods)
        parse(html)


if __name__ == '__main__':
    main()
