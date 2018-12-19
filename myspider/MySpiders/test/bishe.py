#!/usr/bin/env python
# -*- coding:utf-8 -*-
import ast
import urllib2
import urllib
from pyecharts import Bar,Line,WordCloud,Radar
import sys,re
from bs4 import BeautifulSoup
import json
import jsonpath
import requests
import MySQLdb
import time

#获取网页数据
def loadPage(url,i,time):
    try:
        print ("正在加载%s第%d页..." % (time,i))
        sess = requests.Session()
        headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"}
        html = sess.get(url, headers=headers)  # 获取session
        formata = {"PageIndex": i,"PageSize": 20,"Month": time,"KindClassId": 36}
        response = sess.post("http://top.aiweibang.com/rank/getaccountrank", data=formata, headers=headers)
        html2 = response.text
        # print html2
        return html2
    except:
        return '爬取失败'


# 将HTML中的数据添加进ulist数组中,
def writePage(html):
    datalist = []
    for i in range(len(json.loads(html).get("data").get("data"))):      #通过json.loads将json数据转化为Python数据类型
        data = (json.loads(html).get("data").get("data"))[i]
        relay = (data.get('UserName'),data.get('ReadNumSum'),data.get('LikeNumSum'),
                 data.get('ReadNumAvg'),data.get('ReadNumMax'),data.get('BangIndex'))
        datalist.append([relay[0],relay[1],relay[2],relay[3],relay[4],relay[5]])
    return datalist


# 将ulist中的数据保存到mysql数据库中,
def data2mysql(ulist,t):
    conn = MySQLdb.Connect(host='127.0.0.1',
                           port=3306,
                           user='root',
                           passwd='',
                           db='bishe',
                           charset='utf8')  #建立一个数据库连接对象
    cursor = conn.cursor()  #建立一个数据库交互对象cursor
    if (t==1):
        for i in range(len(ulist)):
            u = ulist[i]
            sql_insert = "INSERT INTO DATA1(UserName,ReadNumSum,LikeNumSum,ReadNumAvg,ReadNumMax,BangIndex) " \
                         "VALUES ('%s','%s','%s','%d','%d','%f')" % (str(u[0]),str(u[1]),str(u[2]),u[3],u[4],u[5])
            print "check_insert_available:"+ sql_insert
            cursor.execute(sql_insert)  #执行SQL语句
    if (t==2):
        for i in range(len(ulist)):
            u = ulist[i]
            sql_insert = "INSERT INTO DATA2(UserName,ReadNumSum,LikeNumSum,ReadNumAvg,ReadNumMax,BangIndex) " \
                         "VALUES ('%s','%s','%s','%d','%d','%f')" % (str(u[0]),str(u[1]),str(u[2]),u[3],u[4],u[5])
            print "check_insert_available:"+ sql_insert
            cursor.execute(sql_insert)  #执行SQL语句
    if (t==3):
        for i in range(len(ulist)):
            u = ulist[i]
            sql_insert = "INSERT INTO DATA3(UserName,ReadNumSum,LikeNumSum,ReadNumAvg,ReadNumMax,BangIndex) " \
                         "VALUES ('%s','%s','%s','%d','%d','%f')" % (str(u[0]),str(u[1]),str(u[2]),u[3],u[4],u[5])
            print "check_insert_available:"+ sql_insert
            cursor.execute(sql_insert)  #执行SQL语句
    if (t==4):
        for i in range(len(ulist)):
            u = ulist[i]
            sql_insert = "INSERT INTO DATA4(UserName,ReadNumSum,LikeNumSum,ReadNumAvg,ReadNumMax,BangIndex) " \
                         "VALUES ('%s','%s','%s','%d','%d','%f')" % (str(u[0]),str(u[1]),str(u[2]),u[3],u[4],u[5])
            print "check_insert_available:"+ sql_insert
            cursor.execute(sql_insert)  #执行SQL语句
    if (t==5):
        for i in range(len(ulist)):
            u = ulist[i]
            sql_insert = "INSERT INTO DATA5(UserName,ReadNumSum,LikeNumSum,ReadNumAvg,ReadNumMax,BangIndex) " \
                         "VALUES ('%s','%s','%s','%d','%d','%f')" % (str(u[0]),str(u[1]),str(u[2]),u[3],u[4],u[5])
            print "check_insert_available:"+ sql_insert
            cursor.execute(sql_insert)  #执行SQL语句
    conn.commit()   #正常结束事务
    print '成功保存'
    cursor.close()
    conn.close()

#将获取到的数据进行格式转化
def strData2int():
    conn = MySQLdb.Connect(host='127.0.0.1',
                           port=3306,
                           user='root',
                           passwd='',
                           db='bishe',
                           charset='utf8')
    cursor1 = conn.cursor()
    cursor2 = conn.cursor()
    cursor4 = conn.cursor()
    cursor4.execute("truncate NEWDATA1")
    cursor4.execute("truncate NEWDATA2")
    cursor4.execute("truncate NEWDATA3")
    cursor4.execute("truncate NEWDATA4")
    cursor4.execute("truncate NEWDATA5")
    for t in range(5):
        t=t+1
        if (t == 1):
            sql_select = "select * from DATA1 "
        if (t == 2):
            sql_select = "select * from DATA2 "
        if (t == 3):
            sql_select = "select * from DATA3 "
        if (t == 4):
            sql_select = "select * from DATA4 "
        if (t == 5):
            sql_select = "select * from DATA5 "
        cursor1.execute(sql_select)
        print '选取的总数为:', cursor1.rowcount  # 获取返回数据总条数
        regex = re.compile(r'\d+')
        for i in range(cursor1.rowcount):
            rs = cursor1.fetchone()
            RNS = (int(regex.search(rs[2]).group())*10000)
            LNS = (int(regex.search(rs[3]).group()) * 10000 if ('万' in rs[3]) else int(regex.search(rs[3]).group()))    #通过正则表达式将数据进行处理，达到要求
            u = [rs[0],rs[1], RNS, LNS, rs[4], rs[5],rs[6]]
            if (t == 1):
                sql_insert = "INSERT INTO NEWDATA1(UserName,ReadNumSum,LikeNumSum,ReadNumAvg,ReadNumMax,BangIndex) " \
                             "VALUES ('%s','%d','%d','%d','%d','%f')" % (u[1], u[2], u[3], u[4], u[5], u[6])
            if (t == 2):
                sql_insert = "INSERT INTO NEWDATA2(UserName,ReadNumSum,LikeNumSum,ReadNumAvg,ReadNumMax,BangIndex) " \
                             "VALUES ('%s','%d','%d','%d','%d','%f')" % (u[1], u[2], u[3], u[4], u[5], u[6])
            if (t == 3):
                sql_insert = "INSERT INTO NEWDATA3(UserName,ReadNumSum,LikeNumSum,ReadNumAvg,ReadNumMax,BangIndex) " \
                             "VALUES ('%s','%d','%d','%d','%d','%f')" % (u[1], u[2], u[3], u[4], u[5], u[6])
            if (t == 4):
                sql_insert = "INSERT INTO NEWDATA4(UserName,ReadNumSum,LikeNumSum,ReadNumAvg,ReadNumMax,BangIndex) " \
                             "VALUES ('%s','%d','%d','%d','%d','%f')" % (u[1], u[2], u[3], u[4], u[5], u[6])
            if (t == 5):
                sql_insert = "INSERT INTO NEWDATA5(UserName,ReadNumSum,LikeNumSum,ReadNumAvg,ReadNumMax,BangIndex) " \
                             "VALUES ('%s','%d','%d','%d','%d','%f')" % (u[1], u[2], u[3], u[4], u[5], u[6])
            print "check_insert_available:"+ sql_insert
            cursor2.execute(sql_insert)  #执行SQL语句

    cursor3 = conn.cursor()
    # sql_updata_BangIndex = "call updata_BangIndex"  #执行提前写好的存储过程,对每一个微信公众号进行打分...
    # cursor3.execute(sql_updata_BangIndex)
    print "分数已经打好"
    conn.commit()  # 正常结束事务
    print '成功保存'
    cursor1.close()
    cursor2.close()
    cursor3.close()
    cursor4.close()
    conn.close()

# 数据的可视化
def mysqldataShow():
    conn = MySQLdb.Connect(host='127.0.0.1',
                           port=3306,
                           user='root',
                           passwd='',
                           db='bishe',
                           charset='utf8')
    cursor1 = conn.cursor()
    #通过计算得分以后的分数进行查询并且排序
    sql_select = "select(@i:=@i+1)as rank,UserName , readnumsum,likenumsum,readnumavg,readnummax,bangindex " \
                 "from newdata1 a,(select@i:=0)b order by Bangindex desc;"
    cursor1.execute(sql_select)
    print '选取的总数为:', cursor1.rowcount    #获取返回数据总条数
    UserName = []
    ReadNumSum = []
    LikeNumSum = []
    ReadNumMax=[]
    ReadNumAvg=[]
    BangIndex=[]

    for i in range(cursor1.rowcount):
        rs = cursor1.fetchone()
        UserName.append(rs[1])
        ReadNumSum.append(rs[2])
        LikeNumSum.append(rs[3])
        ReadNumAvg.append(rs[4])
        ReadNumMax.append(rs[5])
        BangIndex.append(rs[6])
    print UserName
    # 生成柱状图,包括得分
    bar1=Bar("公众号排名",width=1500,height=720,page_title='rank',background_color='#F5F5F5')
    bar1.add("综合排名", UserName, BangIndex,is_datazoom_show=True,datazoom_type='both',is_toolbox_show=True)
    bar1.show_config()
    bar1.render(r"C:\Users\lss\Desktop\rank.html")

    # 生成柱状图,包括阅读最高数,阅读平均数,总阅读数,点赞数
    bar2 = Bar("公众号详细分析", width=1500, height=720,page_title='analysis',background_color='#F5F5F5')
    bar2.add("阅读最高数", UserName, ReadNumMax, is_convert=True, mark_line=["average"], mark_point=["max", "min"],
             is_toolbox_show=True)
    bar2.add("阅读平均数", UserName, ReadNumAvg, is_datazoom_show=True, datazoom_type='both',
             datazoom_range=[10, 25], is_toolbox_show=True, mark_line=["average"], mark_point=["max", "min"])
    bar2.add("文章点赞数", UserName, LikeNumSum, mark_line=["average"], mark_point=["max", "min"],
             is_toolbox_show=True)
    bar2.add("文章阅读总数", UserName, ReadNumSum, mark_line=["average"], mark_point=["max", "min"],
             is_toolbox_show=True)
    bar2.show_config()
    bar2.render(r"C:\Users\lss\Desktop\fenxi.html")

    # 生成云图
    wordcloud = WordCloud(width=1500,height=720,page_title='cloud',background_color='#F5F5F5')
    wordcloud.add("公众号",UserName,BangIndex,word_gap=30,word_size_range=[9,100],shape="circle")
    wordcloud.render(r"C:\Users\lss\Desktop\cloud.html")

    # 对最近一个月排名前10的微信公众号进行排名趋势分析
    sql_Tenselect = "select newdata1.username,newdata1.rank as a,newdata2.rank as b," \
                    "newdata3.rank as c,newdata4.rank as d,newdata5.rank as e " \
                    "from newdata1,newdata2,newdata3, newdata4,newdata5 " \
                    "where newdata1.username=newdata2.username " \
                    "and newdata2.username=newdata3.username " \
                    "and newdata3.username=newdata4.username " \
                    "and newdata4.username=newdata5.username " \
                    "and newdata5.rank in (1,2,3,4,5,6,7,8,9,10)"
    cursor2 = conn.cursor()
    cursor2.execute(sql_Tenselect)
    riqi = ["五月前","四月前","三月前","两月前","一月前"]
    line = Line('公众号排名趋势',width=1500,height=720,page_title='line',background_color='#F5F5F5')
    for i in range(cursor2.rowcount):
        rs2 = cursor2.fetchone()
        rank = [rs2[1],rs2[2],rs2[3],rs2[4],rs2[5]]
        line.add(rs2[0],riqi,rank,is_smooth=True,is_label_show=True,is_xaxis_boundarygap=True,mark_line=['max','min'],is_yaxis_inverse=True,xaxis_name='时间',yaxis_name='名次',xaxis_name_gap='end')
    line.render(r"C:\Users\lss\Desktop\everyone.html")

    # 通过雷达图对某个公众号分析
    sql_oneselect = "select username, readnumsum,likenumsum,readnumavg,readnummax from newdata5 where newdata5.rank<10"
    cursor3 = conn.cursor()
    cursor3.execute(sql_oneselect)
    rader = Radar(width=1500, height=720,page_title='leida',background_color='#F5F5F5')
    schema = [
        ("文章阅读总数", 1000000),("文章点赞数",31000),("阅读平均数",30000),("阅读最高数",110000)
    ]
    rader.config(schema,radar_text_color='#4682B4')
    for i in range(cursor3.rowcount):
        rs3 = cursor3.fetchone()
        rader.add(rs3[0],[[rs3[1],rs3[2],rs3[3],rs3[4]]],area_color="#4682B4",label_emphasis_textcolor="#4682B4")
    rader.render(r"C:\Users\lss\Desktop\one.html")

    cursor2.close()
    cursor1.close()
    conn.close()


# 将mysql中的数据读取出来
def mysql2data():
    tplt = '{:<25}\t{:<10}\t{:<10}\t{:<10}\t{:<10}\t{:<10}'
    conn = MySQLdb.Connect(host='127.0.0.1',
                           port=3306,
                           user='root',
                           passwd='',
                           db='bishe',
                           charset='utf8')
    cursor = conn.cursor()
    sql_select = "select * from NEWDATA5 "
    cursor.execute(sql_select)
    print '选取的总数为:',cursor.rowcount

    rs = cursor.fetchall()
    for row in rs:
        print ('{row[0]:{t}<4}{row[1]:{t}^20}{row[2]:{t}>10}{row[3]:{t}>10}{row[4]:{t}>10}{row[5]:{t}>10}{row[6]:>10}'.format(row=row,t=chr(11)))

    cursor.close()
    conn.close()


# 输出测试
def printUnivList(ulist):
    count = 0
    tplt = '{:<25}\t{:<10}\t{:<10}\t{:<10}\t{:<10}\t{:<10}'
   # 定义输出模板为变量tplt，\t为横向制表符，<为左对齐，10为每列的宽度
    print(tplt.format('公众号','月阅读数','月点赞数','单篇平均阅读数','单篇最高阅读数','综合得分'))
   # format()方法做格式化输出
    for i in range(len(ulist)):
        u = ulist[i]
        count = count +1
        print count ,(tplt.format(u[0],u[1],u[2],u[3],u[4],u[5]))


#主调函数
def spider(url):
    times = ["2018-07-01T00:00:00","2018-08-01T00:00:00","2018-09-01T00:00:00","2018-10-01T00:00:00","2018-11-01T00:00:00"]
    t = 0
    for time_ in times:
        t = t+1
        time.sleep(1)     # 设置一个时间间隔,为了反爬虫的需要
        for i in range(10):
            html = loadPage(url,i+1,time_)
            temp = writePage(html)
            printUnivList(temp)
            data2mysql(temp,t)
    mysql2data()      #将mysql中的数据打印出来
    strData2int()       # 进行数据的转换
    mysqldataShow()
    pass

if __name__ == "__main__":
    reload(sys)     #为了下一行进行设置编码
    sys.setdefaultencoding('utf-8')
    url = "http://top.aiweibang.com/rank/account?t=2&tid=36"
    spider(url)