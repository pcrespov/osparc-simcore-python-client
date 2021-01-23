# coding: utf-8

"""
    Public API Server

    **osparc-simcore Public RESTful API Specifications** ## Python Library - Check the [documentation](https://itisfoundation.github.io/osparc-simcore-python-client) - Quick install: ``pip install git+https://github.com/ITISFoundation/osparc-simcore-python-client.git``   # noqa: E501

    The version of the OpenAPI document: 0.4.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from osparc.configuration import Configuration


class FileMetadata(object):
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
        'file_id': 'str',
        'filename': 'str',
        'content_type': 'str',
        'checksum': 'str'
    }

    attribute_map = {
        'file_id': 'file_id',
        'filename': 'filename',
        'content_type': 'content_type',
        'checksum': 'checksum'
    }

    def __init__(self, file_id=None, filename=None, content_type=None, checksum=None, local_vars_configuration=None):  # noqa: E501
        """FileMetadata - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._file_id = None
        self._filename = None
        self._content_type = None
        self._checksum = None
        self.discriminator = None

        if file_id is not None:
            self.file_id = file_id
        self.filename = filename
        if content_type is not None:
            self.content_type = content_type
        self.checksum = checksum

    @property
    def file_id(self):
        """Gets the file_id of this FileMetadata.  # noqa: E501

        File unique identifier built upon its name and checksum  # noqa: E501

        :return: The file_id of this FileMetadata.  # noqa: E501
        :rtype: str
        """
        return self._file_id

    @file_id.setter
    def file_id(self, file_id):
        """Sets the file_id of this FileMetadata.

        File unique identifier built upon its name and checksum  # noqa: E501

        :param file_id: The file_id of this FileMetadata.  # noqa: E501
        :type: str
        """

        self._file_id = file_id

    @property
    def filename(self):
        """Gets the filename of this FileMetadata.  # noqa: E501

        File with extenson  # noqa: E501

        :return: The filename of this FileMetadata.  # noqa: E501
        :rtype: str
        """
        return self._filename

    @filename.setter
    def filename(self, filename):
        """Sets the filename of this FileMetadata.

        File with extenson  # noqa: E501

        :param filename: The filename of this FileMetadata.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and filename is None:  # noqa: E501
            raise ValueError("Invalid value for `filename`, must not be `None`")  # noqa: E501

        self._filename = filename

    @property
    def content_type(self):
        """Gets the content_type of this FileMetadata.  # noqa: E501


        :return: The content_type of this FileMetadata.  # noqa: E501
        :rtype: str
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type):
        """Sets the content_type of this FileMetadata.


        :param content_type: The content_type of this FileMetadata.  # noqa: E501
        :type: str
        """

        self._content_type = content_type

    @property
    def checksum(self):
        """Gets the checksum of this FileMetadata.  # noqa: E501

        MD5 hash of the file's content  # noqa: E501

        :return: The checksum of this FileMetadata.  # noqa: E501
        :rtype: str
        """
        return self._checksum

    @checksum.setter
    def checksum(self, checksum):
        """Sets the checksum of this FileMetadata.

        MD5 hash of the file's content  # noqa: E501

        :param checksum: The checksum of this FileMetadata.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and checksum is None:  # noqa: E501
            raise ValueError("Invalid value for `checksum`, must not be `None`")  # noqa: E501

        self._checksum = checksum

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
        if not isinstance(other, FileMetadata):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FileMetadata):
            return True

        return self.to_dict() != other.to_dict()