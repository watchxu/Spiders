# 去哪网--酒店信息抓取

## 环境要求
```
python3以上
```


## 使用的三方库
```
selenium
pyquery
time
re
```

## 分析思路
```
1.分析去哪网显示数据的方式，发现ajax请求并没有返回数据，并且进行页数切换时，url也没有变，所以猜想数据应该是被js渲染过的
2.想到使用selenium进行抓取
3.
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
这里的price使用正则匹配出价格，同时对售罄的酒店就行过滤
```


## 运行结果
![Image text]()