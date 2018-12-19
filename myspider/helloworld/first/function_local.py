#!/usr/bin/env python
# -*- coding:utf-8 -*-

x = 50


def func():
    global x
    print("x is ", x)
    x = 2
    print('changed local x to ', x)

func()
print('x is still', x)