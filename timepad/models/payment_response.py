# coding: utf-8

"""
    Timepad API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class PaymentResponse(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'amount': 'float',
        'paid_at': 'date',
        'payment_type': 'str',
        'payment_link': 'str'
    }

    attribute_map = {
        'amount': 'amount',
        'paid_at': 'paid_at',
        'payment_type': 'payment_type',
        'payment_link': 'payment_link'
    }

    def __init__(self, amount=None, paid_at=None, payment_type=None, payment_link=None):  # noqa: E501
        """PaymentResponse - a model defined in Swagger"""  # noqa: E501
        self._amount = None
        self._paid_at = None
        self._payment_type = None
        self._payment_link = None
        self.discriminator = None
        self.amount = amount
        if paid_at is not None:
            self.paid_at = paid_at
        if payment_type is not None:
            self.payment_type = payment_type
        if payment_link is not None:
            self.payment_link = payment_link

    @property
    def amount(self):
        """Gets the amount of this PaymentResponse.  # noqa: E501

        Оплаченная сумма (количество рублей, отданных покупателем платёжной системе в этом заказе)  # noqa: E501

        :return: The amount of this PaymentResponse.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this PaymentResponse.

        Оплаченная сумма (количество рублей, отданных покупателем платёжной системе в этом заказе)  # noqa: E501

        :param amount: The amount of this PaymentResponse.  # noqa: E501
        :type: float
        """
        if amount is None:
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501

        self._amount = amount

    @property
    def paid_at(self):
        """Gets the paid_at of this PaymentResponse.  # noqa: E501

        Дата оплаты  # noqa: E501

        :return: The paid_at of this PaymentResponse.  # noqa: E501
        :rtype: date
        """
        return self._paid_at

    @paid_at.setter
    def paid_at(self, paid_at):
        """Sets the paid_at of this PaymentResponse.

        Дата оплаты  # noqa: E501

        :param paid_at: The paid_at of this PaymentResponse.  # noqa: E501
        :type: date
        """

        self._paid_at = paid_at

    @property
    def payment_type(self):
        """Gets the payment_type of this PaymentResponse.  # noqa: E501

        Платёжная система оплаты  # noqa: E501

        :return: The payment_type of this PaymentResponse.  # noqa: E501
        :rtype: str
        """
        return self._payment_type

    @payment_type.setter
    def payment_type(self, payment_type):
        """Sets the payment_type of this PaymentResponse.

        Платёжная система оплаты  # noqa: E501

        :param payment_type: The payment_type of this PaymentResponse.  # noqa: E501
        :type: str
        """

        self._payment_type = payment_type

    @property
    def payment_link(self):
        """Gets the payment_link of this PaymentResponse.  # noqa: E501

        Ссылка на оплату  # noqa: E501

        :return: The payment_link of this PaymentResponse.  # noqa: E501
        :rtype: str
        """
        return self._payment_link

    @payment_link.setter
    def payment_link(self, payment_link):
        """Sets the payment_link of this PaymentResponse.

        Ссылка на оплату  # noqa: E501

        :param payment_link: The payment_link of this PaymentResponse.  # noqa: E501
        :type: str
        """

        self._payment_link = payment_link

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(PaymentResponse, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PaymentResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
