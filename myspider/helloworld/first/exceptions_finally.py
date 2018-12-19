#!/usr/bin/env python
# -*- coding:utf-8 -*-


import sys, time
f = None
try:
    f = open(r"C:\My Documents\test2.txt", encoding='utf-8')
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        print(line)
        # sys.stdout.flush()
        print('press ctrl + c now')
        time.sleep(2)
except IOError:
    print('can not find the file test2.txt ')
except KeyboardInterrupt:
    print("!!!!!YOU input a interrupt")
finally:
    if f:
        f.close()
    print("clear up:closed the file of you open.")