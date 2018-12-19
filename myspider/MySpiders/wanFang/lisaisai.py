#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by lss on 2018/10/9
import os,commands
import xlrd,xlwt
from xlutils.copy import copy
import re
import numpy as np
import logging
from time import sleep
# ip 纬度 经度


def mkdir(path):    # 创建一个文件夹
    folder = os.path.exists(path)
    if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
        os.makedirs(path)  # makedirs 创建文件时如果路径不存在会创建这个路径
        print "---  new folder...  ---"
        print "---  OK  ---"

    else:
        print "---  There is this folder!  ---"
def averagenum(num):    # 计算一个数组的平均值
    nsum = 0
    if len(num)==0:
        return 0
    for i in range(len(num)):
        nsum += num[i]
    return nsum / len(num)
def open_excel(file):
    try:
        data = xlrd.open_workbook(file)
        return data
    except Exception,e:
        print str(e)

def write_excel(file='2.xlsx'):
    time = []
    if not os.path.exists(file):
        print '请添加一个iptest.xlsx文件！！！'.decode('utf-8').encode('gbk')
        sleep(9)
    tables = excel_table_byname(file)
    count = 0
    output = os.popen("curl ifconfig.me")
    myIp = output.read()    # 获取本地公网ip
    print 'publicIp:'+myIp
    mkdir('result')
    with open('result\\myPublicIp.txt','w') as f:
        f.write("本地公网IP是：{0}".format(myIp))
    while(count < len(tables)):
            for row in tables:
                try:
                    temptime = []    # 先定义一个临时时间
                    status = 0  # 状态指示码，指示是否请求成功
                    ipStart = row[0].split('.') # 获取到ip开始段
                    ipStart = map(int, ipStart) # 将string转化为int
                    startInt = ipStart[-1]
                    ipEnd = row[1].split('.')   # 获取到ip结束段
                    ipEnd = map(int,ipEnd)      # 将string转化为int
                    endInt = ipEnd[-1]
                    requestIp = ipStart[:3]
                    requestCount = 1  # 记录请求的次数
                    requestIp.append(np.random.randint(startInt,endInt+1))  #在ip的开始段和结束段之间随机生成一个ip
                    requestIp = ".".join(map(str,requestIp))    # 组合出来一个新的真实请求ip

                    print ipEnd,ipStart,requestIp
                    sql = 'tcping.exe ' + requestIp+' 80'   #加端口
                    print count,'/',len(tables),':',sql
                    output = os.popen(sql)
                    a = output.read()
                    print a
                    if ('Average ='not in a):  # 编码问题很烦人
                        status = 0
                    else:
                        temp = re.findall(r'\d+\.\d+ms', a)  # 将ping命令的返回值中的所有时间值获取到
                        temp = str(temp[-1])
                        status = 1
                    # 判断是否有参数的返回
                    if status == 1:
                        # isInt = int(re.search(r'\d+', temp).group())
                        print re.findall(r'\d+\.\d+', temp)[0]
                        temptime.append(float(re.findall(r'\d+\.\d+', temp)[0]))  # 将ping命令的返回值中的平均时间记录下来
                        # print temptime[-1]  # 打印最后一条的信息

                    while(requestCount < 3 & (endInt-startInt) >= 1):   #判断是否进行请求的发送,如果请求没有超过三次且ip段长度大于一个才发送
                        requestIp = ipStart[:3]
                        requestIp.append(np.random.randint(startInt, endInt + 1))  # 在ip的开始段和结束段之间随机生成一个ip
                        requestIp = ".".join(map(str, requestIp))  # 组合出来一个新的真实请求ip
                        sql = 'tcping.exe ' + requestIp+' 80'
                        print count, '/', len(tables), ':', sql
                        requestCount += 1
                        output = os.popen(sql)
                        a = output.read()
                        print a

                        # if ('请求超时'.decode('utf-8').encode('gbk') in a or '过期'.decode('utf-8').encode('gbk')  in a)and('回复'.decode('utf-8').encode('gbk') not in a): # 编码问题很烦人
                        if ('Average =' not in a): # 编码问题很烦人
                            status = 0
                        else:
                            temp = re.findall(r'\d+\.\d+ms', a)  # 将ping命令的返回值中的所有时间值获取到
                            temp = str(temp[-1])
                            status = 1
                        # 判断是否有参数的返回
                        if status==1:
                            temptime.append(float(re.findall(r'\d+\.\d+ms', temp)[0]))  # 将ping命令的返回值中的平均时间记录下来
                            print temptime[-1]  # 打印最后一条的信息
                    time.append(averagenum(temptime))
                    count = count +1
                except Exception as e:
                    logging.error(e)
                    time.append(0)
                    count = count + 1
                    print e,'----'
                if (count%3) == 0:
                    try:
                        data = open_excel(file)
                        rows = data.sheets()[0].nrows
                        excel = copy(data)  # 将copy方法将xlrd的对象转化为xlwt的对象
                        table = excel.get_sheet(0)  # 用xlwt对象的方法获得要操作的sheet
                        everyWrite = 3 # 每次写的行数
                        for i in range(everyWrite):
                            table.write(i+(count-everyWrite), 6, time[i+(count-everyWrite)])  # 参数分别是 行 列 值
                        excel.save('result\\time.xls')
                    except Exception as e:
                        print e
    #数据写
    data = open_excel(file)
    rows = data.sheets()[0].nrows
    excel = copy(data)                      # 将copy方法将xlrd的对象转化为xlwt的对象
    table = excel.get_sheet(0)              # 用xlwt对象的方法获得要操作的sheet
    for i in range(rows):
        table.write(i,6,time[i]) # 参数分别是 行 列 值
    excel.save('result\\time.xls')
def excel_table_byname(file , colnameindex=0, by_name=u'Sheet1'):
    data = open_excel(file)                 # 打开excel文件
    table = data.sheet_by_name(by_name)     # 根据sheet名字来获取excel中的sheet
    nrows = table.nrows  # 行数
    colnames = table.row_values(colnameindex)  # 某一行数据
    list =[]                                   #  装读取结果的序列
    for rownum in range(0, nrows):           # 遍历每一行的内容
         row = table.row_values(rownum)      # 根据行号获取行
         if row: # 如果行存在
             app = [] # 一行的内容
             for i in range(len(colnames)): # 一列列地读取行的内容
                app.append(row[i])
             list.append(app)                #装载数据
    return list

def main():
    print '正在开始工作.....'.decode('utf-8').encode('gbk')
    write_excel()

if __name__ == '__main__':
    main()
