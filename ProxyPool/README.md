# ProxyPool

## 背景

### 为什么要使用代理池？
1.许多网站有专门的反爬虫措施，可能遇到封IP等问题 
2.互联网上公开了大量免费代理，利用好资源 
3.通过定时的检测维护同样可以得到多个可用的代理 

### 代理池的要求？
1.多站抓取，异步检测 
2.定时筛选，持续更新 
3.提供接口，易于提取 

### 代理池架构
![Image text](https://github.com/watchxu/PythonSpiders/tree/master/ProxyPool/proxypool/image.jpg)

## 安装

### 安装Python

至少Python3.5以上

### 安装Redis

安装好之后将Redis服务开启

### 配置代理池

```
cd proxypool
```

进入proxypool目录，修改settings.py文件

PASSWORD为Redis密码，如果为空，则设置为None

#### 安装依赖

```
pip3 install -r requirements.txt
```

#### 打开代理池和API

```
python3 run.py
```

## 获取代理


利用requests获取方法如下

```python
import requests

PROXY_POOL_URL = 'http://localhost:5555/random'

def get_proxy():
    try:
        response = requests.get(PROXY_POOL_URL)
        if response.status_code == 200:
            return response.text
    except ConnectionError:
        return None
```

