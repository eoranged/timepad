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
from timepad.models.edit_order_attendance import EditOrderAttendance  # noqa: F401,E501


class EditOrderVisitors(object):
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
        'answers': 'dict(str, str)',
        'attendance': 'EditOrderAttendance'
    }

    attribute_map = {
        'id': 'id',
        'answers': 'answers',
        'attendance': 'attendance'
    }

    def __init__(self, id=None, answers=None, attendance=None):  # noqa: E501
        """EditOrderVisitors - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._answers = None
        self._attendance = None
        self.discriminator = None
        self.id = id
        if answers is not None:
            self.answers = answers
        if attendance is not None:
            self.attendance = attendance

    @property
    def id(self):
        """Gets the id of this EditOrderVisitors.  # noqa: E501

        Номер регистрации  # noqa: E501

        :return: The id of this EditOrderVisitors.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EditOrderVisitors.

        Номер регистрации  # noqa: E501

        :param id: The id of this EditOrderVisitors.  # noqa: E501
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def answers(self):
        """Gets the answers of this EditOrderVisitors.  # noqa: E501

        Ответы на анкету регистрации  # noqa: E501

        :return: The answers of this EditOrderVisitors.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._answers

    @answers.setter
    def answers(self, answers):
        """Sets the answers of this EditOrderVisitors.

        Ответы на анкету регистрации  # noqa: E501

        :param answers: The answers of this EditOrderVisitors.  # noqa: E501
        :type: dict(str, str)
        """

        self._answers = answers

    @property
    def attendance(self):
        """Gets the attendance of this EditOrderVisitors.  # noqa: E501


        :return: The attendance of this EditOrderVisitors.  # noqa: E501
        :rtype: EditOrderAttendance
        """
        return self._attendance

    @attendance.setter
    def attendance(self, attendance):
        """Sets the attendance of this EditOrderVisitors.


        :param attendance: The attendance of this EditOrderVisitors.  # noqa: E501
        :type: EditOrderAttendance
        """

        self._attendance = attendance

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
        if issubclass(EditOrderVisitors, dict):
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
        if not isinstance(other, EditOrderVisitors):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other