# coding: utf-8

"""
    Public API Server

    **osparc-simcore Public RESTful API Specifications** ## Python Client - Github [repo](https://github.com/ITISFoundation/osparc-simcore-python-client) - Quick install: ``pip install git+https://github.com/ITISFoundation/osparc-simcore-python-client.git``   # noqa: E501

    The version of the OpenAPI document: 0.3.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from osparc.configuration import Configuration


class Groups(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'me': 'UsersGroup',
        'organizations': 'list[UsersGroup]',
        'all': 'UsersGroup'
    }

    attribute_map = {
        'me': 'me',
        'organizations': 'organizations',
        'all': 'all'
    }

    def __init__(self, me=None, organizations=[], all=None, local_vars_configuration=None):  # noqa: E501
        """Groups - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._me = None
        self._organizations = None
        self._all = None
        self.discriminator = None

        self.me = me
        if organizations is not None:
            self.organizations = organizations
        self.all = all

    @property
    def me(self):
        """Gets the me of this Groups.  # noqa: E501


        :return: The me of this Groups.  # noqa: E501
        :rtype: UsersGroup
        """
        return self._me

    @me.setter
    def me(self, me):
        """Sets the me of this Groups.


        :param me: The me of this Groups.  # noqa: E501
        :type: UsersGroup
        """
        if self.local_vars_configuration.client_side_validation and me is None:  # noqa: E501
            raise ValueError("Invalid value for `me`, must not be `None`")  # noqa: E501

        self._me = me

    @property
    def organizations(self):
        """Gets the organizations of this Groups.  # noqa: E501


        :return: The organizations of this Groups.  # noqa: E501
        :rtype: list[UsersGroup]
        """
        return self._organizations

    @organizations.setter
    def organizations(self, organizations):
        """Sets the organizations of this Groups.


        :param organizations: The organizations of this Groups.  # noqa: E501
        :type: list[UsersGroup]
        """

        self._organizations = organizations

    @property
    def all(self):
        """Gets the all of this Groups.  # noqa: E501


        :return: The all of this Groups.  # noqa: E501
        :rtype: UsersGroup
        """
        return self._all

    @all.setter
    def all(self, all):
        """Sets the all of this Groups.


        :param all: The all of this Groups.  # noqa: E501
        :type: UsersGroup
        """
        if self.local_vars_configuration.client_side_validation and all is None:  # noqa: E501
            raise ValueError("Invalid value for `all`, must not be `None`")  # noqa: E501

        self._all = all

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if not isinstance(other, Groups):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Groups):
            return True

        return self.to_dict() != other.to_dict()
