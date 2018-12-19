#!/usr/bin/env python
# -*- coding:utf-8 -*-

import urllib2

#向指定的url发送请求,返回服务器响应的类文件对象
response = urllib2.urlopen("http://www.baidu.com/")
#服务器返回到类文件对象的操作方法 read()方法就是读取文件的全部内容,返回字符串
html = response.read()
print response.getcode()
print html
