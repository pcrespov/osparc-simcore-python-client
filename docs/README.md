# Current Version

![test](https://github.com/ITISFoundation/osparc-simcore-python-client/workflows/test/badge.svg)


Python client for osparc-simcore Public RESTful API

- API version: 0.3.0
- Package version: 0.3.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

# Requirements

Python 3.6+

# Installation & Usage
## pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/ITISFoundation/osparc-simcore-python-client.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/ITISFoundation/osparc-simcore-python-client.git`)

Then import the package:

```python
import osparc
```

## Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:

```python
import osparc
```

# Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import osparc
from osparc.rest import ApiException
from pprint import pprint


 Defining host is optional and default to http://localhost
configuration.host = "http://localhost"
 Enter a context with an instance of the API client
with osparc.ApiClient(configuration) as api_client:
     Create an instance of the API class
    api_instance = osparc.MetaApi(api_client)

    try:
         Get Service Metadata
        api_response = api_instance.get_service_metadata()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MetaApi->get_service_metadata: %s\n" % e)

```

# Documentation for API Endpoints

All URIs are relative to *http://localhost*

| Class      | Method                                                           | HTTP request     | Description          |
| ---------- | ---------------------------------------------------------------- | ---------------- | -------------------- |
| *MetaApi*  | [**get_service_metadata**](md/MetaApi.md#get_service_metadata) | **GET** /v0/meta | Get Service Metadata |
| *UsersApi* | [**get_my_profile**](md/UsersApi.md#get_my_profile)            | **GET** /v0/me   | Get My Profile       |
| *UsersApi* | [**update_my_profile**](md/UsersApi.md#update_my_profile)      | **PUT** /v0/me   | Update My Profile    |


# Documentation For Models

 - [Groups](md/Groups.md)
 - [HTTPValidationError](md/HTTPValidationError.md)
 - [Meta](md/Meta.md)
 - [Profile](md/Profile.md)
 - [ProfileUpdate](md/ProfileUpdate.md)
 - [UsersGroup](md/UsersGroup.md)
 - [ValidationError](md/ValidationError.md)


# Documentation For Authorization


# HTTPBasic

- **Type**: HTTP basic authentication


# Author

Done with *tons of love* at [Zurich43](https://z43.swiss/)

