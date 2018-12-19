#!/usr/bin/env python
# -*- coding:utf-8 -*-

import urllib2
import random

url = "http://www.baidu.com/"

ua_list = [
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv2.0.1) Gecko/20100101 Firefox/4.0.1",
    "Mozilla/5.0 (Windows NT 6.1; rv2.0.1) Gecko/20100101 Firefox/4.0.1",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11",
    "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"
]

user_agent = random.choice(ua_list)
request = urllib2.Request(url) #构造一个请求
request.add_header("User-Agent", user_agent) #添加一个HTTP报头
print request.get_header("User-agent")
