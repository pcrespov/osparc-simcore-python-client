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
from osparc.models.profile import Profile  # noqa: E501
from osparc.rest import ApiException

class TestProfile(unittest.TestCase):
    """Profile unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Profile
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = osparc.models.profile.Profile()  # noqa: E501
        if include_optional :
            return Profile(
                first_name = 'James', 
                last_name = 'Maxwell', 
                login = '0', 
                role = 'ANONYMOUS', 
                groups = osparc.models.groups.Groups(
                    me = osparc.models.users_group.UsersGroup(
                        gid = '0', 
                        label = '0', 
                        description = '0', ), 
                    organizations = [
                        osparc.models.users_group.UsersGroup(
                            gid = '0', 
                            label = '0', 
                            description = '0', )
                        ], 
                    all = osparc.models.users_group.UsersGroup(
                        gid = '0', 
                        label = '0', 
                        description = '0', ), ), 
                gravatar_id = '0'
            )
        else :
            return Profile(
                login = '0',
                role = 'ANONYMOUS',
        )

    def testProfile(self):
        """Test Profile"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
