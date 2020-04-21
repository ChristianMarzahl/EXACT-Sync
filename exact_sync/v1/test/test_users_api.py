# coding: utf-8

"""
    EXACT - API

    API to interact with the EXACT Server  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from api.users_api import UsersApi  # noqa: E501
from swagger_client.rest import ApiException


class TestUsersApi(unittest.TestCase):
    """UsersApi unit test stubs"""

    def setUp(self):
        self.api = api.users_api.UsersApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_user(self):
        """Test case for create_user

        """
        pass

    def test_destroy_user(self):
        """Test case for destroy_user

        """
        pass

    def test_list_users(self):
        """Test case for list_users

        """
        pass

    def test_partial_update_user(self):
        """Test case for partial_update_user

        """
        pass

    def test_retrieve_user(self):
        """Test case for retrieve_user

        """
        pass

    def test_update_user(self):
        """Test case for update_user

        """
        pass


if __name__ == '__main__':
    unittest.main()