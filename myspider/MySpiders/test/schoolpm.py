#!/usr/bin/env python
# -*- coding:utf-8 -*-
import re

patter = re.compile(r'年\d+月')
patter2 = re.compile(r'\d+')
mas = patter.findall('2109年12月')
for ma in mas:
    print patter2.findall(ma)