#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
import sys

print('the command line arguments are:')
for i in sys.argv:
    print(i)

print('\n\nthe pythonPath is', sys.path, '\n')
print(os.getcwd())