#!/usr/bin/env python
# -*- coding:utf-8 -*-

import urllib2
import urllib

url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null"

headers = {
"Host" : "fanyi.youdao.com",
"Accept" : "application/json, text/javascript, */*; q=0.01",
"Origin" : "http://fanyi.youdao.com",
"X-Requested-With" : "XMLHttpRequest",
"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
"Content-Type" : "application/x-www-form-urlencoded; charset=UTF-8",


"Accept-Language" : "zh-CN,zh;q=0.8"
}

key = raw_input("请输入需要翻译的英文:")

formdata = {
"i": key,
"from":"AUTO",
"to":"AUTO",
"smartresult":"dict",
"client":"fanyideskweb",
# "salt":"1516970899948",
# "sign":"2776b8856d32e207dd4adece0e5c3938",
"doctype":"json",
"version":"2.1",
"keyfrom":"fanyi.web",
"action":"FY_BY_REALTIME",
"typoResult":"false"
}
data = urllib.urlencode(formdata)

request = urllib2.Request(url, data=data, headers= headers)
print urllib2.urlopen(request).read()