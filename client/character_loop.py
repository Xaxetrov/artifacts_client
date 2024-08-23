import time

import openapi_client
import openapi_client.api_client

import client.character_action as character_action

def character_action_loop(name: str, api_client: openapi_client.api_client.ApiClient):

    loop = True
    y = 0
    # Create an instance of the API class
    characters_api = openapi_client.MyCharactersApi(api_client)

    while(loop):
        
        movement_data = character_action.move(name, 0, y, characters_api)
        if movement_data is not None:
            time.sleep(movement_data.cooldown.total_seconds)
        y = 1 - y
