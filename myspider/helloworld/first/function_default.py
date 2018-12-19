#!/usr/bin/env python
# -*- coding:utf-8 -*-


def say(message, times=1):
    print(message * times)

say('hello')
say('hello ', 4)

def func(a, b=5, c=10):
    print('a is ', a, 'and b is ', b, 'and c is', c)

func(3, 7)
func(25, c=24)
func(c=50, a=100)