# coding: utf-8

"""
    Artifacts API

     Artifacts is an API-based MMO game where you can manage 5 characters to explore, fight, gather resources, craft items and much more.  Website: https://artifactsmmo.com/  Documentation: https://docs.artifactsmmo.com/  OpenAPI Spec: https://api.artifactsmmo.com/openapi.json 

    The version of the OpenAPI document: 1.6
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.status_response_schema import StatusResponseSchema

class TestStatusResponseSchema(unittest.TestCase):
    """StatusResponseSchema unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> StatusResponseSchema:
        """Test StatusResponseSchema
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `StatusResponseSchema`
        """
        model = StatusResponseSchema()
        if include_optional:
            return StatusResponseSchema(
                data = openapi_client.models.status_schema.StatusSchema(
                    status = '', 
                    version = '', 
                    characters_online = 56, 
                    server_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    announcements = [
                        openapi_client.models.announcement_schema.AnnouncementSchema(
                            message = '', 
                            created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                        ], 
                    last_wipe = '', 
                    next_wipe = '', )
            )
        else:
            return StatusResponseSchema(
                data = openapi_client.models.status_schema.StatusSchema(
                    status = '', 
                    version = '', 
                    characters_online = 56, 
                    server_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    announcements = [
                        openapi_client.models.announcement_schema.AnnouncementSchema(
                            message = '', 
                            created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                        ], 
                    last_wipe = '', 
                    next_wipe = '', ),
        )
        """

    def testStatusResponseSchema(self):
        """Test StatusResponseSchema"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
