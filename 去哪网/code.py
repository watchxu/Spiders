#! /usr/bin/env python
# *_*coding:utf-8 *_*

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pyquery import PyQuery as pq
import time
import re


browser = webdriver.Chrome()
wait = WebDriverWait(browser,10)  #指定一个最长等待时间

def search_keyword(bourn,start_time,end_time):
    try:
        browser.get('http://hotel.qunar.com')
        destination = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"div.city-input input")))
        fromdate = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.data-in.ui-date-in input")))
        todata = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.data-out.ui-date-out input")))
        button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'div.search-btn')))
        destination.clear()
        destination.send_keys(bourn)
        fromdate.clear()
        fromdate.send_keys(start_time)
        todata.clear()
        todata.send_keys(end_time)
        button.click()

    except TimeoutException:
        return search_keyword()

def next(next):
    js = "var q=document.documentElement.scrollTop=100000"
    browser.execute_script(js)
    time.sleep(4)
    print('正在抓取第', next, '页')
    get_products()
    page = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'li.item.next')))
    page.click()



def get_products():
    html = browser.page_source
    # print(html)
    doc = pq(html)
    items = doc('.b_result_box').items()
    for item in items:
        price = item.find('.hotel_price b').text()
        try:
            product = {
                "title": item.find('.hotel_item a').text(),
                "price": re.search('^[0-9]+', price).group() + "￥",
                "grade": item.find('.score b').text()
            }
        except AttributeError:
            product = {
                "title": item.find('.hotel_item a').text(),
                "price": "售罄" + "￥",
                "grade": item.find('.score b').text()
            }
        print(product)


def main():
    bourn = input("请输入目的地:").strip()
    start_time = input("请输入入住时间:").strip()
    end_time = input("请输入离店时间:").strip()
    page = input("请输入抓取的页数:")
    search_keyword(bourn,start_time,end_time)
    for i in range(1,int(page)+1):
        next(i)
        time.sleep(2)

if __name__ == '__main__':
    main()