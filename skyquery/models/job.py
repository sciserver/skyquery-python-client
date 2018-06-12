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

from skyquery.models.job_dependency import JobDependency  # noqa: F401,E501


class Job(object):
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
        'guid': 'str',
        'name': 'str',
        'status': 'str',
        'can_cancel': 'bool',
        'has_error': 'bool',
        'queue': 'str',
        'comments': 'str',
        'error': 'str',
        'date_created': 'str',
        'date_started': 'str',
        'date_finished': 'str',
        'dependencies': 'list[JobDependency]'
    }

    attribute_map = {
        'guid': 'guid',
        'name': 'name',
        'status': 'status',
        'can_cancel': 'canCancel',
        'has_error': 'hasError',
        'queue': 'queue',
        'comments': 'comments',
        'error': 'error',
        'date_created': 'dateCreated',
        'date_started': 'dateStarted',
        'date_finished': 'dateFinished',
        'dependencies': 'dependencies'
    }

    def __init__(self, guid=None, name=None, status=None, can_cancel=None, has_error=None, queue=None, comments=None, error=None, date_created=None, date_started=None, date_finished=None, dependencies=None):  # noqa: E501
        """Job - a model defined in Swagger"""  # noqa: E501

        self._guid = None
        self._name = None
        self._status = None
        self._can_cancel = None
        self._has_error = None
        self._queue = None
        self._comments = None
        self._error = None
        self._date_created = None
        self._date_started = None
        self._date_finished = None
        self._dependencies = None
        self.discriminator = None

        if guid is not None:
            self.guid = guid
        if name is not None:
            self.name = name
        if status is not None:
            self.status = status
        if can_cancel is not None:
            self.can_cancel = can_cancel
        if has_error is not None:
            self.has_error = has_error
        if queue is not None:
            self.queue = queue
        if comments is not None:
            self.comments = comments
        if error is not None:
            self.error = error
        if date_created is not None:
            self.date_created = date_created
        if date_started is not None:
            self.date_started = date_started
        if date_finished is not None:
            self.date_finished = date_finished
        if dependencies is not None:
            self.dependencies = dependencies

    @property
    def guid(self):
        """Gets the guid of this Job.  # noqa: E501


        :return: The guid of this Job.  # noqa: E501
        :rtype: str
        """
        return self._guid

    @guid.setter
    def guid(self, guid):
        """Sets the guid of this Job.


        :param guid: The guid of this Job.  # noqa: E501
        :type: str
        """

        self._guid = guid

    @property
    def name(self):
        """Gets the name of this Job.  # noqa: E501


        :return: The name of this Job.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Job.


        :param name: The name of this Job.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def status(self):
        """Gets the status of this Job.  # noqa: E501


        :return: The status of this Job.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Job.


        :param status: The status of this Job.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def can_cancel(self):
        """Gets the can_cancel of this Job.  # noqa: E501


        :return: The can_cancel of this Job.  # noqa: E501
        :rtype: bool
        """
        return self._can_cancel

    @can_cancel.setter
    def can_cancel(self, can_cancel):
        """Sets the can_cancel of this Job.


        :param can_cancel: The can_cancel of this Job.  # noqa: E501
        :type: bool
        """

        self._can_cancel = can_cancel

    @property
    def has_error(self):
        """Gets the has_error of this Job.  # noqa: E501


        :return: The has_error of this Job.  # noqa: E501
        :rtype: bool
        """
        return self._has_error

    @has_error.setter
    def has_error(self, has_error):
        """Sets the has_error of this Job.


        :param has_error: The has_error of this Job.  # noqa: E501
        :type: bool
        """

        self._has_error = has_error

    @property
    def queue(self):
        """Gets the queue of this Job.  # noqa: E501


        :return: The queue of this Job.  # noqa: E501
        :rtype: str
        """
        return self._queue

    @queue.setter
    def queue(self, queue):
        """Sets the queue of this Job.


        :param queue: The queue of this Job.  # noqa: E501
        :type: str
        """

        self._queue = queue

    @property
    def comments(self):
        """Gets the comments of this Job.  # noqa: E501


        :return: The comments of this Job.  # noqa: E501
        :rtype: str
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """Sets the comments of this Job.


        :param comments: The comments of this Job.  # noqa: E501
        :type: str
        """

        self._comments = comments

    @property
    def error(self):
        """Gets the error of this Job.  # noqa: E501


        :return: The error of this Job.  # noqa: E501
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this Job.


        :param error: The error of this Job.  # noqa: E501
        :type: str
        """

        self._error = error

    @property
    def date_created(self):
        """Gets the date_created of this Job.  # noqa: E501


        :return: The date_created of this Job.  # noqa: E501
        :rtype: str
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """Sets the date_created of this Job.


        :param date_created: The date_created of this Job.  # noqa: E501
        :type: str
        """

        self._date_created = date_created

    @property
    def date_started(self):
        """Gets the date_started of this Job.  # noqa: E501


        :return: The date_started of this Job.  # noqa: E501
        :rtype: str
        """
        return self._date_started

    @date_started.setter
    def date_started(self, date_started):
        """Sets the date_started of this Job.


        :param date_started: The date_started of this Job.  # noqa: E501
        :type: str
        """

        self._date_started = date_started

    @property
    def date_finished(self):
        """Gets the date_finished of this Job.  # noqa: E501


        :return: The date_finished of this Job.  # noqa: E501
        :rtype: str
        """
        return self._date_finished

    @date_finished.setter
    def date_finished(self, date_finished):
        """Sets the date_finished of this Job.


        :param date_finished: The date_finished of this Job.  # noqa: E501
        :type: str
        """

        self._date_finished = date_finished

    @property
    def dependencies(self):
        """Gets the dependencies of this Job.  # noqa: E501


        :return: The dependencies of this Job.  # noqa: E501
        :rtype: list[JobDependency]
        """
        return self._dependencies

    @dependencies.setter
    def dependencies(self, dependencies):
        """Sets the dependencies of this Job.


        :param dependencies: The dependencies of this Job.  # noqa: E501
        :type: list[JobDependency]
        """

        self._dependencies = dependencies

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
        if not isinstance(other, Job):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
