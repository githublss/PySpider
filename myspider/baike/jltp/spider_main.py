#!/usr/bin/env python
# -*- coding:utf-8 -*-
from gitbaike import url_manager, html_downloader, html_outputer
from jltp import html_parser


class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self,root_url):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print 'craw %d  %s' % (count, new_url)
                html_count = self.downloader.download(new_url)
                new_urls, new_name = self.parser.parse(new_url, html_count)
                self.urls.add_new_urls(new_urls)

                if count == 10:
                    break

                count = count + 1
            except:
                print 'craw failed'

if __name__ == "__main__":
    root_url = "https://bcy.net/u/453458/post/illust"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)