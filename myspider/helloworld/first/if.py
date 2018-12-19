#!/usr/bin/env python
# -*- coding:utf-8 -*-

number = 23
guess = int(input('Enter an integer : '))

if guess == number:
    print('congratulations, you guessed it.')
    print('(but you do not win any prizes!)')
elif guess < number:
    print('no, it is a little higher then that')
else:
    print('no, it is a little lower then that')

print('done')