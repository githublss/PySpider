#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import time

source = ['"C:\My Documents"', 'C:\\TEMP']

target_dir = 'E:\\Backup'

if not os.path.exists(target_dir):
    os.mkdir(target_dir)

today = target_dir + os.sep + time.strftime('%Y%m%d')

now = time.strftime('%H%M%S')

comment = input('enter a comment ---> ')

if len(comment) == 0:
    targer = today + os.sep + now + 'zip'
else:
    targer = today + os.sep + now + '_' + comment.replace(' ', '_') + '.zip'


if not os.path.exists(today):
    os.mkdir(today)
    print('successfully creatde directory ', today)

zip_command = "zip -r -v {0} {1}".format(targer,' '.join(source))

print('zip command is:')
print(zip_command)
print('running:')
if os.system(zip_command) == 0: # zip成功执行后会返回一个0
    print('successfully backup to', targer)
else:
    print('backup failed')