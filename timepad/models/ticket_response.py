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
from timepad.models.attendance_response import AttendanceResponse  # noqa: F401,E501
from timepad.models.codes_response import CodesResponse  # noqa: F401,E501
from timepad.models.place_response import PlaceResponse  # noqa: F401,E501
from timepad.models.ticket_type_response import TicketTypeResponse  # noqa: F401,E501


class TicketResponse(object):
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
        'id': 'int',
        'number': 'str',
        'price_nominal': 'float',
        'answers': 'dict(str, str)',
        'ticket_type': 'TicketTypeResponse',
        'attendance': 'AttendanceResponse',
        'place': 'PlaceResponse',
        'codes': 'CodesResponse',
        'personal_link': 'str',
        'eticket_link': 'str'
    }

    attribute_map = {
        'id': 'id',
        'number': 'number',
        'price_nominal': 'price_nominal',
        'answers': 'answers',
        'ticket_type': 'ticket_type',
        'attendance': 'attendance',
        'place': 'place',
        'codes': 'codes',
        'personal_link': 'personal_link',
        'eticket_link': 'eticket_link'
    }

    def __init__(self, id=None, number=None, price_nominal=None, answers=None, ticket_type=None, attendance=None, place=None, codes=None, personal_link=None, eticket_link=None):  # noqa: E501
        """TicketResponse - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._number = None
        self._price_nominal = None
        self._answers = None
        self._ticket_type = None
        self._attendance = None
        self._place = None
        self._codes = None
        self._personal_link = None
        self._eticket_link = None
        self.discriminator = None
        self.id = id
        if number is not None:
            self.number = number
        if price_nominal is not None:
            self.price_nominal = price_nominal
        self.answers = answers
        self.ticket_type = ticket_type
        if attendance is not None:
            self.attendance = attendance
        if place is not None:
            self.place = place
        if codes is not None:
            self.codes = codes
        if personal_link is not None:
            self.personal_link = personal_link
        if eticket_link is not None:
            self.eticket_link = eticket_link

    @property
    def id(self):
        """Gets the id of this TicketResponse.  # noqa: E501

        Уникальный номер билета  # noqa: E501

        :return: The id of this TicketResponse.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TicketResponse.

        Уникальный номер билета  # noqa: E501

        :param id: The id of this TicketResponse.  # noqa: E501
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def number(self):
        """Gets the number of this TicketResponse.  # noqa: E501

        Номер билета  # noqa: E501

        :return: The number of this TicketResponse.  # noqa: E501
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this TicketResponse.

        Номер билета  # noqa: E501

        :param number: The number of this TicketResponse.  # noqa: E501
        :type: str
        """

        self._number = number

    @property
    def price_nominal(self):
        """Gets the price_nominal of this TicketResponse.  # noqa: E501

        Номинальная цена билета на момент покупки. ВНИМАНИЕ! Эта цена не учитывает начисленные скидки на заказ и является ценой заказанной категории билета на момент его оплаты.  # noqa: E501

        :return: The price_nominal of this TicketResponse.  # noqa: E501
        :rtype: float
        """
        return self._price_nominal

    @price_nominal.setter
    def price_nominal(self, price_nominal):
        """Sets the price_nominal of this TicketResponse.

        Номинальная цена билета на момент покупки. ВНИМАНИЕ! Эта цена не учитывает начисленные скидки на заказ и является ценой заказанной категории билета на момент его оплаты.  # noqa: E501

        :param price_nominal: The price_nominal of this TicketResponse.  # noqa: E501
        :type: float
        """

        self._price_nominal = price_nominal

    @property
    def answers(self):
        """Gets the answers of this TicketResponse.  # noqa: E501

        Объект с ответами на вопросы анкеты  # noqa: E501

        :return: The answers of this TicketResponse.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._answers

    @answers.setter
    def answers(self, answers):
        """Sets the answers of this TicketResponse.

        Объект с ответами на вопросы анкеты  # noqa: E501

        :param answers: The answers of this TicketResponse.  # noqa: E501
        :type: dict(str, str)
        """
        if answers is None:
            raise ValueError("Invalid value for `answers`, must not be `None`")  # noqa: E501

        self._answers = answers

    @property
    def ticket_type(self):
        """Gets the ticket_type of this TicketResponse.  # noqa: E501


        :return: The ticket_type of this TicketResponse.  # noqa: E501
        :rtype: TicketTypeResponse
        """
        return self._ticket_type

    @ticket_type.setter
    def ticket_type(self, ticket_type):
        """Sets the ticket_type of this TicketResponse.


        :param ticket_type: The ticket_type of this TicketResponse.  # noqa: E501
        :type: TicketTypeResponse
        """
        if ticket_type is None:
            raise ValueError("Invalid value for `ticket_type`, must not be `None`")  # noqa: E501

        self._ticket_type = ticket_type

    @property
    def attendance(self):
        """Gets the attendance of this TicketResponse.  # noqa: E501


        :return: The attendance of this TicketResponse.  # noqa: E501
        :rtype: AttendanceResponse
        """
        return self._attendance

    @attendance.setter
    def attendance(self, attendance):
        """Sets the attendance of this TicketResponse.


        :param attendance: The attendance of this TicketResponse.  # noqa: E501
        :type: AttendanceResponse
        """

        self._attendance = attendance

    @property
    def place(self):
        """Gets the place of this TicketResponse.  # noqa: E501


        :return: The place of this TicketResponse.  # noqa: E501
        :rtype: PlaceResponse
        """
        return self._place

    @place.setter
    def place(self, place):
        """Sets the place of this TicketResponse.


        :param place: The place of this TicketResponse.  # noqa: E501
        :type: PlaceResponse
        """

        self._place = place

    @property
    def codes(self):
        """Gets the codes of this TicketResponse.  # noqa: E501


        :return: The codes of this TicketResponse.  # noqa: E501
        :rtype: CodesResponse
        """
        return self._codes

    @codes.setter
    def codes(self, codes):
        """Sets the codes of this TicketResponse.


        :param codes: The codes of this TicketResponse.  # noqa: E501
        :type: CodesResponse
        """

        self._codes = codes

    @property
    def personal_link(self):
        """Gets the personal_link of this TicketResponse.  # noqa: E501

        Персональная ссылка  # noqa: E501

        :return: The personal_link of this TicketResponse.  # noqa: E501
        :rtype: str
        """
        return self._personal_link

    @personal_link.setter
    def personal_link(self, personal_link):
        """Sets the personal_link of this TicketResponse.

        Персональная ссылка  # noqa: E501

        :param personal_link: The personal_link of this TicketResponse.  # noqa: E501
        :type: str
        """

        self._personal_link = personal_link

    @property
    def eticket_link(self):
        """Gets the eticket_link of this TicketResponse.  # noqa: E501

        Ссылка на электронный билет  # noqa: E501

        :return: The eticket_link of this TicketResponse.  # noqa: E501
        :rtype: str
        """
        return self._eticket_link

    @eticket_link.setter
    def eticket_link(self, eticket_link):
        """Sets the eticket_link of this TicketResponse.

        Ссылка на электронный билет  # noqa: E501

        :param eticket_link: The eticket_link of this TicketResponse.  # noqa: E501
        :type: str
        """

        self._eticket_link = eticket_link

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
        if issubclass(TicketResponse, dict):
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
        if not isinstance(other, TicketResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
