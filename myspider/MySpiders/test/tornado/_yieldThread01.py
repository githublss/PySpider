#!/usr/bin/env python
# -*- coding:utf-8 -*-
import time

import thread
gen = None      # 全局生成器，供给long_io使用

"""协程异步初级版本"""
def long_io():
    """模拟长延时操作"""
    def fun():
        print 'start longIO'
        global gen
        time.sleep(5)
        try:
            print 'finish longIO, and send result of return, continue exe'
            gen.send('io result is OK')
        except StopIteration:
            pass
    thread.start_new_thread(fun, ())

def on_finish(ret):
    """回调函数，a的收尾工作"""
    print 'start callback'
    ret = yield 
    print 'result is %s' % ret
    print 'finish callback'

def req_a():
    """模拟第一个请求"""
    print 'start request A'
    ret = yield long_io()
    print 'ret:%s' % ret
    print 'finish request A'

def req_b():
    """模拟第二个请求"""
    print 'start request B'
    time.sleep(2)
    print 'finish request B'


def main():
    """模拟tornado处理"""
    global gen
    gen = req_a()
    gen.next()  # 开启生成器req_a的执行
    req_b()
    # time.sleep(6)
    # print 'main is over...buy_buy'
    while 1:
        pass


if __name__ == '__main__':
    print "begin...."
    main()