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
from timepad.models.order_event_response import OrderEventResponse  # noqa: F401,E501
from timepad.models.order_referrer_response import OrderReferrerResponse  # noqa: F401,E501
from timepad.models.order_status_response import OrderStatusResponse  # noqa: F401,E501
from timepad.models.payment_response import PaymentResponse  # noqa: F401,E501
from timepad.models.ticket_response import TicketResponse  # noqa: F401,E501


class RegistrationOrderResponse(object):
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
        'created_at': 'date',
        'status': 'OrderStatusResponse',
        'mail': 'str',
        'payment': 'PaymentResponse',
        'tickets': 'list[TicketResponse]',
        'answers': 'dict(str, str)',
        'promocodes': 'list[str]',
        'event': 'OrderEventResponse',
        'referrer': 'OrderReferrerResponse',
        'subscribed_to_newsletter': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'created_at': 'created_at',
        'status': 'status',
        'mail': 'mail',
        'payment': 'payment',
        'tickets': 'tickets',
        'answers': 'answers',
        'promocodes': 'promocodes',
        'event': 'event',
        'referrer': 'referrer',
        'subscribed_to_newsletter': 'subscribed_to_newsletter'
    }

    def __init__(self, id=None, created_at=None, status=None, mail=None, payment=None, tickets=None, answers=None, promocodes=None, event=None, referrer=None, subscribed_to_newsletter=None):  # noqa: E501
        """RegistrationOrderResponse - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._created_at = None
        self._status = None
        self._mail = None
        self._payment = None
        self._tickets = None
        self._answers = None
        self._promocodes = None
        self._event = None
        self._referrer = None
        self._subscribed_to_newsletter = None
        self.discriminator = None
        self.id = id
        self.created_at = created_at
        self.status = status
        if mail is not None:
            self.mail = mail
        if payment is not None:
            self.payment = payment
        self.tickets = tickets
        self.answers = answers
        if promocodes is not None:
            self.promocodes = promocodes
        if event is not None:
            self.event = event
        if referrer is not None:
            self.referrer = referrer
        if subscribed_to_newsletter is not None:
            self.subscribed_to_newsletter = subscribed_to_newsletter

    @property
    def id(self):
        """Gets the id of this RegistrationOrderResponse.  # noqa: E501

        Уникальный номер заказа  # noqa: E501

        :return: The id of this RegistrationOrderResponse.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this RegistrationOrderResponse.

        Уникальный номер заказа  # noqa: E501

        :param id: The id of this RegistrationOrderResponse.  # noqa: E501
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def created_at(self):
        """Gets the created_at of this RegistrationOrderResponse.  # noqa: E501

        Дата создания заказа  # noqa: E501

        :return: The created_at of this RegistrationOrderResponse.  # noqa: E501
        :rtype: date
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this RegistrationOrderResponse.

        Дата создания заказа  # noqa: E501

        :param created_at: The created_at of this RegistrationOrderResponse.  # noqa: E501
        :type: date
        """
        if created_at is None:
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def status(self):
        """Gets the status of this RegistrationOrderResponse.  # noqa: E501


        :return: The status of this RegistrationOrderResponse.  # noqa: E501
        :rtype: OrderStatusResponse
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this RegistrationOrderResponse.


        :param status: The status of this RegistrationOrderResponse.  # noqa: E501
        :type: OrderStatusResponse
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def mail(self):
        """Gets the mail of this RegistrationOrderResponse.  # noqa: E501

        Адрес электронной почты заказчика билетов. Если режим регистрации на ваше событие находится в положении &laquo;Простая регистрация&raquo; или &laquo;Мультирегистрация&raquo;, здесь будет находиться адрес электронной почты из поля &laquo;E-mail&raquo; формы покупки билетов. Если режим регистрации выставлен как &laquo;Мультианкета&raquo;, то здесь будет находится адрес электронной почты первого участника. В некоторых случаях, когда форма регистрации настроена на отображение отдельной формы заказчика, в этом поле будет находится адрес электронной почты из этой формы.  # noqa: E501

        :return: The mail of this RegistrationOrderResponse.  # noqa: E501
        :rtype: str
        """
        return self._mail

    @mail.setter
    def mail(self, mail):
        """Sets the mail of this RegistrationOrderResponse.

        Адрес электронной почты заказчика билетов. Если режим регистрации на ваше событие находится в положении &laquo;Простая регистрация&raquo; или &laquo;Мультирегистрация&raquo;, здесь будет находиться адрес электронной почты из поля &laquo;E-mail&raquo; формы покупки билетов. Если режим регистрации выставлен как &laquo;Мультианкета&raquo;, то здесь будет находится адрес электронной почты первого участника. В некоторых случаях, когда форма регистрации настроена на отображение отдельной формы заказчика, в этом поле будет находится адрес электронной почты из этой формы.  # noqa: E501

        :param mail: The mail of this RegistrationOrderResponse.  # noqa: E501
        :type: str
        """

        self._mail = mail

    @property
    def payment(self):
        """Gets the payment of this RegistrationOrderResponse.  # noqa: E501


        :return: The payment of this RegistrationOrderResponse.  # noqa: E501
        :rtype: PaymentResponse
        """
        return self._payment

    @payment.setter
    def payment(self, payment):
        """Sets the payment of this RegistrationOrderResponse.


        :param payment: The payment of this RegistrationOrderResponse.  # noqa: E501
        :type: PaymentResponse
        """

        self._payment = payment

    @property
    def tickets(self):
        """Gets the tickets of this RegistrationOrderResponse.  # noqa: E501

        Список регистраций  # noqa: E501

        :return: The tickets of this RegistrationOrderResponse.  # noqa: E501
        :rtype: list[TicketResponse]
        """
        return self._tickets

    @tickets.setter
    def tickets(self, tickets):
        """Sets the tickets of this RegistrationOrderResponse.

        Список регистраций  # noqa: E501

        :param tickets: The tickets of this RegistrationOrderResponse.  # noqa: E501
        :type: list[TicketResponse]
        """
        if tickets is None:
            raise ValueError("Invalid value for `tickets`, must not be `None`")  # noqa: E501

        self._tickets = tickets

    @property
    def answers(self):
        """Gets the answers of this RegistrationOrderResponse.  # noqa: E501

        Массив Ответов  # noqa: E501

        :return: The answers of this RegistrationOrderResponse.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._answers

    @answers.setter
    def answers(self, answers):
        """Sets the answers of this RegistrationOrderResponse.

        Массив Ответов  # noqa: E501

        :param answers: The answers of this RegistrationOrderResponse.  # noqa: E501
        :type: dict(str, str)
        """
        if answers is None:
            raise ValueError("Invalid value for `answers`, must not be `None`")  # noqa: E501

        self._answers = answers

    @property
    def promocodes(self):
        """Gets the promocodes of this RegistrationOrderResponse.  # noqa: E501

        Список промокодов  # noqa: E501

        :return: The promocodes of this RegistrationOrderResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._promocodes

    @promocodes.setter
    def promocodes(self, promocodes):
        """Sets the promocodes of this RegistrationOrderResponse.

        Список промокодов  # noqa: E501

        :param promocodes: The promocodes of this RegistrationOrderResponse.  # noqa: E501
        :type: list[str]
        """

        self._promocodes = promocodes

    @property
    def event(self):
        """Gets the event of this RegistrationOrderResponse.  # noqa: E501


        :return: The event of this RegistrationOrderResponse.  # noqa: E501
        :rtype: OrderEventResponse
        """
        return self._event

    @event.setter
    def event(self, event):
        """Sets the event of this RegistrationOrderResponse.


        :param event: The event of this RegistrationOrderResponse.  # noqa: E501
        :type: OrderEventResponse
        """

        self._event = event

    @property
    def referrer(self):
        """Gets the referrer of this RegistrationOrderResponse.  # noqa: E501


        :return: The referrer of this RegistrationOrderResponse.  # noqa: E501
        :rtype: OrderReferrerResponse
        """
        return self._referrer

    @referrer.setter
    def referrer(self, referrer):
        """Sets the referrer of this RegistrationOrderResponse.


        :param referrer: The referrer of this RegistrationOrderResponse.  # noqa: E501
        :type: OrderReferrerResponse
        """

        self._referrer = referrer

    @property
    def subscribed_to_newsletter(self):
        """Gets the subscribed_to_newsletter of this RegistrationOrderResponse.  # noqa: E501

        Подписка на анонсы событий организатора  # noqa: E501

        :return: The subscribed_to_newsletter of this RegistrationOrderResponse.  # noqa: E501
        :rtype: bool
        """
        return self._subscribed_to_newsletter

    @subscribed_to_newsletter.setter
    def subscribed_to_newsletter(self, subscribed_to_newsletter):
        """Sets the subscribed_to_newsletter of this RegistrationOrderResponse.

        Подписка на анонсы событий организатора  # noqa: E501

        :param subscribed_to_newsletter: The subscribed_to_newsletter of this RegistrationOrderResponse.  # noqa: E501
        :type: bool
        """

        self._subscribed_to_newsletter = subscribed_to_newsletter

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
        if issubclass(RegistrationOrderResponse, dict):
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
        if not isinstance(other, RegistrationOrderResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
