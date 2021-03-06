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


class TicketTypeResponse(object):
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
        'name': 'str',
        'description': 'str',
        'buy_amount_min': 'float',
        'buy_amount_max': 'float',
        'price': 'float',
        'is_promocode_locked': 'bool',
        'remaining': 'int',
        'sale_ends_at': 'date',
        'sale_starts_at': 'date',
        'public_key': 'str',
        'is_active': 'bool',
        'ad_partner_profit': 'float',
        'send_personal_links': 'bool',
        'sold': 'float',
        'attended': 'float',
        'limit': 'float',
        'status': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'buy_amount_min': 'buy_amount_min',
        'buy_amount_max': 'buy_amount_max',
        'price': 'price',
        'is_promocode_locked': 'is_promocode_locked',
        'remaining': 'remaining',
        'sale_ends_at': 'sale_ends_at',
        'sale_starts_at': 'sale_starts_at',
        'public_key': 'public_key',
        'is_active': 'is_active',
        'ad_partner_profit': 'ad_partner_profit',
        'send_personal_links': 'send_personal_links',
        'sold': 'sold',
        'attended': 'attended',
        'limit': 'limit',
        'status': 'status'
    }

    def __init__(self, id=None, name=None, description=None, buy_amount_min=None, buy_amount_max=None, price=None, is_promocode_locked=None, remaining=None, sale_ends_at=None, sale_starts_at=None, public_key=None, is_active=None, ad_partner_profit=None, send_personal_links=None, sold=None, attended=None, limit=None, status=None):  # noqa: E501
        """TicketTypeResponse - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._description = None
        self._buy_amount_min = None
        self._buy_amount_max = None
        self._price = None
        self._is_promocode_locked = None
        self._remaining = None
        self._sale_ends_at = None
        self._sale_starts_at = None
        self._public_key = None
        self._is_active = None
        self._ad_partner_profit = None
        self._send_personal_links = None
        self._sold = None
        self._attended = None
        self._limit = None
        self._status = None
        self.discriminator = None
        self.id = id
        self.name = name
        if description is not None:
            self.description = description
        self.buy_amount_min = buy_amount_min
        self.buy_amount_max = buy_amount_max
        self.price = price
        self.is_promocode_locked = is_promocode_locked
        self.remaining = remaining
        self.sale_ends_at = sale_ends_at
        if sale_starts_at is not None:
            self.sale_starts_at = sale_starts_at
        self.public_key = public_key
        self.is_active = is_active
        if ad_partner_profit is not None:
            self.ad_partner_profit = ad_partner_profit
        if send_personal_links is not None:
            self.send_personal_links = send_personal_links
        if sold is not None:
            self.sold = sold
        if attended is not None:
            self.attended = attended
        if limit is not None:
            self.limit = limit
        if status is not None:
            self.status = status

    @property
    def id(self):
        """Gets the id of this TicketTypeResponse.  # noqa: E501

        Уникальный номер типа билета  # noqa: E501

        :return: The id of this TicketTypeResponse.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TicketTypeResponse.

        Уникальный номер типа билета  # noqa: E501

        :param id: The id of this TicketTypeResponse.  # noqa: E501
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this TicketTypeResponse.  # noqa: E501

        Название типа билета  # noqa: E501

        :return: The name of this TicketTypeResponse.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TicketTypeResponse.

        Название типа билета  # noqa: E501

        :param name: The name of this TicketTypeResponse.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this TicketTypeResponse.  # noqa: E501

        Описание типа билета  # noqa: E501

        :return: The description of this TicketTypeResponse.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this TicketTypeResponse.

        Описание типа билета  # noqa: E501

        :param description: The description of this TicketTypeResponse.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def buy_amount_min(self):
        """Gets the buy_amount_min of this TicketTypeResponse.  # noqa: E501

        Минимальное количество билетов в одной покупке  # noqa: E501

        :return: The buy_amount_min of this TicketTypeResponse.  # noqa: E501
        :rtype: float
        """
        return self._buy_amount_min

    @buy_amount_min.setter
    def buy_amount_min(self, buy_amount_min):
        """Sets the buy_amount_min of this TicketTypeResponse.

        Минимальное количество билетов в одной покупке  # noqa: E501

        :param buy_amount_min: The buy_amount_min of this TicketTypeResponse.  # noqa: E501
        :type: float
        """
        if buy_amount_min is None:
            raise ValueError("Invalid value for `buy_amount_min`, must not be `None`")  # noqa: E501

        self._buy_amount_min = buy_amount_min

    @property
    def buy_amount_max(self):
        """Gets the buy_amount_max of this TicketTypeResponse.  # noqa: E501

        Максимальное количество билетов в одной покупке  # noqa: E501

        :return: The buy_amount_max of this TicketTypeResponse.  # noqa: E501
        :rtype: float
        """
        return self._buy_amount_max

    @buy_amount_max.setter
    def buy_amount_max(self, buy_amount_max):
        """Sets the buy_amount_max of this TicketTypeResponse.

        Максимальное количество билетов в одной покупке  # noqa: E501

        :param buy_amount_max: The buy_amount_max of this TicketTypeResponse.  # noqa: E501
        :type: float
        """
        if buy_amount_max is None:
            raise ValueError("Invalid value for `buy_amount_max`, must not be `None`")  # noqa: E501

        self._buy_amount_max = buy_amount_max

    @property
    def price(self):
        """Gets the price of this TicketTypeResponse.  # noqa: E501

        Цена билета  # noqa: E501

        :return: The price of this TicketTypeResponse.  # noqa: E501
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this TicketTypeResponse.

        Цена билета  # noqa: E501

        :param price: The price of this TicketTypeResponse.  # noqa: E501
        :type: float
        """
        if price is None:
            raise ValueError("Invalid value for `price`, must not be `None`")  # noqa: E501

        self._price = price

    @property
    def is_promocode_locked(self):
        """Gets the is_promocode_locked of this TicketTypeResponse.  # noqa: E501

        Закрыт ли этот тип билета введённым промокодом  # noqa: E501

        :return: The is_promocode_locked of this TicketTypeResponse.  # noqa: E501
        :rtype: bool
        """
        return self._is_promocode_locked

    @is_promocode_locked.setter
    def is_promocode_locked(self, is_promocode_locked):
        """Sets the is_promocode_locked of this TicketTypeResponse.

        Закрыт ли этот тип билета введённым промокодом  # noqa: E501

        :param is_promocode_locked: The is_promocode_locked of this TicketTypeResponse.  # noqa: E501
        :type: bool
        """
        if is_promocode_locked is None:
            raise ValueError("Invalid value for `is_promocode_locked`, must not be `None`")  # noqa: E501

        self._is_promocode_locked = is_promocode_locked

    @property
    def remaining(self):
        """Gets the remaining of this TicketTypeResponse.  # noqa: E501

        Сколько билетов осталось  # noqa: E501

        :return: The remaining of this TicketTypeResponse.  # noqa: E501
        :rtype: int
        """
        return self._remaining

    @remaining.setter
    def remaining(self, remaining):
        """Sets the remaining of this TicketTypeResponse.

        Сколько билетов осталось  # noqa: E501

        :param remaining: The remaining of this TicketTypeResponse.  # noqa: E501
        :type: int
        """
        if remaining is None:
            raise ValueError("Invalid value for `remaining`, must not be `None`")  # noqa: E501

        self._remaining = remaining

    @property
    def sale_ends_at(self):
        """Gets the sale_ends_at of this TicketTypeResponse.  # noqa: E501

        Дата окончания продажи типа билета  # noqa: E501

        :return: The sale_ends_at of this TicketTypeResponse.  # noqa: E501
        :rtype: date
        """
        return self._sale_ends_at

    @sale_ends_at.setter
    def sale_ends_at(self, sale_ends_at):
        """Sets the sale_ends_at of this TicketTypeResponse.

        Дата окончания продажи типа билета  # noqa: E501

        :param sale_ends_at: The sale_ends_at of this TicketTypeResponse.  # noqa: E501
        :type: date
        """
        if sale_ends_at is None:
            raise ValueError("Invalid value for `sale_ends_at`, must not be `None`")  # noqa: E501

        self._sale_ends_at = sale_ends_at

    @property
    def sale_starts_at(self):
        """Gets the sale_starts_at of this TicketTypeResponse.  # noqa: E501

        Дата начала продажи типа билета  # noqa: E501

        :return: The sale_starts_at of this TicketTypeResponse.  # noqa: E501
        :rtype: date
        """
        return self._sale_starts_at

    @sale_starts_at.setter
    def sale_starts_at(self, sale_starts_at):
        """Sets the sale_starts_at of this TicketTypeResponse.

        Дата начала продажи типа билета  # noqa: E501

        :param sale_starts_at: The sale_starts_at of this TicketTypeResponse.  # noqa: E501
        :type: date
        """

        self._sale_starts_at = sale_starts_at

    @property
    def public_key(self):
        """Gets the public_key of this TicketTypeResponse.  # noqa: E501

        Публичный ключ для расшифровки QR-кода билета этого типа  # noqa: E501

        :return: The public_key of this TicketTypeResponse.  # noqa: E501
        :rtype: str
        """
        return self._public_key

    @public_key.setter
    def public_key(self, public_key):
        """Sets the public_key of this TicketTypeResponse.

        Публичный ключ для расшифровки QR-кода билета этого типа  # noqa: E501

        :param public_key: The public_key of this TicketTypeResponse.  # noqa: E501
        :type: str
        """
        if public_key is None:
            raise ValueError("Invalid value for `public_key`, must not be `None`")  # noqa: E501

        self._public_key = public_key

    @property
    def is_active(self):
        """Gets the is_active of this TicketTypeResponse.  # noqa: E501

        Активность типа билета  # noqa: E501

        :return: The is_active of this TicketTypeResponse.  # noqa: E501
        :rtype: bool
        """
        return self._is_active

    @is_active.setter
    def is_active(self, is_active):
        """Sets the is_active of this TicketTypeResponse.

        Активность типа билета  # noqa: E501

        :param is_active: The is_active of this TicketTypeResponse.  # noqa: E501
        :type: bool
        """
        if is_active is None:
            raise ValueError("Invalid value for `is_active`, must not be `None`")  # noqa: E501

        self._is_active = is_active

    @property
    def ad_partner_profit(self):
        """Gets the ad_partner_profit of this TicketTypeResponse.  # noqa: E501

        Партнёрская прибыль  # noqa: E501

        :return: The ad_partner_profit of this TicketTypeResponse.  # noqa: E501
        :rtype: float
        """
        return self._ad_partner_profit

    @ad_partner_profit.setter
    def ad_partner_profit(self, ad_partner_profit):
        """Sets the ad_partner_profit of this TicketTypeResponse.

        Партнёрская прибыль  # noqa: E501

        :param ad_partner_profit: The ad_partner_profit of this TicketTypeResponse.  # noqa: E501
        :type: float
        """

        self._ad_partner_profit = ad_partner_profit

    @property
    def send_personal_links(self):
        """Gets the send_personal_links of this TicketTypeResponse.  # noqa: E501

        Отправка персональных сссылок  # noqa: E501

        :return: The send_personal_links of this TicketTypeResponse.  # noqa: E501
        :rtype: bool
        """
        return self._send_personal_links

    @send_personal_links.setter
    def send_personal_links(self, send_personal_links):
        """Sets the send_personal_links of this TicketTypeResponse.

        Отправка персональных сссылок  # noqa: E501

        :param send_personal_links: The send_personal_links of this TicketTypeResponse.  # noqa: E501
        :type: bool
        """

        self._send_personal_links = send_personal_links

    @property
    def sold(self):
        """Gets the sold of this TicketTypeResponse.  # noqa: E501

        Количество проданных билетов  # noqa: E501

        :return: The sold of this TicketTypeResponse.  # noqa: E501
        :rtype: float
        """
        return self._sold

    @sold.setter
    def sold(self, sold):
        """Sets the sold of this TicketTypeResponse.

        Количество проданных билетов  # noqa: E501

        :param sold: The sold of this TicketTypeResponse.  # noqa: E501
        :type: float
        """

        self._sold = sold

    @property
    def attended(self):
        """Gets the attended of this TicketTypeResponse.  # noqa: E501

        Количество посетивших людей  # noqa: E501

        :return: The attended of this TicketTypeResponse.  # noqa: E501
        :rtype: float
        """
        return self._attended

    @attended.setter
    def attended(self, attended):
        """Sets the attended of this TicketTypeResponse.

        Количество посетивших людей  # noqa: E501

        :param attended: The attended of this TicketTypeResponse.  # noqa: E501
        :type: float
        """

        self._attended = attended

    @property
    def limit(self):
        """Gets the limit of this TicketTypeResponse.  # noqa: E501

        Ограничение на количество билетов в этом типе билета  # noqa: E501

        :return: The limit of this TicketTypeResponse.  # noqa: E501
        :rtype: float
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this TicketTypeResponse.

        Ограничение на количество билетов в этом типе билета  # noqa: E501

        :param limit: The limit of this TicketTypeResponse.  # noqa: E501
        :type: float
        """

        self._limit = limit

    @property
    def status(self):
        """Gets the status of this TicketTypeResponse.  # noqa: E501

        Статус типа билета  # noqa: E501

        :return: The status of this TicketTypeResponse.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this TicketTypeResponse.

        Статус типа билета  # noqa: E501

        :param status: The status of this TicketTypeResponse.  # noqa: E501
        :type: str
        """

        self._status = status

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
        if issubclass(TicketTypeResponse, dict):
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
        if not isinstance(other, TicketTypeResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
