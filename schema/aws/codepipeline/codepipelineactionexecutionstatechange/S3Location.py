# coding: utf-8
import pprint
import re  # noqa: F401

import six
from enum import Enum

class S3Location(object):


    _types = {
        'bucket': 'str',
        'key': 'str'
    }

    _attribute_map = {
        'bucket': 'bucket',
        'key': 'key'
    }

    def __init__(self, bucket=None, key=None):  # noqa: E501
        self._bucket = None
        self._key = None
        self.discriminator = None
        self.bucket = bucket
        self.key = key


    @property
    def bucket(self):

        return self._bucket

    @bucket.setter
    def bucket(self, bucket):


        self._bucket = bucket


    @property
    def key(self):

        return self._key

    @key.setter
    def key(self, key):


        self._key = key

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
        if issubclass(S3Location, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, S3Location):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

