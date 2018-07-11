#! /usr/bin/env python
# *_*coding:utf-8 *_*

import uuid
import requests

path = '/Users/xulei16/Downloads/video/'
url = 'https://api.huoshan.com/hotsoon/item/video/_playback/'
url_list = []

def response(flow):
    url_list.append(flow.request.url)


    for i in url_list:
        if url in i:
            title = uuid.uuid4()
            filename = path + str(title) + '.mp4'
            res = requests.get(i,stream=True)
            with open(filename, 'ab') as f:
                f.write(res.content)

                f.flush()
                print(filename + '下载完成')
                url_list.clear()
