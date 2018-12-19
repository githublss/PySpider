#!/usr/bin/env python
# -*- coding:utf-8 -*-

import io

f = io.open(r"C:\My Documents\test2.txt",'w',encoding='utf-8')
f.write(u'我要尝试写入一些非英文字母\n1234\nmy name is lss')
f.close()

f = io.open(r"C:\My Documents\test2.txt",'r',encoding='utf-8')
lines = f.readlines()
for line in lines:
    print(line,end='')