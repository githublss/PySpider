#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pickle

shoplistfile = r"C:\My Documents\test2.data"

shoplist = ['apple', 'banana', 'watermellen']

f = open(shoplistfile, 'wb')
pickle.dump(shoplist, f)
f.close()
del shoplist

f = open(shoplistfile,'rb')
shoplist = pickle.load(f)
print(shoplist)