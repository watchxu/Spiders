环境要求：python3
抓取猫眼电影top100 --> code.py

抓取的目标网站为：http://maoyan.com/board/4
页面中显示的有效信息有影片名称、主演、上映时间、上映地区、评分、图片等信息
点击下一页发现url会变成http://maoyan.com/board/4?offset=30，主要增加了offset参数，
且规律是0，10，20，30
使用正则表达式对网页进行解析


直接在命令行执行：python3 code.py
{'index': '1', 'image': 'http://p1.meituan.net/movie/20803f59291c47e1e116c11963ce019e68711.jpg@160w_220h_1e_1c', 'title': '霸王别姬', 'actor': '张国荣,张丰毅,巩俐', 'time': '1993-01-01(中国香港)', 'score': '9.6'}
{'index': '2', 'image': 'http://p0.meituan.net/movie/283292171619cdfd5b240c8fd093f1eb255670.jpg@160w_220h_1e_1c', 'title': '肖申克的救赎', 'actor': '蒂姆·罗宾斯,摩根·弗里曼,鲍勃·冈顿', 'time': '1994-10-14(美国)', 'score': '9.5'}
{'index': '3', 'image': 'http://p0.meituan.net/movie/54617769d96807e4d81804284ffe2a27239007.jpg@160w_220h_1e_1c', 'title': '罗马假日', 'actor': '格利高里·派克,奥黛丽·赫本,埃迪·艾伯特', 'time': '1953-09-02(美国)', 'score': '9.1'}
{'index': '4', 'image': 'http://p0.meituan.net/movie/e55ec5d18ccc83ba7db68caae54f165f95924.jpg@160w_220h_1e_1c', 'title': '这个杀手不太冷', 'actor': '让·雷诺,加里·奥德曼,娜塔莉·波特曼', 'time': '1994-09-14(法国)', 'score': '9.5'}
{'index': '5', 'image': 'http://p1.meituan.net/movie/f5a924f362f050881f2b8f82e852747c118515.jpg@160w_220h_1e_1c', 'title': '教父', 'actor': '马龙·白兰度,阿尔·帕西诺,詹姆斯·肯恩', 'time': '1972-03-24(美国)', 'score': '9.3'}
{'index': '6', 'image': 'http://p1.meituan.net/movie/0699ac97c82cf01638aa5023562d6134351277.jpg@160w_220h_1e_1c', 'title': '泰坦尼克号', 'actor': '莱昂纳多·迪卡普里奥,凯特·温丝莱特,比利·赞恩', 'time': '1998-04-03', 'score': '9.5'}
{'index': '7', 'image': 'http://p0.meituan.net/movie/b03e9c52c585635d2cb6a3f7c08a8a50112441.jpg@160w_220h_1e_1c', 'title': '龙猫', 'actor': '日高法子,坂本千夏,糸井重里', 'time': '1988-04-16(日本)', 'score': '9.2'}
{'index': '8', 'image': 'http://p0.meituan.net/movie/da64660f82b98cdc1b8a3804e69609e041108.jpg@160w_220h_1e_1c', 'title': '唐伯虎点秋香', 'actor': '周星驰,巩俐,郑佩佩', 'time': '1993-07-01(中国香港)', 'score': '9.2'}
{'index': '9', 'image': 'http://p0.meituan.net/movie/46c29a8b8d8424bdda7715e6fd779c66235684.jpg@160w_220h_1e_1c', 'title': '魂断蓝桥', 'actor': '费雯·丽,罗伯特·泰勒,露塞尔·沃特森', 'time': '1940-05-17(美国)', 'score': '9.2'}
{'index': '10', 'image': 'http://p0.meituan.net/movie/b076ce63e9860ecf1ee9839badee5228329384.jpg@160w_220h_1e_1c', 'title': '千与千寻', 'actor': '柊瑠美,入野自由,夏木真理', 'time': '2001-07-20(日本)', 'score': '9.3'}
{'index': '11', 'image': 'http://p0.meituan.net/movie/230e71d398e0c54730d58dc4bb6e4cca51662.jpg@160w_220h_1e_1c', 'title': '乱世佳人', 'actor': '费雯·丽,克拉克·盖博,奥利维娅·德哈维兰', 'time': '1939-12-15(美国)', 'score': '9.1'}
{'index': '12', 'image': 'http://p1.meituan.net/movie/18e3191039d5e71562477659301f04aa61905.jpg@160w_220h_1e_1c', 'title': '喜剧之王', 'actor': '周星驰,莫文蔚,张柏芝', 'time': '1999-02-13(中国香港)', 'score': '9.2'}
{'index': '13', 'image': 'http://p1.meituan.net/movie/ba1ed511668402605ed369350ab779d6319397.jpg@160w_220h_1e_1c', 'title': '天空之城', 'actor': '寺田农,鹫尾真知子,龟山助清', 'time': '1992', 'score': '9.1'}
{'index': '14', 'image': 'http://p1.meituan.net/movie/14a7b337e8063e3ce05a5993ed80176b74208.jpg@160w_220h_1e_1c', 'title': '大闹天宫', 'actor': '邱岳峰,毕克,富润生', 'time': '1965-12-31', 'score': '9.0'}
{'index': '15', 'image': 'http://p1.meituan.net/movie/39ed7a0941a3604bba78d299b11a18ce119679.jpg@160w_220h_1e_1c', 'title': '辛德勒的名单', 'actor': '连姆·尼森,拉尔夫·费因斯,本·金斯利', 'time': '1993-12-15(美国)', 'score': '9.2'}
{'index': '16', 'image': 'http://p1.meituan.net/movie/6bc004d57358ee6875faa5e9a1239140128550.jpg@160w_220h_1e_1c', 'title': '音乐之声', 'actor': '朱莉·安德鲁斯,克里斯托弗·普卢默,埃琳诺·帕克', 'time': '1965-03-02(美国)', 'score': '9.0'}
{'index': '17', 'image': 'http://p0.meituan.net/movie/ae7245920d95c03765fe1615f3a1fe3865785.jpg@160w_220h_1e_1c', 'title': '春光乍泄', 'actor': '张国荣,梁朝伟,张震', 'time': '1997-05-30(中国香港)', 'score': '9.2'}
{'index': '18', 'image': 'http://p1.meituan.net/movie/0e91ffcfa7e53449216cc29ee8af513a75791.jpg@160w_220h_1e_1c', 'title': '剪刀手爱德华', 'actor': '约翰尼·德普,薇诺娜·瑞德,黛安·韦斯特', 'time': '1990-12-06(美国)', 'score': '8.8'}
{'index': '19', 'image': 'http://p0.meituan.net/movie/43d259ecbcd53e8bbe902632772281d6327525.jpg@160w_220h_1e_1c', 'title': '美丽人生', 'actor': '罗伯托·贝尼尼,尼可莱塔·布拉斯基,乔治·坎塔里尼', 'time': '1997-12-20(意大利)', 'score': '9.3'}
{'index': '20', 'image': 'http://p1.meituan.net/movie/c15b7623cce2f51c75562a3baefe507b68290.jpg@160w_220h_1e_1c', 'title': '海上钢琴师', 'actor': '蒂姆·罗斯,普路特·泰勒·文斯,比尔·努恩', 'time': '1998-10-28(意大利)', 'score': '9.2'}


抓取猫眼热映口碑榜 --> code2.py
抓取的目标网站为：http://maoyan.com/board
显示片名、主演、上映时间
使用xpath提取网页内容

直接在命令行执行：python3 code2.py
{'id': '1', 'title': '超人总动员2', 'actor': '主演：格雷格·T·尼尔森,霍利·亨特,莎拉·沃威尔', 'time': '间：2018-06-22'}
{'id': '2', 'title': '阿飞正传', 'actor': '主演：张国荣,张曼玉,刘德华', 'time': '间：2018-06-25'}
{'id': '3', 'title': '超时空同居', 'actor': '主演：雷佳音,佟丽娅,徐峥', 'time': '间：2018-05-18'}
{'id': '4', 'title': '生存家族', 'actor': '主演：小日向文世,深津绘里,泉泽祐希', 'time': '间：2018-06-22'}
{'id': '5', 'title': '复仇者联盟3：无限战争', 'actor': '主演：小罗伯特·唐尼,克里斯·海姆斯沃斯,马克·鲁弗洛', 'time': '间：2018-05-11'}
{'id': '6', 'title': '青年马克思', 'actor': '主演：奥古斯特·迪尔,史特凡·柯纳斯克,薇姬·克里普斯', 'time': '间：2018-05-05'}
{'id': '7', 'title': '侏罗纪世界2', 'actor': '主演：克里斯·帕拉特,布莱丝·达拉斯·霍华德,泰德·拉文', 'time': '间：2018-06-15'}
{'id': '8', 'title': '完美陌生人', 'actor': '主演：朱塞佩·巴蒂斯通,安娜·福列塔,马可·贾利尼', 'time': '间：2018-05-25'}
{'id': '9', 'title': '第七个小矮人', 'actor': '主演：Otto Waalkes,Mirco Nontschew,Boris Aljinovic', 'time': '间：2018-06-16'}


两个代码主要分为四个部分：
1、获取抓取的网站源码 --> get_one_page
2、解析获取的网站源码 --> parse_one_page
3、存储抓取的内容    -->  write_to_file
4、主函数           --> main 