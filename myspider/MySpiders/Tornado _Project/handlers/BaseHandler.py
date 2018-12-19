#!/usr/bin/env python
# -*- coding:utf-8 -*-
from tornado.web import RequestHandler

class BaseHandler(RequestHandler):
    """自定义基类"""

    # @property   #成员方法作为属性对待
    # def db(self):
    #     return self.application.db
    #
    # @property   # 这里装饰器的作用有遗忘，
    # def redis(self):
    #     return self.application.redis

    def prepare(self):
        pass

    def set_default_headers(self):
        pass

    # def write_error(self, status_code, **kwargs):
    #     pass

    def initialize(self):
        pass

    def on_finish(self):
        pass