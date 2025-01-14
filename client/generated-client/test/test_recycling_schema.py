# coding: utf-8

"""
    Artifacts API

     Artifacts is an API-based MMO game where you can manage 5 characters to explore, fight, gather resources, craft items and much more.  Website: https://artifactsmmo.com/  Documentation: https://docs.artifactsmmo.com/  OpenAPI Spec: https://api.artifactsmmo.com/openapi.json 

    The version of the OpenAPI document: 1.6
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.recycling_schema import RecyclingSchema

class TestRecyclingSchema(unittest.TestCase):
    """RecyclingSchema unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RecyclingSchema:
        """Test RecyclingSchema
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RecyclingSchema`
        """
        model = RecyclingSchema()
        if include_optional:
            return RecyclingSchema(
                code = 'z',
                quantity = 1.0
            )
        else:
            return RecyclingSchema(
                code = 'z',
        )
        """

    def testRecyclingSchema(self):
        """Test RecyclingSchema"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
