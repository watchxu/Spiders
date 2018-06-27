#! /usr/bin/env python
# coding: utf-8

import requests
import os
from hashlib import md5
from multiprocessing.pool import Pool

headers = {

    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',

}



def get_pase(url,offset):

    params = {
        'offset':offset,
        'format':'json',
        'keyword':'街拍',
        'autoload':'true',
        'count':'20',
        'cur_tab':'1',
        'from':'search_tab'
    }

    response = requests.get(url,headers=headers,params=params)
    try:
        if response.status_code == 200:
            return response.json()

    except Exception as e:
        print(e.args)

def get_images(json):
    if json:
        items = json.get('data')
        for item in items:
            title = item.get('title')
            images_list = item.get('image_list')
            if images_list:
                for image in images_list:
                    yield {
                        'title': title,
                        'images': 'http:' + image.get('url')
                    }


def save_image(item):
    if not os.path.exists(item.get('title')):
        os.mkdir(item.get('title'))
    try:

        image_url = item.get('images')
        new_image_url = image_url.replace('list','large')
        response = requests.get(new_image_url)
        if response.status_code == 200:
            file_path = '{0}/{1}.{2}'.format(item.get('title'), md5(response.content).hexdigest(), 'jpg')
            if not os.path.exists(file_path):
                with open(file_path, 'wb')as f:
                    f.write(response.content)
            else:
                print('Already Downloaded', file_path)
    except requests.ConnectionError:
        print('Failed to save image')


def main(offset):
    url = 'https://www.toutiao.com/search_content/'
    json = get_pase(url,offset)
    for item in get_images(json):
        print('\033[32;1m%s\033[0m' % item)
        save_image(item)

GROUP_START = 1
GROUP_END = 5

if __name__ == '__main__':
    pool = Pool()
    groups = ([x * 20 for x in range(GROUP_START, GROUP_END + 1)])
    pool.map(main, groups)
    pool.close()
    pool.join()