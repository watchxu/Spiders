#抓取猫眼热映口碑榜
import json
import requests
from requests.exceptions import RequestException
from lxml import etree
import time

#抓取首页
def get_one_page(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None

def parse_html(html):
    html = etree.HTML(html)
    result = html.xpath('//dl[@class="board-wrapper"]/dd')

    for line in result:
        id = line.xpath('i/text()')
        title = line.xpath('div/div/div/p/a/@title')
        actor = line.xpath('div/div/div/p[@class="star"]/text()')
        time = line.xpath('div/div/div/p[@class="releasetime"]/text()')
        for i in actor:
            actor = i.strip()

        yield {
                'id': id[0],
                'title': title[0],
                'actor': actor,
                'time': time[0][3:],

                    }

def write_to_file(content):
    with open('result.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')


def main():
    url = 'http://maoyan.com/board'
    html = get_one_page(url)
    for item in parse_html(html):
        print(item)
        write_to_file(item)
        time.sleep(1)


if __name__ == '__main__':
    main()