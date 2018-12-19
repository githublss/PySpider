#!/usr/bin/env python
# -*- coding:utf-8 -*-

import urllib2
import urllib

url = "http://www.bjmemc.com.cn/xgzs_searchAirQuality.action "

headers = {
"Host": "www.bjmemc.com.cn",


"Accept": "*/*",
"Origin": "http://www.bjmemc.com.cn",

"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
"Referer": "http://www.bjmemc.com.cn/xgzs_sjcx.action",
"Accept-Language": "zh-CN,zh;q=0.9",
"Cookie": "JSESSIONID=99D2FB06FC54A76DC74050112385A7FC",
}

# key = raw_input("请输入需要翻译的英文:")

formdata = {
"dName","城市环境评价点",
"siteName","东城东四",
"time","2018-08-18",
}
data = urllib.urlencode(formdata)

request = urllib2.Request(url, data=data, headers= headers)
print urllib2.urlopen(request).read()