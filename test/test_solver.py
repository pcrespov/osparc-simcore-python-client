# coding: utf-8

"""
    Public API Server

    **osparc-simcore Public RESTful API Specifications** ## Python Library - Check the [documentation](https://itisfoundation.github.io/osparc-simcore-python-client) - Quick install: ``pip install git+https://github.com/ITISFoundation/osparc-simcore-python-client.git``   # noqa: E501

    The version of the OpenAPI document: 0.4.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import osparc
from osparc.models.solver import Solver  # noqa: E501
from osparc.rest import ApiException

class TestSolver(unittest.TestCase):
    """Solver unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Solver
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = osparc.models.solver.Solver()  # noqa: E501
        if include_optional :
            return Solver(
                uuid = '0', 
                name = '0', 
                version = '0', 
                version_aliases = [
                    '0'
                    ], 
                title = '0', 
                description = '0', 
                maintainer = '0', 
                released = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                solver_url = '0'
            )
        else :
            return Solver(
                uuid = '0',
                name = '0',
                version = '0',
                title = '0',
                maintainer = '0',
                solver_url = '0',
        )

    def testSolver(self):
        """Test Solver"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()