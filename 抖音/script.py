#! /usr/bin/env python
# -*- coding: utf-8 -*-

from appium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait

class Action():
   def __init__(self):
      # 初始化配置，设置Desired Capabilities参数
      self.desired_caps = {
         "platformName": "Android",
         "deviceName": "meizu_MA5",
         "appPackage": "com.ss.android.ugc.aweme",
         "appActivity": ".main.MainActivity"
      }
      # 指定Appium Server
      self.server = 'http://localhost:4723/wd/hub'
      # 新建一个Session
      self.driver = webdriver.Remote(self.server, self.desired_caps)
      # 设置滑动初始坐标和滑动距离
      self.start_x = 360
      self.start_y = 900
      self.distance = 600

   def comments(self):
      sleep(3)
      # app开启之后点击一次屏幕，确保页面的展示
      self.driver.tap([(360, 900)],500)

   def scroll(self):
      # 无限滑动
      while True:
         # 模拟滑动
         self.driver.swipe(self.start_x, self.start_y, self.start_x,
                           self.start_y - self.distance)
         # 设置延时等待
         sleep(2)

   def main(self):
      self.comments()
      self.scroll()



if __name__ == '__main__':
   action = Action()
   action.main()


