#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import time

# 1.需要备份的文件与目录被指定在一个列表中
source = ['"C:\My Documents"','c:\\TEMP']

target_dir = 'E:\\Backup'

today = target_dir + os.sep + time.strftime('%Y%m%d')

now = time.strftime('%H%M%S')

# target = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'
target = today + os.sep +now +'.zip'
if not os.path.exists(target_dir):
    os.mkdir(target_dir) # 创建目录

if not os.path.exists(today):
   os.mkdir(today) # 创建目录
   print('successfully created directory', today)

zip_command = 'zip -r {0} {1}'.format(target, ' '.join(source))

print('zip command is:')
print(zip_command)
print("running:")
if os.system(zip_command) == 0:
    print('successful backup to', target)
else:
    print('backup failed')
