import sys
import hashlib
import requests
from requests import exceptions
import time
import json

class LagouSpider(object):



    def auth_token(self):
        _version = sys.version_info

        is_python3 = (_version[0] == 3)

        orderno = "ZF20186293991RYB1UK"
        secret = "b73f0702d5a142409a8dd51ec4c4b860"

        ip = "forward.xdaili.cn"
        port = "80"

        ip_port = ip + ":" + port

        timestamp = str(int(time.time()))                # 计算时间戳
        string = ""
        string = "orderno=" + orderno + "," + "secret=" + secret + "," + "timestamp=" + timestamp

        if is_python3:
            string = string.encode()

        md5_string = hashlib.md5(string).hexdigest()                 # 计算sign
        sign = md5_string.upper()                              # 转换成大写
        global auth
        auth = "sign=" + sign + "&" + "orderno=" + orderno + "&" + "timestamp=" + timestamp


        proxy = {"http": "http://" + ip_port, "https": "https://" + ip_port}
        return proxy

    def parse(self,proxy,page):
        city = '北京'
        # url = "https://www.lagou.com/jobs/positionAjax.json"
        url = 'https://www.lagou.com/jobs/positionAjax.json?city=' + city + '&needAddtionalResult=false&isSchoolJob=0'
        headers = {
            "Proxy-Authorization": auth,
            'Host': 'www.lagou.com',
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Language': 'zh-CN,en-US;q=0.7,en;q=0.3',
            'Accept-Encoding': 'gzip, deflate, br',
            'Referer': 'https://www.lagou.com/jobs/list_Python',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'X-Requested-With': 'XMLHttpRequest',


            }

        body = {
            "first": "true",
            "pn": page,
            "kd": "python爬虫"
        }
        try:
            r = requests.post(url=url, headers=headers, data=body,proxies=proxy,verify=False,allow_redirects=False)
            return r
        except Exception:
            pass


    def save(self,result):
        with open('result.txt', 'a', encoding='utf-8') as f:
            f.write(json.dumps(result, ensure_ascii=False) + '\n')

    def main(self):
        proxy = self.auth_token()

        for i in range(1,31):

            response = self.parse(proxy,i)
            try:
                result = json.loads(response.text)
                try:
                    if result['success'] != "false":
                       
                        print(str(i).center(50,"#"))
                        print(result)
                        self.save(result)
                        continue
                    else:
                        proxy = self.auth_token()
                except exceptions.ProxyError:
                    pass
            except Exception:
                pass



if __name__ == '__main__':
    response = LagouSpider()
    response.main()

