#!/usr/bin/env python
# -*- coding:utf-8 -*-

number = 23
running = True
while running:
    guess = int(input('Enter an integer:>'))

    if guess == number:
        print('congratulations, you guessed it')

        running = False
    elif guess < number:
        print('no, it is a little higher than that.')

    else:
        print('no, it is a little lower than that.')
else:
    print('the while loop is over.')
print('done')