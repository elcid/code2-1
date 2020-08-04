# coding: utf-8
import pprint
import re  # noqa: F401

import six
from enum import Enum

class Type(object):


    _types = {
        'owner': 'str',
        'provider': 'str',
        'category': 'str',
        'version': 'float'
    }

    _attribute_map = {
        'owner': 'owner',
        'provider': 'provider',
        'category': 'category',
        'version': 'version'
    }

    def __init__(self, owner=None, provider=None, category=None, version=None):  # noqa: E501
        self._owner = None
        self._provider = None
        self._category = None
        self._version = None
        self.discriminator = None
        self.owner = owner
        self.provider = provider
        self.category = category
        self.version = version


    @property
    def owner(self):

        return self._owner

    @owner.setter
    def owner(self, owner):


        self._owner = owner


    @property
    def provider(self):

        return self._provider

    @provider.setter
    def provider(self, provider):


        self._provider = provider


    @property
    def category(self):

        return self._category

    @category.setter
    def category(self, category):


        self._category = category


    @property
    def version(self):

        return self._version

    @version.setter
    def version(self, version):


        self._version = version

    def to_dict(self):
        result = {}

        for attr, _ in six.iteritems(self._types):
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
        if issubclass(Type, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, Type):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

