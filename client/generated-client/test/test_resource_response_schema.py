# coding: utf-8

"""
    Artifacts API

     Artifacts is an API-based MMO game where you can manage 5 characters to explore, fight, gather resources, craft items and much more.  Website: https://artifactsmmo.com/  Documentation: https://docs.artifactsmmo.com/  OpenAPI Spec: https://api.artifactsmmo.com/openapi.json 

    The version of the OpenAPI document: 1.6
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.resource_response_schema import ResourceResponseSchema

class TestResourceResponseSchema(unittest.TestCase):
    """ResourceResponseSchema unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ResourceResponseSchema:
        """Test ResourceResponseSchema
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ResourceResponseSchema`
        """
        model = ResourceResponseSchema()
        if include_optional:
            return ResourceResponseSchema(
                data = openapi_client.models.resource_schema.ResourceSchema(
                    name = '', 
                    code = '', 
                    skill = 'mining', 
                    level = 56, 
                    drops = [
                        openapi_client.models.drop_rate_schema.DropRateSchema(
                            code = 'z', 
                            rate = 1.0, 
                            min_quantity = 1.0, 
                            max_quantity = 1.0, )
                        ], )
            )
        else:
            return ResourceResponseSchema(
                data = openapi_client.models.resource_schema.ResourceSchema(
                    name = '', 
                    code = '', 
                    skill = 'mining', 
                    level = 56, 
                    drops = [
                        openapi_client.models.drop_rate_schema.DropRateSchema(
                            code = 'z', 
                            rate = 1.0, 
                            min_quantity = 1.0, 
                            max_quantity = 1.0, )
                        ], ),
        )
        """

    def testResourceResponseSchema(self):
        """Test ResourceResponseSchema"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
