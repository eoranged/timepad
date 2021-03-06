# coding: utf-8

"""
    Timepad API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0

    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import timepad
from timepad.api.___api import _Api  # noqa: E501
from timepad.rest import ApiException


class Test_Api(unittest.TestCase):
    """_Api unit test stubs"""

    def setUp(self):
        self.api = _Api()  # noqa: E501

    def tearDown(self):
        pass

    def test_event_companies_list(self):
        """Test case for event_companies_list

        Получить список реквизитов компаний  # noqa: E501
        """
        pass

    def test_event_company(self):
        """Test case for event_company

        Получить реквизиты юрлица по ID  # noqa: E501
        """
        pass

    def test_event_company_payments(self):
        """Test case for event_company_payments

        Получить запросы на оплату от юрлица  # noqa: E501
        """
        pass

    def test_event_company_payments_0(self):
        """Test case for event_company_payments_0

        Получить запросы на оплату от юрлица по ID  # noqa: E501
        """
        pass

    def test_event_company_payments_1(self):
        """Test case for event_company_payments_1

        Получить выставленные счета  # noqa: E501
        """
        pass

    def test_event_company_payments_2(self):
        """Test case for event_company_payments_2

        Получить счет по ID  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
