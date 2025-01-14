# coding: utf-8

"""
    Artifacts API

     Artifacts is an API-based MMO game where you can manage 5 characters to explore, fight, gather resources, craft items and much more.  Website: https://artifactsmmo.com/  Documentation: https://docs.artifactsmmo.com/  OpenAPI Spec: https://api.artifactsmmo.com/openapi.json 

    The version of the OpenAPI document: 1.6
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.item_effect_schema import ItemEffectSchema

class TestItemEffectSchema(unittest.TestCase):
    """ItemEffectSchema unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ItemEffectSchema:
        """Test ItemEffectSchema
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ItemEffectSchema`
        """
        model = ItemEffectSchema()
        if include_optional:
            return ItemEffectSchema(
                name = '',
                value = 56
            )
        else:
            return ItemEffectSchema(
                name = '',
                value = 56,
        )
        """

    def testItemEffectSchema(self):
        """Test ItemEffectSchema"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
