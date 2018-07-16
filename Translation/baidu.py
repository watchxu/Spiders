from urllib import request, parse
import json

#百度翻译

while True:
    content = input('请输入需要查询的信息(输入"q"退出程序):')
    if content == 'q':
        break
    url = 'http://fanyi.baidu.com/sug'
    # body = {
    #     'from': 'en',
    #     'to': 'zh',
    #     'query': content,
    #     'transtype': 'translang',
    #     'simple_means_flag': '3',
    #     'sign': '54706.276099',
    #     'token': '9757aaf831a612059b098899d4541038'
    # }
    body = {
        'kw': content
    }
    data = bytes(parse.urlencode(body), encoding='utf8')
    req = request.Request(url=url, data=data, method='POST')
    req.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36')
    response = request.urlopen(req)
    tag = response.read().decode('utf-8')
    tag = json.loads(tag)

    print(tag['data'][0]['v'])
