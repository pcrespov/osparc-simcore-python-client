# coding: utf-8

"""
    Public API Server

    **osparc-simcore Public RESTful API Specifications** ## Python Client - Github [repo](https://github.com/ITISFoundation/osparc-simcore-python-client) - Quick install: ``pip install git+https://github.com/ITISFoundation/osparc-simcore-python-client.git``   # noqa: E501

    The version of the OpenAPI document: 0.3.0
    Generated by: https://openapi-generator.tech
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "osparc-simcore-python-api"
VERSION = "0.3.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="Public API Server",
    author="OpenAPI Generator community",
    author_email="team@openapitools.org",
    url="https://github.com/ITISFoundation/osparc-simcore-python-client.git",
    keywords=["OpenAPI", "OpenAPI-Generator", "Public API Server"],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    long_description="""\
    **osparc-simcore Public RESTful API Specifications** ## Python Client - Github [repo](https://github.com/ITISFoundation/osparc-simcore-python-client) - Quick install: &#x60;&#x60;pip install git+https://github.com/ITISFoundation/osparc-simcore-python-client.git&#x60;&#x60;   # noqa: E501
    """
)
