#!/usr/bin/env python
# -*- coding:utf-8 -*-
import urllib2
import urllib
url = "https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action"

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"}
formdata = {
    'start':'0',
    'limit': '100'
}
data = urllib.urlencode(formdata)

request = urllib2.Request(url,data= data,headers=headers)
print urllib2.urlopen(request).read()