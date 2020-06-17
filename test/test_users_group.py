# coding: utf-8

"""
    Public API Server

    **osparc-simcore Public RESTful API Specifications** ## Python Client - Github [repo](https://github.com/ITISFoundation/osparc-simcore-python-client) - Quick install: ``pip install git+https://github.com/ITISFoundation/osparc-simcore-python-client.git``   # noqa: E501

    The version of the OpenAPI document: 0.2.1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import osparc
from osparc.models.users_group import UsersGroup  # noqa: E501
from osparc.rest import ApiException

class TestUsersGroup(unittest.TestCase):
    """UsersGroup unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test UsersGroup
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = osparc.models.users_group.UsersGroup()  # noqa: E501
        if include_optional :
            return UsersGroup(
                gid = '0', 
                label = '0', 
                description = '0'
            )
        else :
            return UsersGroup(
                gid = '0',
                label = '0',
        )

    def testUsersGroup(self):
        """Test UsersGroup"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()