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


class LocationResponse(object):
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
        'country': 'str',
        'city': 'str',
        'address': 'str',
        'coordinates': 'list[float]'
    }

    attribute_map = {
        'country': 'country',
        'city': 'city',
        'address': 'address',
        'coordinates': 'coordinates'
    }

    def __init__(self, country=None, city=None, address=None, coordinates=None):  # noqa: E501
        """LocationResponse - a model defined in Swagger"""  # noqa: E501
        self._country = None
        self._city = None
        self._address = None
        self._coordinates = None
        self.discriminator = None
        self.country = country
        self.city = city
        self.address = address
        self.coordinates = coordinates

    @property
    def country(self):
        """Gets the country of this LocationResponse.  # noqa: E501

        Название страны  # noqa: E501

        :return: The country of this LocationResponse.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this LocationResponse.

        Название страны  # noqa: E501

        :param country: The country of this LocationResponse.  # noqa: E501
        :type: str
        """
        if country is None:
            raise ValueError("Invalid value for `country`, must not be `None`")  # noqa: E501

        self._country = country

    @property
    def city(self):
        """Gets the city of this LocationResponse.  # noqa: E501

        Название города  # noqa: E501

        :return: The city of this LocationResponse.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this LocationResponse.

        Название города  # noqa: E501

        :param city: The city of this LocationResponse.  # noqa: E501
        :type: str
        """
        if city is None:
            raise ValueError("Invalid value for `city`, must not be `None`")  # noqa: E501

        self._city = city

    @property
    def address(self):
        """Gets the address of this LocationResponse.  # noqa: E501

        Адрес проведения события  # noqa: E501

        :return: The address of this LocationResponse.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this LocationResponse.

        Адрес проведения события  # noqa: E501

        :param address: The address of this LocationResponse.  # noqa: E501
        :type: str
        """
        if address is None:
            raise ValueError("Invalid value for `address`, must not be `None`")  # noqa: E501

        self._address = address

    @property
    def coordinates(self):
        """Gets the coordinates of this LocationResponse.  # noqa: E501

        Широта и долгота для карт  # noqa: E501

        :return: The coordinates of this LocationResponse.  # noqa: E501
        :rtype: list[float]
        """
        return self._coordinates

    @coordinates.setter
    def coordinates(self, coordinates):
        """Sets the coordinates of this LocationResponse.

        Широта и долгота для карт  # noqa: E501

        :param coordinates: The coordinates of this LocationResponse.  # noqa: E501
        :type: list[float]
        """
        if coordinates is None:
            raise ValueError("Invalid value for `coordinates`, must not be `None`")  # noqa: E501

        self._coordinates = coordinates

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
        if issubclass(LocationResponse, dict):
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
        if not isinstance(other, LocationResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other