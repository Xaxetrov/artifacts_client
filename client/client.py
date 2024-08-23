from pathlib import Path

import openapi_client

from client.character_loop import character_action_loop


# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.artifactsmmo.com",
    access_token=Path('.token').read_text()
)


def run():
    # Enter a context with an instance of the API client
    with openapi_client.ApiClient(configuration) as api_client:
        character_action_loop('Firminy', api_client)

if __name__ == "__main__":
    run()