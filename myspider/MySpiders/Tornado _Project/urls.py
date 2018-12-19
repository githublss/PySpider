#!/usr/bin/env python
# -*- coding:utf-8 -*-
from handlers import Passport
urls = [
    (r"/", Passport.IndexHandler),
]