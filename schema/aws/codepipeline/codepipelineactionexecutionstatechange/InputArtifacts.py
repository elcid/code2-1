# coding: utf-8
import pprint
import re  # noqa: F401

import six
from enum import Enum
from schema.aws.codepipeline.codepipelineactionexecutionstatechange.S3Location import S3Location  # noqa: F401,E501

class InputArtifacts(object):


    _types = {
        'name': 'str',
        's3location': 'S3Location'
    }

    _attribute_map = {
        'name': 'name',
        's3location': 's3location'
    }

    def __init__(self, name=None, s3location=None):  # noqa: E501
        self._name = None
        self._s3location = None
        self.discriminator = None
        self.name = name
        self.s3location = s3location


    @property
    def name(self):

        return self._name

    @name.setter
    def name(self, name):


        self._name = name


    @property
    def s3location(self):

        return self._s3location

    @s3location.setter
    def s3location(self, s3location):


        self._s3location = s3location

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
        if issubclass(InputArtifacts, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, InputArtifacts):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

