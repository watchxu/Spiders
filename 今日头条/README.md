目标：输入需要爬取的淘宝信息，例如爬取淘宝的“美食”信息
其中包括图片url、价格、交易量、店铺名、产地

使用的模块
selenium
pyquery
pymongo
re


代码中主要包含5个函数
search_keyword：主要是模拟浏览器在淘宝搜索框输入需要抓取的信息，其中模拟浏览器是使用selenium模块
index_page：抓取索引页，主要功能是“找到换页框”、“点击确定框”从而实现翻页功能，并且验证当前抓取页（page）是否和真实抓取的页面一致
get_products：主要是解析网页源码，提取数据，代码中是使用pyquery模块进行提取的
save_to_mongo：数据存储，这里是使用的MongoDB进行数据存储，在存储之前需要创建对应的库和表
main：主要控制抓取什么信息，还有抓取的页数


执行：python3 code.py
请输入需要查询的内容 or q退出:ipad
total: 100 页
请输入页数:10
正在抓取第 1 页
{'image': 'http//g-search1.alicdn.com/img/bao/uploaded/i4/imgextra/i1/43576469/TB2sBHCieGSBuNjSspbXXciipXa_!!0-saturn_solar.jpg', 'price': '¥\n2318.00', 'deal': '5336人付款', 'title': '[12期分期]Apple/苹果 iPad 2018款 9.7英寸wifi新款平板电脑128G', 'shop': '卓辰数码旗舰店', 'location': '浙江 杭州'}
{'image': 'http//g-search3.alicdn.com/img/bao/uploaded/i4/i3/2616970884/TB1a5aayYuWBuNjSszgXXb8jVXa_!!0-item_pic.jpg', 'price': '¥\n1988.00', 'deal': '22410人付款', 'title': 'Apple/苹果\niPad\n9.7英寸平板电脑 WIFI 正品国行 正品国行开发票', 'shop': '苏宁易购官方旗舰店', 'location': '江苏 南京'}
{'image': 'http//g-search1.alicdn.com/img/bao/uploaded/i4/i3/1669409267/TB141zZr5OYBuNjSsD4XXbSkFXa_!!0-item_pic.jpg', 'price': '¥\n2318.00', 'deal': '5336人付款', 'title': '[12期分期]Apple/苹果\niPad\n2018款 9.7英寸wifi新款平板电脑128G', 'shop': '卓辰数码旗舰店', 'location': '浙江 杭州'}
{'image': 'http//g-search3.alicdn.com/img/bao/uploaded/i4/i3/2616970884/TB1_FIxqyCYBuNkSnaVXXcMsVXa_!!0-item_pic.jpg', 'price': '¥\n2398.00', 'deal': '101303人付款', 'title': '2018新款 Apple/苹果 9.7英寸\niPad\n智能平板电脑 正品国行', 'shop': '苏宁易购官方旗舰店', 'location': '江苏 南京'}
{'image': 'http//g-search2.alicdn.com/img/bao/uploaded/i4/i1/97045700/TB2qoUdyuuSBuNjSsplXXbe8pXa_!!97045700.jpg', 'price': '¥\n1878.00', 'deal': '3706人付款', 'title': 'Apple/苹果\niPad\n2018款 苹果平板电脑9.7英寸\nipad\n新款\nipad\n2018', 'shop': '深圳_恒波', 'location': '广东 深圳'}
