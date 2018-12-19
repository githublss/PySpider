#!/usr/bin/env python
# -*- coding:utf-8 -*-

import urllib
import urllib2
import cookielib
#通过CookJar()类构造一个cookieJar()对象,吧保存cookie值
cookie = cookielib.CookieJar()
#通过HTTPCookieProcessor()处理器类构造一个处理器对象,用来处理cookie
cookie_handler = urllib2.HTTPCookieProcessor(cookie)

#构建一个自定义的opener
opener = urllib2.build_opener(cookie_handler)
#添加HTTP报头参数
opener.addheaders = [("User-Agent", "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36")]
# url = "http://www.renren.com/SysHome.do"
url = "http://www.renren.com/PLogin.do"
data = {"email": "13213818295","password": "199506"}
data = urllib.urlencode(data)

#生成请求对象
request = urllib2.Request(url, data= data)
#发送请求对象
response = opener.open(request)

print response.read()

# respon_test = opener.open("http://www.renren.com/848290267/profile")
# print respon_test.read()