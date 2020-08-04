# coding: utf-8
import pprint
import re  # noqa: F401

import six
from enum import Enum
from schema.aws.codepipeline.codepipelineactionexecutionstatechange.ExecutionResult import ExecutionResult  # noqa: F401,E501
from schema.aws.codepipeline.codepipelineactionexecutionstatechange.InputArtifacts import InputArtifacts  # noqa: F401,E501
from schema.aws.codepipeline.codepipelineactionexecutionstatechange.OutputArtifacts import OutputArtifacts  # noqa: F401,E501
from schema.aws.codepipeline.codepipelineactionexecutionstatechange.Type import Type  # noqa: F401,E501

class CodePipelineActionExecutionStateChange(object):


    _types = {
        'type': 'Type',
        'pipeline': 'str',
        'execution_id': 'str',
        'stage': 'str',
        'action': 'str',
        'state': 'str',
        'region': 'str',
        'version': 'float',
        'execution_result': 'ExecutionResult',
        'input_artifacts': 'InputArtifacts',
        'output_artifacts': 'OutputArtifacts'
    }

    _attribute_map = {
        'type': 'type',
        'pipeline': 'pipeline',
        'execution_id': 'execution-id',
        'stage': 'stage',
        'action': 'action',
        'state': 'state',
        'region': 'region',
        'version': 'version',
        'execution_result': 'execution-result',
        'input_artifacts': 'input-artifacts',
        'output_artifacts': 'output-artifacts'
    }

    def __init__(self, type=None, pipeline=None, execution_id=None, stage=None, action=None, state=None, region=None, version=None, execution_result=None, input_artifacts=None, output_artifacts=None):  # noqa: E501
        self._type = None
        self._pipeline = None
        self._execution_id = None
        self._stage = None
        self._action = None
        self._state = None
        self._region = None
        self._version = None
        self._execution_result = None
        self._input_artifacts = None
        self._output_artifacts = None
        self.discriminator = None
        self.type = type
        self.pipeline = pipeline
        self.execution_id = execution_id
        self.stage = stage
        self.action = action
        self.state = state
        self.region = region
        self.version = version
        self.execution_result = execution_result
        self.input_artifacts = input_artifacts
        self.output_artifacts = output_artifacts


    @property
    def type(self):

        return self._type

    @type.setter
    def type(self, type):


        self._type = type


    @property
    def pipeline(self):

        return self._pipeline

    @pipeline.setter
    def pipeline(self, pipeline):


        self._pipeline = pipeline


    @property
    def execution_id(self):

        return self._execution_id

    @execution_id.setter
    def execution_id(self, execution_id):


        self._execution_id = execution_id


    @property
    def stage(self):

        return self._stage

    @stage.setter
    def stage(self, stage):


        self._stage = stage


    @property
    def action(self):

        return self._action

    @action.setter
    def action(self, action):


        self._action = action


    @property
    def state(self):

        return self._state

    @state.setter
    def state(self, state):


        self._state = state


    @property
    def region(self):

        return self._region

    @region.setter
    def region(self, region):


        self._region = region


    @property
    def version(self):

        return self._version

    @version.setter
    def version(self, version):


        self._version = version


    @property
    def execution_result(self):

        return self._execution_result

    @execution_result.setter
    def execution_result(self, execution_result):


        self._execution_result = execution_result


    @property
    def input_artifacts(self):

        return self._input_artifacts

    @input_artifacts.setter
    def input_artifacts(self, input_artifacts):


        self._input_artifacts = input_artifacts


    @property
    def output_artifacts(self):

        return self._output_artifacts

    @output_artifacts.setter
    def output_artifacts(self, output_artifacts):


        self._output_artifacts = output_artifacts

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
        if issubclass(CodePipelineActionExecutionStateChange, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, CodePipelineActionExecutionStateChange):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

