#!/usr/bin/env python
# -*- coding:utf-8 -*-
import urllib
import urllib2

url = "http://www.baidu.com/s"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"}

keyword = raw_input("please in put a keyword: ")
wd = {"wd": keyword}
#通过urllib.urlencode() 参数是一个dict类型
wd = urllib.urlencode(wd)

fulurl = url + "?" + wd

#构造请求对象
request = urllib2.Request(fulurl, headers=headers)

response = urllib2.urlopen(request)

print response.read()