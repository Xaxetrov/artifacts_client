# coding: utf-8

"""
    Artifacts API

     Artifacts is an API-based MMO game where you can manage 5 characters to explore, fight, gather resources, craft items and much more.  Website: https://artifactsmmo.com/  Documentation: https://docs.artifactsmmo.com/  OpenAPI Spec: https://api.artifactsmmo.com/openapi.json 

    The version of the OpenAPI document: 1.6
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.grand_exchange_api import GrandExchangeApi


class TestGrandExchangeApi(unittest.TestCase):
    """GrandExchangeApi unit test stubs"""

    def setUp(self) -> None:
        self.api = GrandExchangeApi()

    def tearDown(self) -> None:
        pass

    def test_get_all_ge_items_ge_get(self) -> None:
        """Test case for get_all_ge_items_ge_get

        Get All Ge Items
        """
        pass

    def test_get_ge_item_ge_code_get(self) -> None:
        """Test case for get_ge_item_ge_code_get

        Get Ge Item
        """
        pass


if __name__ == '__main__':
    unittest.main()