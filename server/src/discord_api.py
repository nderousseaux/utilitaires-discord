"""List of API calls for discord api"""

import requests

BASE_URL = ''
HEADERS = {}

def init(token, base_url):
    """Init authorization token and base url of discord api"""

    global BASE_URL, HEADERS

    BASE_URL = base_url
    HEADERS = {'authorization':token}


def update_group_name(id_group, new_name):
    """Update the name of a discord group"""

    response = requests.patch(BASE_URL + 'channels/' + id_group,
        headers=HEADERS,
        json={
            'name':new_name
        }
    )

    # If an error has occured
    if 200 < response.status_code > 299:
        raise ConnectionError(response.text)
