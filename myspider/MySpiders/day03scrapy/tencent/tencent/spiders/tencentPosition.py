# -*- coding: utf-8 -*-
import scrapy
from tencent.items import TencentItem
from scrapy.loader import ItemLoader
#创建一个爬虫类
class TencentpositionSpider(scrapy.Spider):
    # 爬虫名
    name = "tencentPosition"
    # 允许爬虫的范围
    allowed_domains = ["tencent.com"]
    # 爬虫起始的url
    url = 'https://hr.tencent.com/position.php?&start='
    offset = 0
    start_urls = [url + str(offset)]

    def parse(self, response):
        for each in response.xpath("//tr[@class='even']|//tr[@class='odd']"):
            item = TencentItem()
            l = ItemLoader(item=TencentItem(),response=response)

