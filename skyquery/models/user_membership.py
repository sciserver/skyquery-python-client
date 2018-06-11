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


class UserMembership(object):
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
        'user': 'str',
        'group': 'str',
        'role': 'str'
    }

    attribute_map = {
        'user': 'user',
        'group': 'group',
        'role': 'role'
    }

    def __init__(self, user=None, group=None, role=None):  # noqa: E501
        """UserMembership - a model defined in Swagger"""  # noqa: E501

        self._user = None
        self._group = None
        self._role = None
        self.discriminator = None

        if user is not None:
            self.user = user
        if group is not None:
            self.group = group
        if role is not None:
            self.role = role

    @property
    def user(self):
        """Gets the user of this UserMembership.  # noqa: E501


        :return: The user of this UserMembership.  # noqa: E501
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this UserMembership.


        :param user: The user of this UserMembership.  # noqa: E501
        :type: str
        """

        self._user = user

    @property
    def group(self):
        """Gets the group of this UserMembership.  # noqa: E501


        :return: The group of this UserMembership.  # noqa: E501
        :rtype: str
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this UserMembership.


        :param group: The group of this UserMembership.  # noqa: E501
        :type: str
        """

        self._group = group

    @property
    def role(self):
        """Gets the role of this UserMembership.  # noqa: E501


        :return: The role of this UserMembership.  # noqa: E501
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this UserMembership.


        :param role: The role of this UserMembership.  # noqa: E501
        :type: str
        """

        self._role = role

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
        if not isinstance(other, UserMembership):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other