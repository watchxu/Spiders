# 抓取火山小视频

## 分析视频请求地址结构
```
def response(flow):
    print(flow.request.url)
通过mitmdump分析视频地址结构，发现视频地址都是https://api.huoshan.com/hotsoon/item/video/_playback/?video_id=v0300c770000bd1j46782ijm1cnu5rhg&line=0
直接复制这个地址在浏览器访问发现可以直接看到视频内容，那么现在就开始对这个地址进行抓取
```

## 代码主要分为两个部分
### script.py抓取解析视频地址
### action.py模拟用户对视频内容进行翻页
```
 "platformName": "Android",  #如果是IOS就替换掉
 "deviceName": "meizu_MA5",  #执行adb devices -l可以查看
 "appPackage": "com.ss.android.ugc.live",  #下面两个信息可以通过adb logcat|grep START 查看对应的应用包名，看cmp这一行
 "appActivity": ".main.MainActivity"
```

