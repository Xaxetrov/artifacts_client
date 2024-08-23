from openapi_client.api.my_characters_api import MyCharactersApi
from openapi_client.models.destination_schema import DestinationSchema
from openapi_client.rest import ApiException


def move(name: str, x: int, y: int, characters_api: MyCharactersApi):
    destination_schema = DestinationSchema(x = x, y = y)

    try:
        api_response = characters_api.action_move_my_name_action_move_post(name, destination_schema)
    except ApiException as e:
        if e.status == 490:
            print('Ignored exception: %s\n' % e)
            return None
    else:
        return api_response.data