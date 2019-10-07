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


class EditOrderPayment(object):
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
        'paid_at': 'datetime',
        'amount': 'float',
        'payment_type': 'str'
    }

    attribute_map = {
        'paid_at': 'paid_at',
        'amount': 'amount',
        'payment_type': 'payment_type'
    }

    def __init__(self, paid_at=None, amount=None, payment_type=None):  # noqa: E501
        """EditOrderPayment - a model defined in Swagger"""  # noqa: E501
        self._paid_at = None
        self._amount = None
        self._payment_type = None
        self.discriminator = None
        if paid_at is not None:
            self.paid_at = paid_at
        if amount is not None:
            self.amount = amount
        if payment_type is not None:
            self.payment_type = payment_type

    @property
    def paid_at(self):
        """Gets the paid_at of this EditOrderPayment.  # noqa: E501

        Дата оплаты заказа  # noqa: E501

        :return: The paid_at of this EditOrderPayment.  # noqa: E501
        :rtype: datetime
        """
        return self._paid_at

    @paid_at.setter
    def paid_at(self, paid_at):
        """Sets the paid_at of this EditOrderPayment.

        Дата оплаты заказа  # noqa: E501

        :param paid_at: The paid_at of this EditOrderPayment.  # noqa: E501
        :type: datetime
        """

        self._paid_at = paid_at

    @property
    def amount(self):
        """Gets the amount of this EditOrderPayment.  # noqa: E501

        Сумма заказа  # noqa: E501

        :return: The amount of this EditOrderPayment.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this EditOrderPayment.

        Сумма заказа  # noqa: E501

        :param amount: The amount of this EditOrderPayment.  # noqa: E501
        :type: float
        """

        self._amount = amount

    @property
    def payment_type(self):
        """Gets the payment_type of this EditOrderPayment.  # noqa: E501

        Тип платежа  # noqa: E501

        :return: The payment_type of this EditOrderPayment.  # noqa: E501
        :rtype: str
        """
        return self._payment_type

    @payment_type.setter
    def payment_type(self, payment_type):
        """Sets the payment_type of this EditOrderPayment.

        Тип платежа  # noqa: E501

        :param payment_type: The payment_type of this EditOrderPayment.  # noqa: E501
        :type: str
        """

        self._payment_type = payment_type

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
        if issubclass(EditOrderPayment, dict):
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
        if not isinstance(other, EditOrderPayment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other