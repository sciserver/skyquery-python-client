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


class SourceTable(object):
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
        'dataset': 'str',
        'table': 'str'
    }

    attribute_map = {
        'dataset': 'dataset',
        'table': 'table'
    }

    def __init__(self, dataset=None, table=None):  # noqa: E501
        """SourceTable - a model defined in Swagger"""  # noqa: E501

        self._dataset = None
        self._table = None
        self.discriminator = None

        if dataset is not None:
            self.dataset = dataset
        if table is not None:
            self.table = table

    @property
    def dataset(self):
        """Gets the dataset of this SourceTable.  # noqa: E501


        :return: The dataset of this SourceTable.  # noqa: E501
        :rtype: str
        """
        return self._dataset

    @dataset.setter
    def dataset(self, dataset):
        """Sets the dataset of this SourceTable.


        :param dataset: The dataset of this SourceTable.  # noqa: E501
        :type: str
        """

        self._dataset = dataset

    @property
    def table(self):
        """Gets the table of this SourceTable.  # noqa: E501


        :return: The table of this SourceTable.  # noqa: E501
        :rtype: str
        """
        return self._table

    @table.setter
    def table(self, table):
        """Sets the table of this SourceTable.


        :param table: The table of this SourceTable.  # noqa: E501
        :type: str
        """

        self._table = table

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
        if not isinstance(other, SourceTable):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
