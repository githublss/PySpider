#!/usr/bin/env python
# -*- coding:utf-8 -*-
import time

import thread

"""回调异步"""
def long_io(on_finish):
    """模拟长延时操作"""
    def fun(callback):
        print 'start longIO'
        time.sleep(5)
        print 'finish longIO'
        callback('OK')
    thread.start_new_thread(fun, (on_finish,))

def on_finish(ret):
    """回调函数，a的收尾工作"""
    print 'start callback'
    print 'result is %s' % ret
    print 'finish callback'

def req_a():
    """模拟第一个请求"""
    print 'start request A'
    long_io(on_finish)
    print 'remove request A'

def req_b():
    """模拟第二个请求"""
    print 'start request B'
    time.sleep(2)
    print 'finish request B'


def main():
    """模拟tornado处理"""
    req_a()
    req_b()
    time.sleep(6)
    print 'main is over...buy_buy'


if __name__ == '__main__':
    print "begin...."
    main()