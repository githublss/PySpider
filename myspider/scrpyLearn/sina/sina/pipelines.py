# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class SinaPipeline(object):
    def process_item(self, item, spider):
        sonUrls = item['sonUrls']

        #文件名为子链接url中间部分，将/替换为_,保存为。TXT格式
        filename = sonUrls[7:-6].replace('/','_')
        filename = filename + ".txt"

        fp = open(item['subFilename']+'/'+filename,'w')
        fp.write(item['content'])
        fp.close
        return item
