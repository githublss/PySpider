#!/usr/bin/env python
# -*- coding:utf-8 -*-
import re
import urlparse

from bs4 import BeautifulSoup


class HtmlParser(object):

    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return

        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        return new_urls, new_data
#<div class="postWorkCard__img ovf">
# <a href="/illust/detail/43286/1839174" class="postWorkCard__link" target="_blank">
# </a>
# <img src="https://img9.bcyimg.com/drawer/43286/post/c0c7t/aa9cad70e93611e7a4e9c9626748eba1.png/tl640" alt="Luv  letter  *" ✿"*."="">
# <span class="countBadge"><i class="i-multiPic-white mr5"></i>多图</span> </div>
    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        # links = soup.find_all('a', href=re.compile(r"/view/\d+\.htm"))
        # links = soup.find_all('a', href=re.compile(r"/item/(.*)"))
        # links = soup.find_all('a', href=re.compile(r"/illust/detail/(.*)"))
        links = soup.find_all('a', href=re.compile(r"/illust/detail/\d+/\d+"))
        for link in links:
            new_url = link['href']
            new_full_url = urlparse.urljoin(page_url, new_url)
            new_urls.add(new_full_url)
        return new_urls

    def _get_new_data(self, page_url, soup):
        res_data = {}

        # url
        res_data['url'] = page_url
        # <dd class="lemmaWgt-lemmaTitle-title"><h1>Python</h1>
        title_node = soup.find('div', class_= "postWorkCard__img ovf").find("img")
        res_data['title'] = title_node.get_text()

        # summary_node = soup.find('div', class_="lemma-summary")
        # res_data['summary'] = summary_node.get_text()
        return res_data