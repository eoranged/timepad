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


class CreateOrganization(object):
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
        'name': 'str',
        'subdomain': 'str',
        'phone': 'str'
    }

    attribute_map = {
        'name': 'name',
        'subdomain': 'subdomain',
        'phone': 'phone'
    }

    def __init__(self, name=None, subdomain=None, phone=None):  # noqa: E501
        """CreateOrganization - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._subdomain = None
        self._phone = None
        self.discriminator = None
        self.name = name
        self.subdomain = subdomain
        self.phone = phone

    @property
    def name(self):
        """Gets the name of this CreateOrganization.  # noqa: E501

        Название организации  # noqa: E501

        :return: The name of this CreateOrganization.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateOrganization.

        Название организации  # noqa: E501

        :param name: The name of this CreateOrganization.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def subdomain(self):
        """Gets the subdomain of this CreateOrganization.  # noqa: E501

        URL-идентификатор организации в Таймпаде (***.timepad.ru)  # noqa: E501

        :return: The subdomain of this CreateOrganization.  # noqa: E501
        :rtype: str
        """
        return self._subdomain

    @subdomain.setter
    def subdomain(self, subdomain):
        """Sets the subdomain of this CreateOrganization.

        URL-идентификатор организации в Таймпаде (***.timepad.ru)  # noqa: E501

        :param subdomain: The subdomain of this CreateOrganization.  # noqa: E501
        :type: str
        """
        if subdomain is None:
            raise ValueError("Invalid value for `subdomain`, must not be `None`")  # noqa: E501

        self._subdomain = subdomain

    @property
    def phone(self):
        """Gets the phone of this CreateOrganization.  # noqa: E501

        Телефон организатора  # noqa: E501

        :return: The phone of this CreateOrganization.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this CreateOrganization.

        Телефон организатора  # noqa: E501

        :param phone: The phone of this CreateOrganization.  # noqa: E501
        :type: str
        """
        if phone is None:
            raise ValueError("Invalid value for `phone`, must not be `None`")  # noqa: E501

        self._phone = phone

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
        if issubclass(CreateOrganization, dict):
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
        if not isinstance(other, CreateOrganization):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other