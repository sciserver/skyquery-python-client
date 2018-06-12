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

from skyquery.models.user_membership import UserMembership  # noqa: F401,E501


class UserMembershipResponse(object):
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
        'role': 'UserMembership'
    }

    attribute_map = {
        'role': 'role'
    }

    def __init__(self, role=None):  # noqa: E501
        """UserMembershipResponse - a model defined in Swagger"""  # noqa: E501

        self._role = None
        self.discriminator = None

        if role is not None:
            self.role = role

    @property
    def role(self):
        """Gets the role of this UserMembershipResponse.  # noqa: E501


        :return: The role of this UserMembershipResponse.  # noqa: E501
        :rtype: UserMembership
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this UserMembershipResponse.


        :param role: The role of this UserMembershipResponse.  # noqa: E501
        :type: UserMembership
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
        if not isinstance(other, UserMembershipResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
