#!/usr/bin/env python
# -*- coding:utf-8 -*-
from BaseHandler import BaseHandler
import logging

class IndexHandler(BaseHandler):
    def get(self):
        logging.debug('this is debug')
        logging.info('this is info')
        logging.warning('this is waring')
        logging.error('this is error')
        print 'this is print msg'
        self.write('hello itcast')