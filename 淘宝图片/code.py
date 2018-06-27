 #! /usr/bin/env python
# coding: utf-8

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pyquery import PyQuery as pq
from pymongo import MongoClient
import re



browser = webdriver.Chrome()
wait = WebDriverWait(browser,10)  #指定一个最长等待时间

# client = MongoClient('mongodb://127.0.0.2:27017')
# db = client['taobao']
# collection = db['taobao']


def search_keyword(keyword="美食"):
    '''
    搜索关键字
    :param keyword:
    :return:
    '''
    try:
        browser.get('https://www.taobao.com/')
        inputbox = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#q')))
        button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#J_TSearchForm  div.search-button  button')))
        inputbox.clear()
        inputbox.send_keys(keyword)
        button.click()

        totalPages = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-pager  div  div div div.total'))).text
        totalPages = re.search('(\d+)', totalPages).group(1)
        # print(totalPages)
        return totalPages

    except TimeoutException:
        return search_keyword(keyword)


def index_page(page):
    '''
    抓取索引页
    :param page:
    :return:
    '''
    print('正在抓取第',page,'页')

    try:
        if page > 1:
            input = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-pager div.form > input')))    #presence_of_element_located：节点加载出来，传入定位元组
            submit = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, '#mainsrp-pager div.form > span.btn.J_Submit')))  #element_to_be_clickable：节点可点击
            input.clear()
            input.send_keys(page)
            submit.click()
        wait.until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#mainsrp-pager li.item.active > span'), str(page)))  #验证当前查询的页数是否和真实显示的页数一致
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.m-itemlist .items .item')))
        get_products()
    except TimeoutException:
        index_page(page)


#往mangoDB中存储
def save_to_mongo(result):

    if collection.insert(result):
        print('Saved to Mongo',result)



def  get_products():
    '''
    提取商品数据
    :return:
    '''
    html = browser.page_source   #返回网页源码

    doc = pq(html)
    items = doc('#mainsrp-itemlist .items .item').items()  #items()方法是对每个节点进行遍历
    for item in items:
        product = {
            'image': 'http' + item.find('.pic .img').attr('data-src').strip(),  #attr()方法来获取属性
            'price': item.find('.price').text().strip(),
            'deal': item.find('.deal-cnt').text().strip(),
            'title': item.find('.title').text().strip(),
            'shop': item.find('.shop').text().strip(),
            'location': item.find('.location').text().strip()
        }
        print (product)
        # save_to_mongo(product)


def main():
    '''
    每一页进行遍历
    :return:
    '''
    # for i in range(1,21):
    #     index_page(i)
    # browser.close()
    p = input('请输入需要查询的内容 or q退出:').strip()
    if p == 'q':exit()
    total = int(search_keyword(p))
    print('total:',total,'页')
    page = int(input('请输入页数:').strip())
    if page <= total:
        for i in range(1,page+1):
            index_page(i)
    else:
        for i in range(1,total+1):
            index_page(i)
    browser.close()




if __name__ == '__main__':
    main()