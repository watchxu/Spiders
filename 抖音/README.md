# douyin_v1.py

## 主要通过mitmdump进行分析抓取页面

## 安装依赖
```
pip3 install -r requirements.txt
```

## 获取视频播放地址
```
get_video_urls()
```

## 下载视频
```
video_downloader
```

## 运行主函数
```
python3 douyin.py
```

# douyin_v2.py

## 使用mitmdump和appium进行页面自动化抓取

### 主要使用appium对屏幕进行滑动抓取，抓取时间不要设置过短，可能有些视频会受网络影响会抓取失败

### script.py是操作手机实现自动化的

