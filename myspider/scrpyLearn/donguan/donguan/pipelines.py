# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json

class DonguanPipeline(object):
    def __init__(self):
        self.filename = open('dongguan.json','w')

    def process_item(self, item, spider):
        # 当item中有汉字是要将ensure_ascii 设置为False，Unicode编码是万国码，具有通用性
        text = json.dumps(dict(item),ensure_ascii = False)+",\n"
        self.filename.write(text.encode('utf-8'))
        return item

    def close_spider(self,spider):
        self.filename.close()
