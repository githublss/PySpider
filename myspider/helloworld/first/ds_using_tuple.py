#!/usr/bin/env python
# -*- coding:utf-8 -*-

zoo = ('python', 'elephant', 'penguin')
print('number of animals in the zoo is', len(zoo))

new_zoo = 'monkey', 'camel', zoo
print('number of cages in ten new zoo is ',len(new_zoo))
print('all animals in new zoo are ', new_zoo)
print('from old zoo are', new_zoo[2])
print('last from old zoo is ', new_zoo[2][2])
print('number of animals in the new zoo is',
      len(new_zoo)-1+len(new_zoo[2]))