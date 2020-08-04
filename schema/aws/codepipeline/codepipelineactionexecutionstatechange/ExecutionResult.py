# coding: utf-8
import pprint
import re  # noqa: F401

import six
from enum import Enum

class ExecutionResult(object):


    _types = {
        'external_execution_id': 'str',
        'external_execution_url': 'str',
        'external_execution_summary': 'str'
    }

    _attribute_map = {
        'external_execution_id': 'external-execution-id',
        'external_execution_url': 'external-execution-url',
        'external_execution_summary': 'external-execution-summary'
    }

    def __init__(self, external_execution_id=None, external_execution_url=None, external_execution_summary=None):  # noqa: E501
        self._external_execution_id = None
        self._external_execution_url = None
        self._external_execution_summary = None
        self.discriminator = None
        self.external_execution_id = external_execution_id
        self.external_execution_url = external_execution_url
        self.external_execution_summary = external_execution_summary


    @property
    def external_execution_id(self):

        return self._external_execution_id

    @external_execution_id.setter
    def external_execution_id(self, external_execution_id):


        self._external_execution_id = external_execution_id


    @property
    def external_execution_url(self):

        return self._external_execution_url

    @external_execution_url.setter
    def external_execution_url(self, external_execution_url):


        self._external_execution_url = external_execution_url


    @property
    def external_execution_summary(self):

        return self._external_execution_summary

    @external_execution_summary.setter
    def external_execution_summary(self, external_execution_summary):


        self._external_execution_summary = external_execution_summary

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
        if issubclass(ExecutionResult, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, ExecutionResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

