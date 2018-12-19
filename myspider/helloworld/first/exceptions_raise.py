#!/usr/bin/env python
# -*- coding:utf-8 -*-


class ShortInputException(Exception):
    def __init__(self, length, atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast

try:
    text = input('Enter something--->')
    if len(text) < 3:
        raise ShortInputException(len(text), 3)
except EOFError:
    print('why you input a eoferror?')
except KeyboardInterrupt:
    print('You cancelled the operation.')
except ShortInputException as se:
    print(('you input {0} is too short,you must input at last {1}').format(se.length,se.atleast))
else:
    print('no exception is raise')