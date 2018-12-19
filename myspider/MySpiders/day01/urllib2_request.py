#!/usr/bin/env python
# -*- coding:utf-8 -*-

import urllib2

ua_headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"
}
request = urllib2.Request("http://www.baidu.com/", headers=ua_headers)

response = urllib2.urlopen(request)

html = response.read()
print response.getcode()

print response.geturl()

print response.info()
