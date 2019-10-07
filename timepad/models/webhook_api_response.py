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


class WebhookApiResponse(object):
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
        'organization': 'int',
        'url': 'str',
        'status': 'str',
        'type': 'str',
        'secret': 'str'
    }

    attribute_map = {
        'id': 'id',
        'organization': 'organization',
        'url': 'url',
        'status': 'status',
        'type': 'type',
        'secret': 'secret'
    }

    def __init__(self, id=None, organization=None, url=None, status=None, type=None, secret=None):  # noqa: E501
        """WebhookApiResponse - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._organization = None
        self._url = None
        self._status = None
        self._type = None
        self._secret = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if organization is not None:
            self.organization = organization
        if url is not None:
            self.url = url
        if status is not None:
            self.status = status
        if type is not None:
            self.type = type
        if secret is not None:
            self.secret = secret

    @property
    def id(self):
        """Gets the id of this WebhookApiResponse.  # noqa: E501

        Идентификатор webhook'а  # noqa: E501

        :return: The id of this WebhookApiResponse.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this WebhookApiResponse.

        Идентификатор webhook'а  # noqa: E501

        :param id: The id of this WebhookApiResponse.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def organization(self):
        """Gets the organization of this WebhookApiResponse.  # noqa: E501

        Идентификатор организации  # noqa: E501

        :return: The organization of this WebhookApiResponse.  # noqa: E501
        :rtype: int
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """Sets the organization of this WebhookApiResponse.

        Идентификатор организации  # noqa: E501

        :param organization: The organization of this WebhookApiResponse.  # noqa: E501
        :type: int
        """

        self._organization = organization

    @property
    def url(self):
        """Gets the url of this WebhookApiResponse.  # noqa: E501

        URL-адресс для колбека при событии  # noqa: E501

        :return: The url of this WebhookApiResponse.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this WebhookApiResponse.

        URL-адресс для колбека при событии  # noqa: E501

        :param url: The url of this WebhookApiResponse.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def status(self):
        """Gets the status of this WebhookApiResponse.  # noqa: E501

        Статус webhook'а  # noqa: E501

        :return: The status of this WebhookApiResponse.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this WebhookApiResponse.

        Статус webhook'а  # noqa: E501

        :param status: The status of this WebhookApiResponse.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def type(self):
        """Gets the type of this WebhookApiResponse.  # noqa: E501

        Тип webhook'а  # noqa: E501

        :return: The type of this WebhookApiResponse.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this WebhookApiResponse.

        Тип webhook'а  # noqa: E501

        :param type: The type of this WebhookApiResponse.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def secret(self):
        """Gets the secret of this WebhookApiResponse.  # noqa: E501

        Ключ подписи webhook'а  # noqa: E501

        :return: The secret of this WebhookApiResponse.  # noqa: E501
        :rtype: str
        """
        return self._secret

    @secret.setter
    def secret(self, secret):
        """Sets the secret of this WebhookApiResponse.

        Ключ подписи webhook'а  # noqa: E501

        :param secret: The secret of this WebhookApiResponse.  # noqa: E501
        :type: str
        """

        self._secret = secret

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
        if issubclass(WebhookApiResponse, dict):
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
        if not isinstance(other, WebhookApiResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other