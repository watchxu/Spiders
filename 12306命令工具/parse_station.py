#! /usr/bin/env python
# *_*coding:utf-8 *_*

import re
import requests
from pprint import pprint


def main():
    url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9058'
    r = requests.get(url)
    pattern = u'([\u4e00-\u9fa5]+)\|([A-Z]+)'  #[\u4e00-\u9fa5]表示匹配任何中文字符
    result = dict(re.findall(pattern,r.text))
    # print(result.keys())
    # print(result.values())
    return result

if __name__ == '__main__':
    main()