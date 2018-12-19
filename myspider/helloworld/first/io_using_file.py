#!/usr/bin/env python
# -*- coding:utf-8 -*-
#文件的读写
from datetime import time, datetime

poem = '''\
Programming is fun
When the work is done
if you wanna make your work also fun:
use Python!
'''
f = open(r"C:\My Documents\测试1.txt", 'a')
f.write(poem)

f.write(datetime.now().strftime('%Y-%m-%d %H:%M:%S')+'\n\n')
f.close()

f = open(r"C:\My Documents\测试1.txt")
lines = f.readlines()
for line in lines:
    print(line,end=" ")

f.close()