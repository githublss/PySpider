#!/usr/bin/env python
# -*- coding:utf-8 -*-


def maximum(x, y):
    if x > y:
        return x
    elif x == y:
        return 'the number are equal'
    else:
        return y

print(maximum(2, 2))

def print_max(x, y):
    """print the maximum of two number
    the two values must be integers"""
    x = int(x)
    y = int(y)
    if x > y:
        print(x, 'is maximum')
    else:
        print(y, 'is maximum')

print_max(3, 5)
print(print_max.__doc__)