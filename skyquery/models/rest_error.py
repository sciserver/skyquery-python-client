# coding: utf-8

"""
    SkyQuery REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class RestError(object):
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
        'type': 'str',
        'message': 'str',
        'stack_trace': 'str',
        'log_event_id': 'str'
    }

    attribute_map = {
        'type': 'Type',
        'message': 'Message',
        'stack_trace': 'StackTrace',
        'log_event_id': 'LogEventID'
    }

    def __init__(self, type=None, message=None, stack_trace=None, log_event_id=None):  # noqa: E501
        """RestError - a model defined in Swagger"""  # noqa: E501

        self._type = None
        self._message = None
        self._stack_trace = None
        self._log_event_id = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if message is not None:
            self.message = message
        if stack_trace is not None:
            self.stack_trace = stack_trace
        if log_event_id is not None:
            self.log_event_id = log_event_id

    @property
    def type(self):
        """Gets the type of this RestError.  # noqa: E501


        :return: The type of this RestError.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this RestError.


        :param type: The type of this RestError.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def message(self):
        """Gets the message of this RestError.  # noqa: E501


        :return: The message of this RestError.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this RestError.


        :param message: The message of this RestError.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def stack_trace(self):
        """Gets the stack_trace of this RestError.  # noqa: E501


        :return: The stack_trace of this RestError.  # noqa: E501
        :rtype: str
        """
        return self._stack_trace

    @stack_trace.setter
    def stack_trace(self, stack_trace):
        """Sets the stack_trace of this RestError.


        :param stack_trace: The stack_trace of this RestError.  # noqa: E501
        :type: str
        """

        self._stack_trace = stack_trace

    @property
    def log_event_id(self):
        """Gets the log_event_id of this RestError.  # noqa: E501


        :return: The log_event_id of this RestError.  # noqa: E501
        :rtype: str
        """
        return self._log_event_id

    @log_event_id.setter
    def log_event_id(self, log_event_id):
        """Sets the log_event_id of this RestError.


        :param log_event_id: The log_event_id of this RestError.  # noqa: E501
        :type: str
        """

        self._log_event_id = log_event_id

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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, RestError):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
