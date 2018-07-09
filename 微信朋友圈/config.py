#! /usr/bin/env python
# *_*coding:utf-8 *_*


#平台
PLATFORM = 'Android'

#设备名称，通过adb devices -l 获取
DEVICE_NAME = 'meizu_MA5'


#APP包名 通过adb logcat|grep START 查看对应的应用包名
APP_PACKAGE = 'com.tencent.mm'

#入口类名
APP_ACTIVITY = '.ui.LauncherUI'

#Appium地址
DRIVER_SERVER = 'http://localhost:4723/wd/hub'

#等待元素加载时间
TIMEOUT = 300

#微信手机号密码
USERNAME = ''
PASSWORD = ''

#滑动点
FLICK_START_X = 300
FLICK_START_Y = 300
FLICK_DISTANCE = 700

#MongoDB配置
MONGO_URL = 'localhost'
MONGO_DB = 'moments'
MONGO_COLLECTION = 'moments'

#滑动间隔
SCROLL_SLEEP_TIME = 1
