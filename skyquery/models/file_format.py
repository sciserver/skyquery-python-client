# coding: utf-8

"""
    null

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: null
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class FileFormat(object):
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
        'mime_type': 'str',
        'generate_identity_column': 'bool'
    }

    attribute_map = {
        'mime_type': 'mimeType',
        'generate_identity_column': 'generateIdentityColumn'
    }

    def __init__(self, mime_type=None, generate_identity_column=None):  # noqa: E501
        """FileFormat - a model defined in Swagger"""  # noqa: E501

        self._mime_type = None
        self._generate_identity_column = None
        self.discriminator = None

        if mime_type is not None:
            self.mime_type = mime_type
        if generate_identity_column is not None:
            self.generate_identity_column = generate_identity_column

    @property
    def mime_type(self):
        """Gets the mime_type of this FileFormat.  # noqa: E501


        :return: The mime_type of this FileFormat.  # noqa: E501
        :rtype: str
        """
        return self._mime_type

    @mime_type.setter
    def mime_type(self, mime_type):
        """Sets the mime_type of this FileFormat.


        :param mime_type: The mime_type of this FileFormat.  # noqa: E501
        :type: str
        """

        self._mime_type = mime_type

    @property
    def generate_identity_column(self):
        """Gets the generate_identity_column of this FileFormat.  # noqa: E501


        :return: The generate_identity_column of this FileFormat.  # noqa: E501
        :rtype: bool
        """
        return self._generate_identity_column

    @generate_identity_column.setter
    def generate_identity_column(self, generate_identity_column):
        """Sets the generate_identity_column of this FileFormat.


        :param generate_identity_column: The generate_identity_column of this FileFormat.  # noqa: E501
        :type: bool
        """

        self._generate_identity_column = generate_identity_column

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
        if not isinstance(other, FileFormat):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other