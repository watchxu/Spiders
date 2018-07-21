# 抓取亚马逊网站信息

## 使用的模块
```
requests ---> 获取html信息
pyquery  --->  解析html，提取需要的信息
re --- 提取价格信息
```

## 主要功能函数
```
get_html()  ---> 模拟请求，获取html数据
parse()  ---> 使用pyquery库进行数据提取
main() ---> 主函数
```

## 运行结果：python3 amazon.py
```
Please enter the item you want to grab:ipad
Number of pages seized:2
Start grabbing the 1 page
{'image': 'https://images-cn.ssl-images-amazon.com/images/I/5103X180QPL._AA200_.jpg', 'title': '【2018新款】Apple iPad 平板电脑 9.7英寸 WiFi版 128GB 金色 （A10 芯片/Retina显示屏/Touch ID MRJP2CH/A）正品国行 顺丰发货 可开专票', 'price': '￥2,964.00'}
{'image': 'https://images-cn.ssl-images-amazon.com/images/I/41EPtGRh+oL._AA200_.jpg', 'title': '【2018新款】Apple iPad 平板电脑 9.7英寸 WiFi版 128G 深空灰 （A10 芯片/Retina显示屏/Touch ID MR7J2CH/A）正品国行 顺丰发货 可开专票', 'price': '￥2,967.00'}
{'image': 'https://images-cn.ssl-images-amazon.com/images/I/5103X180QPL._AA200_.jpg', 'title': '【2018新款】Apple iPad 平板电脑 9.7英寸 WiFi版 32GB 金色 （A10 芯片/Retina显示屏/Touch ID MRJN2CH/A）正品国行 顺丰发货 可开专票', 'price': '￥2,290.00'}
{'image': 'https://images-cn.ssl-images-amazon.com/images/I/51npy57EpbL._AA200_.jpg', 'title': '【2017新款】 Apple iPad 9.7英寸平板电脑(金色) WIFI版 32G', 'price': '￥1,997.00'}
{'image': 'https://images-cn.ssl-images-amazon.com/images/I/51pQAwXPNxL._AA200_.jpg', 'title': 'Apple iPad 9.7英寸平板电脑(银色) WIFI版 128G【2017款】', 'price': '￥2,746.00'}
{'image': 'https://images-cn.ssl-images-amazon.com/images/I/510Ta9x1YtL._AA200_.jpg', 'title': 'Apple iPad mini 4 MK9P2CH/A 7.9英寸平板电脑 (128G/WLAN/银色)', 'price': '￥2,525.00'}
{'image': 'https://images-cn.ssl-images-amazon.com/images/I/51d0cR35q+L._AA200_.jpg', 'title': '美国MoKo 苹果 新iPad 9.7寸保护套带笔槽 苹果9.7英寸三折智能休眠保护壳 iPad9.7轻薄防摔全包壳 适配全新Apple iPad 9.7英寸2018款（A1893/A1954） 平板电脑支撑折叠保护皮套 深蓝色', 'price': '￥69.00'}
{'image': 'https://images-cn.ssl-images-amazon.com/images/I/51wfhVaKnUL._AA200_.jpg', 'title': '【2018新款】 Apple iPad 9.7英寸平板电脑(128G WIFI版/A10 芯片/Retina显示屏/Touch ID技术 MR7K2CH/A) 银色 套装版【内含复古麋鹿定制款保护套+chirslain清洁套装】', 'price': '￥3,018.00'}
{'image': 'https://images-cn.ssl-images-amazon.com/images/I/51o91zTSzCL._AA200_.jpg', 'title': 'Apple iPad mini 4 MK9Q2CH/A 7.9英寸平板电脑 (128G/WLAN/金色)', 'price': '￥2,550.00'}
{'image': 'https://images-cn.ssl-images-amazon.com/images/I/41qSdzsIkxL._AA200_.jpg', 'title': '【2018新款】 Apple iPad 9.7英寸平板电脑(32G WIFI版/A10 芯片/Retina显示屏/Touch ID技术 MR7G2CH/A) 银色 套装版【内含复古麋鹿定制款保护套+chirslain清洁套装】', 'price': '￥2,299.00'}
{'image': 'https://images-cn.ssl-images-amazon.com/images/I/41HQsyS5QqL._AA200_.jpg', 'title': '美国MoKo 苹果 Apple iPad 9.7 保护套 苹果9.7英寸三折智能休眠全包保护壳 iPad9.7轻薄磨砂质感背壳半透明保护壳 适配全新Apple iPad 9.7英寸 Retina（2018 / 2017版)平板电脑支撑折叠保护皮套 海军蓝', 'price': '￥69.00'}
{'image': 'https://images-cn.ssl-images-amazon.com/images/I/51npy57EpbL._AA200_.jpg', 'title': '【2017新款】 Apple iPad 9.7英寸平板电脑(金色) WIFI版 128G', 'price': '￥2,754.00'}
{'image': 'https://images-cn.ssl-images-amazon.com/images/I/51fXzOPJETL._AA200_.jpg', 'title': 'Apple iPad 9.7英寸平板电脑(深空灰色) WIFI版 128G 【2017款】', 'price': '￥2,754.00'}
{'image': 'https://images-cn.ssl-images-amazon.com/images/I/41PvYC7o24L._AA200_.jpg', 'title': 'Kindle Paperwhite电子书阅读器： 300 ppi超清电子墨水触控屏、内置阅读灯、超长续航', 'price': '￥958.00'}
{'image': 'https://images-cn.ssl-images-amazon.com/images/I/51pQAwXPNxL._AA200_.jpg', 'title': 'Apple iPad 9.7英寸平板电脑(银色) WIFI版 32G 【2017款】', 'price': '￥2,105.00'}
{'image': 'https://images-cn.ssl-images-amazon.com/images/I/51t10idOgkL._AA200_.jpg', 'title': 'Logitech 罗技 多功能智能设备 蓝牙键盘K480-黑 支持Ipad', 'price': '￥172.00'}
{'image': 'https://images-cn.ssl-images-amazon.com/images/I/510KAiART9L._AA200_.jpg', 'title': 'Apple iPad mini 4 MK9N2CH/A 7.9英寸平板电脑 (128G/WLAN/深空灰色)', 'price': '￥2,530.00'}

```