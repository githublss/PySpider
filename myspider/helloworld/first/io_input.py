#!/usr/bin/env python
# -*- coding:utf-8 -*-
import re

# 检测回文诗
def reverse(text):
    # re.sub('[,./@#%$%^&*()_+]', text)

    return (re.sub("[,./@#%$^&*()_+" "]",'', text).lower()).replace(' ','')[::-1]

def is_palindrom(text):
    return re.sub("[,./@#%$^&*()_+" "]",'', text).lower().replace(' ','') == reverse(text)


something = input('enput something:-->')
if is_palindrom(something):
    print('yes,it is a palindrom')
else:
    print('no,it is not palindrom')