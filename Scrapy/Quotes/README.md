# Quotes
## 切换到quote目录下执行scrapy crawl quotes   
## 如果你本地有多个python环境的话，记得使用python -m scrapy crawl quotes  
 
## 目录结构  
```
这是一个scrapy框架默认目录结构   
scrapy.cfg --> 配置文件，指定settings配置文件路径  
quote/ ---> 该项目的python模块，之后您将在此加入代码   
quote/items.py --> 用来保存数据接口   
quote/middlewares.py --> 存储中间件   
quote/pipelines.py --> 项目中的pipelines文件   
quote/settings.py --> 定义一些配置信息   
quote/spiders/ --> 放置spider代码的目录   
```

## 存储是使用mongodb进行数据存储，配置信息是在pipelines.py文件中写了一个MongoPipeline类
## 之后需要在settings.py文件中添加，如果不添加会无法正常将数据存储到数据库中  
```  
ITEM_PIPELINES = {  
   'quote.pipelines.TextPipeline': 300,  #后面的数字是优先级，数字越小优先级越高   
   'quote.pipelines.MongoPipeline': 500,     
}     
```

```
部分运行结果：  
2018-06-28 10:52:58 [scrapy.utils.log] INFO: Scrapy 1.5.0 started (bot: quote)    
2018-06-28 10:52:58 [scrapy.utils.log] INFO: Versions: lxml 4.2.1.0, libxml2 2.9.8, cssselect 1.0.3, parsel     1.4.0, w3lib 1.19.0, Twisted 18.4.0, Python 3.6.5 (default, Apr 25 2018, 14:23:58) - [GCC 4.2.1 Compatible Apple LLVM 9.1.0 (clang-902.0.39.1)], pyOpenSSL 18.0.0 (OpenSSL 1.1.0h  27 Mar 2018), cryptography 2.2.2, Platform Darwin-17.5.0-x86_64-i386-64bit   
2018-06-28 10:52:58 [scrapy.crawler] INFO: Overridden settings: {'BOT_NAME': 'quote', 'NEWSPIDER_MODULE':    'quote.spiders', 'ROBOTSTXT_OBEY': True, 'SPIDER_MODULES': ['quote.spiders']}   
2018-06-28 10:52:58 [scrapy.middleware] INFO: Enabled extensions:   
['scrapy.extensions.corestats.CoreStats',   
 'scrapy.extensions.telnet.TelnetConsole',  
 'scrapy.extensions.memusage.MemoryUsage',  
 'scrapy.extensions.logstats.LogStats']   
2018-06-28 10:52:58 [scrapy.middleware] INFO: Enabled downloader middlewares:   
['scrapy.downloadermiddlewares.robotstxt.RobotsTxtMiddleware',   
 'scrapy.downloadermiddlewares.httpauth.HttpAuthMiddleware',   
 'scrapy.downloadermiddlewares.downloadtimeout.DownloadTimeoutMiddleware',   
 'scrapy.downloadermiddlewares.defaultheaders.DefaultHeadersMiddleware',   
 'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware',   
 'scrapy.downloadermiddlewares.retry.RetryMiddleware',   
 'scrapy.downloadermiddlewares.redirect.MetaRefreshMiddleware',   
 'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware',   
 'scrapy.downloadermiddlewares.redirect.RedirectMiddleware',   
 'scrapy.downloadermiddlewares.cookies.CookiesMiddleware', 
 'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware',   
 'scrapy.downloadermiddlewares.stats.DownloaderStats']   
2018-06-28 10:52:58 [scrapy.middleware] INFO: Enabled spider middlewares:   
['scrapy.spidermiddlewares.httperror.HttpErrorMiddleware',   
 'scrapy.spidermiddlewares.offsite.OffsiteMiddleware',   
 'scrapy.spidermiddlewares.referer.RefererMiddleware',   
 'scrapy.spidermiddlewares.urllength.UrlLengthMiddleware',   
 'scrapy.spidermiddlewares.depth.DepthMiddleware']   
2018-06-28 10:52:58 [scrapy.middleware] INFO: Enabled item pipelines:   
['quote.pipelines.TextPipeline', 'quote.pipelines.MongoPipeline']   
2018-06-28 10:52:58 [scrapy.core.engine] INFO: Spider opened   
2018-06-28 10:52:58 [scrapy.extensions.logstats] INFO: Crawled 0 pages (at 0 pages/min), scraped 0 items (at 0 items/min)   
2018-06-28 10:52:58 [scrapy.extensions.telnet] DEBUG: Telnet console listening on 127.0.0.1:6023   
2018-06-28 10:52:59 [scrapy.core.engine] DEBUG: Crawled (404) <GET http://quotes.toscrape.com/robots.txt> (referer: None)   
2018-06-28 10:53:00 [scrapy.core.engine] DEBUG: Crawled (200) <GET http://quotes.toscrape.com/> (referer: None)  
2018-06-28 10:53:00 [scrapy.core.scraper] DEBUG: Scraped from <200 http://quotes.toscrape.com/>   
{'author': 'Albert Einstein',   
 'tags': ['change', 'deep-thoughts', 'thinking', 'world'],   
 'text': '“The world as we have created it is a process of o...'}   
2018-06-28 10:53:00 [scrapy.core.scraper] DEBUG: Scraped from <200 http://quotes.toscrape.com/>   
{'author': 'J.K. Rowling',   
 'tags': ['abilities', 'choices'],   
 'text': '“It is our choices, Harry, that show what we truly...'}   
2018-06-28 10:53:00 [scrapy.core.scraper] DEBUG: Scraped from <200 http://quotes.toscrape.com/>   
{'author': 'Albert Einstein',   
 'tags': ['inspirational', 'life', 'live', 'miracle', 'miracles'],   
 'text': '“There are only two ways to live your life. One is...'}   
2018-06-28 10:53:00 [scrapy.core.scraper] DEBUG: Scraped from <200 http://quotes.toscrape.com/>   
{'author': 'Jane Austen',  
 'tags': ['aliteracy', 'books', 'classic', 'humor'],   
 'text': '“The person, be it gentleman or lady, who has not...'}   
2018-06-28 10:53:00 [scrapy.core.scraper] DEBUG: Scraped from <200 http://quotes.toscrape.com/>   
```
