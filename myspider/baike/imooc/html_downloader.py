#!/usr/bin/env python
# -*- coding:utf-8 -*-
import urllib2
import urllib

## 网页下载器
### urllib2
### requests
class HtmlDownloader(object):

    def download(self, url):
        if url is None:
            return None
        response = urllib2.urlopen(url)
        if response.getcode() != 200:
            return None
        return response.read()
