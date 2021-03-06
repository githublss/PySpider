#!/usr/bin/env python
# -*- coding:utf-8 -*-
import time

import thread
gen = None      # 全局生成器，供给long_io使用

"""协程异步最终版本"""
def gen_coroutine(f):
    def wrapper(*args, **kwargs):
        gen_f = f()         # gen_f为生成器req_a
        r = gen_f.next()    # r是生成器long_io
        def fun(g):
            ret = g.next()
            try:
                gen_f.send(ret)
            except StopIteration:
                pass
        thread.start_new_thread(fun,(r,))
    print '呼叫装饰器'
    return wrapper


def long_io():
    """模拟长延时操作"""
    print 'start LongIo'
    time.sleep(5)
    print 'finish LongIO, yield result'
    yield 'io result'


def on_finish(ret):
    """回调函数，a的收尾工作"""
    print 'start callback'
    ret = yield 
    print 'result is %s' % ret
    print 'finish callback'


@gen_coroutine
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
    req_a()
    req_b()
    # time.sleep(6)
    # print 'main is over...buy_buy'
    while 1:
        pass


if __name__ == '__main__':
    print "begin...."       # 输出结果很是诧异！！！没有弄明白
    print '123'
    main()