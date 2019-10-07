# -*- coding: utf-8 -*-
"""
API client fpr Timepad service.
Documentation for the API : http://dev.timepad.ru

Swagger UI: https://api.timepad.ru/doc/interactive/
"""

__author__ = """Vladimir Protasov"""
__version__ = '0.1.0'


class Api:
    def __init__(self, token):
        self.token = token
