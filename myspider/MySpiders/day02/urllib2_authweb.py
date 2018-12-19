#!/usr/bin/env python
# -*- coding:utf-8 -*-

import urllib2

test = "test"
password = "123456"
webserver = "192.168.21.52"

passwordMgr = urllib2.HTTPPasswordMgrWithDefaultRealm()

passwordMgr.add_password(None,webserver,test,password)

httpauth_handler = urllib2.HTTPBasicAuthHandler(passwordMgr)

proxyauth_handler = urllib2.ProxyBasicAuthHandler(passwordMgr)

opener = urllib2.build_opener(httpauth_handler,proxyauth_handler)

request = urllib2.Request("http://192.168.21.52/")

response = opener.open(request)

print response.read()