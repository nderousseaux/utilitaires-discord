"""List of API calls for discord api"""

import requests

BASE_URL = ''
HEADERS = {}

def init(base_url):
    """Init base url of discord api"""

    global BASE_URL

    BASE_URL = base_url


def set_token(credentials):
    """Set token of discord api"""

    token = ''

    #If authentification method is token
    if 'token' in credentials.keys():
        token = credentials['token']

    else:
        token = signin(credentials['login'], credentials['password'])

    global HEADERS
    HEADERS['authorization'] = token


def signin(login, password):
    """Log an user"""

    response = requests.post(BASE_URL + 'auth/login',
        headers=HEADERS,
        json={
            'login':login,
            'password': password
        }
    )

    # If an error has occured
    if 200 < response.status_code > 299:
        raise ConnectionError(response.text)

    #Return token
    return dict(response.json())['token']


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
