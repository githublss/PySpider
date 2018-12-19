#!/usr/bin/env python
# -*- coding:utf-8 -*-

import urllib2
import os

proxyuser = os.environ.get("proxyuser")
proxypasswd = os.environ.get("proxypasswd")

authproxy_handler = urllib2.ProxyHandler({"http": "mr_mao_hacker:sffqry9r@114.215.104.49:16816"})
opener = urllib2.build_opener(authproxy_handler)

request = urllib2.Request("http://www.baidu.com/")
response = opener.open(request)
print response.read()