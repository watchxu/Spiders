#! /usr/bin/env python
# *_*coding:utf-8 *_*

from urllib import request, parse
import json

#有道翻译

while True:
    content = input('请输入需要查询的信息(输入"q"退出程序):')
    if content == 'q':
        break
    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
    body = {
        'i': content,
        'from': 'AUTO',
        'to': 'AUTO',
        'smartresult': 'dict',
        'client': 'fanyideskweb',
        'salt': '1523603391464',
        'sign': '47cbbefab4e9dc042e0aebd695b2236e',
        'doctype': 'json',
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_REALTIME',
        'typoResult': 'false'
    }

    data = bytes(parse.urlencode(body), encoding='utf8')
    req = request.Request(url=url, data=data, method='POST')
    req.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36)')
    response = request.urlopen(req)
    tag = response.read().decode('utf-8')
    tag = json.loads(tag)
    print("翻译结果: %s" % (tag['translateResult'][0][0]['tgt']))
