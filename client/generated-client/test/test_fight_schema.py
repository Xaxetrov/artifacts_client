# coding: utf-8

"""
    Artifacts API

     Artifacts is an API-based MMO game where you can manage 5 characters to explore, fight, gather resources, craft items and much more.  Website: https://artifactsmmo.com/  Documentation: https://docs.artifactsmmo.com/  OpenAPI Spec: https://api.artifactsmmo.com/openapi.json 

    The version of the OpenAPI document: 1.6
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.fight_schema import FightSchema

class TestFightSchema(unittest.TestCase):
    """FightSchema unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FightSchema:
        """Test FightSchema
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FightSchema`
        """
        model = FightSchema()
        if include_optional:
            return FightSchema(
                xp = 56,
                gold = 56,
                drops = [
                    openapi_client.models.drop_schema.DropSchema(
                        code = '', 
                        quantity = 56, )
                    ],
                turns = 56,
                monster_blocked_hits = openapi_client.models.blocked_hits_schema.BlockedHitsSchema(
                    fire = 56, 
                    earth = 56, 
                    water = 56, 
                    air = 56, 
                    total = 56, ),
                player_blocked_hits = openapi_client.models.blocked_hits_schema.BlockedHitsSchema(
                    fire = 56, 
                    earth = 56, 
                    water = 56, 
                    air = 56, 
                    total = 56, ),
                logs = [
                    ''
                    ],
                result = 'win'
            )
        else:
            return FightSchema(
                xp = 56,
                gold = 56,
                drops = [
                    openapi_client.models.drop_schema.DropSchema(
                        code = '', 
                        quantity = 56, )
                    ],
                turns = 56,
                monster_blocked_hits = openapi_client.models.blocked_hits_schema.BlockedHitsSchema(
                    fire = 56, 
                    earth = 56, 
                    water = 56, 
                    air = 56, 
                    total = 56, ),
                player_blocked_hits = openapi_client.models.blocked_hits_schema.BlockedHitsSchema(
                    fire = 56, 
                    earth = 56, 
                    water = 56, 
                    air = 56, 
                    total = 56, ),
                logs = [
                    ''
                    ],
                result = 'win',
        )
        """

    def testFightSchema(self):
        """Test FightSchema"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
