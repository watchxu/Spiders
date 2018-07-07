# Lagou

## 拉钩网站抓取，分别使用scrapy框架和requests库进行抓取，效果都是一样的   

## LagouSpider这个文件中同时定义了一个LagouSpider类，分别包含了
```    
	auth_token：获取代理ip，因为频繁请求拉钩，网站会封禁本地ip   
	parse：主要是对抓取到的response进行解析格式化  
	save：将数据保存到文件中，也可以到数据库中，这里目前只保存到文件中   
	main：真正执行的函数   
```
## scrapy抓取相对来说就比较简单，主要是获取的ajax页面，对ajax不对进行循环请求即可，然后数据存储到数据库中或者文件中   