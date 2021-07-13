"""List of API calls for random_phrases API"""

import requests

BASE_URL = ''

def init_ra_pha(base_url):
    """Init base url of random_phrases api"""

    global BASE_URL

    BASE_URL = base_url


def get_sentence():
    """Get sentence from api"""

    response = requests.get(BASE_URL + '/?maxLength=100')

    # If an error has occured
    if 200 < response.status_code > 299:
        raise ConnectionError(response.text)

    return response.text
