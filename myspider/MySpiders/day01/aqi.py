#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 城市空气质量数据的获取
import urllib2
import urllib
import pandas as pd
import json
import sys

reload(sys)     #为了下一行进行设置编码
sys.setdefaultencoding('utf-8')
url = "http://www.bjmemc.com.cn/xgzs_searchAirQuality.action "

headers = {
"Host": "www.bjmemc.com.cn",

"Accept": "*/*",
"Origin": "http://www.bjmemc.com.cn",

"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
"Referer": "http://www.bjmemc.com.cn/xgzs_sjcx.action",
"Accept-Language": "zh-CN,zh;q=0.9",
"Cookie": "JSESSIONID=99D2FB06FC54A76DC74050112385A7FC",
}
f = open(r'D:/aqi.txt','a')
for time in pd.date_range('20180801','20180803'):
    time=time.strftime(r'%Y-%m-%d')
    print time
    dname='城市环境评价点'
    sname='东城东四'

    formdata = {
    "dName":dname,
    "siteName":sname,
    "time":time ,
    }
    data = urllib.urlencode(formdata)

    request = urllib2.Request(url, data=data, headers= headers)
    text=urllib2.urlopen(request).read()

    text=json.loads(text)
    if(text['o38haqi']):
        print '空气质量指数：' + text['o38haqi']
        print '空气质量级别：' + text['qlevel']
        print '空气质量描述：' + text['description']
        f.write("\n'空气质量指数：'" + text['o38haqi']+"\n空气质量级别：'" + text['qlevel']+"\n空气质量描述：'" + text['description'])
    else:
        print 'no have date'