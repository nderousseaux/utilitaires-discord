"""Some useful functions for this app"""

from os import environ


def get_env_var():
    """Checking the consistency of environment variables"""

    credentials = get_env_authen() # {token} or {login, password}

    group = get_env_group() # {id_group}

    timeout = get_env_timeout() # {fixed_duration} or {min_duration, max_duration}

    return credentials, group, timeout


def get_env_authen():
    """Checking the consistency of environment variables for authentification"""

    credentials = {}

    # Checking if UTDI_TOKEN is not defined at the same time as UTDI_LOGIN or UTDI_PASSWORD
    if (
        'UTDI_TOKEN' in environ.keys() and
        ('UTDI_LOGIN' in environ.keys() or 'UTDI_PASSWORD' in environ.keys())
    ):
        raise EnvironmentError(
            'The environment variables UTDI_LOGIN/UTDI_PASSWORD and UTDI_TOKEN are all declared.'
            'Please choose between an authentication by login/password or an authentification by token : Not both at the same time.'
        )

    # Checking if UTDI_TOKEN is set
    if 'UTDI_TOKEN' in environ.keys():

        # Verifing if UTDI_TOKEN is not an empty string
        if not environ['UTDI_TOKEN']:
            raise EnvironmentError('The UTDI_TOKEN environment variable is set but its value is an empty string.')
        
        else:
            credentials['token'] = environ['UTDI_TOKEN']

    # Checking if UTDI_LOGIN is set
    elif 'UTDI_LOGIN' in environ.keys():

        # Verifing if UTDI_LOGIN is not an empty string
        if not environ['UTDI_LOGIN']:
            raise EnvironmentError('The UTDI_LOGIN environment variable is set but its value is an empty string.')

        credentials['login'] = environ['UTDI_LOGIN']

        # Checking if UTDI_PASSWORD is set
        if not 'UTDI_PASSWORD' in environ.keys():
            raise EnvironmentError('The UTDI_PASSWORD is not set.')

        # Verifing if UTDI_PASSWORD is not an empty string
        if not environ['UTDI_PASSWORD']:
            raise EnvironmentError('The UTDI_PASSWORD environment variable is set but its value is an empty string.')
        
        credentials['password'] = environ['UTDI_PASSWORD']

    else:
        raise EnvironmentError(
            'No UTDI_LOGIN/PASSWORD or UTDI_TOKEN environment variables is declared.'
            'Please declare a way of authentication: LOGIN/PASSWORD or TOKEN.'
        )

    return credentials

def get_env_group():
    """Checking the consistency of environment variables for group"""

    group = {}

    # Checking if UTDI_ID_GROUP is defined
    if 'UTDI_ID_GROUP' in environ.keys():

        # Verifing if UTDI_ID_GROUP is not an empty string
        if not environ['UTDI_ID_GROUP']:
            raise EnvironmentError('The UTDI_ID_GROUP environment variable is set but its value is an empty string.')

        group['id_group'] = environ['UTDI_ID_GROUP']

    else:
        raise EnvironmentError('The UTDI_ID_GROUP environment variable is not set.')

    return group

def get_env_timeout():
    """Checking the consistency of environment variables for update time"""

    timeout = {}

    # Checking if UTDI_UPDATE_TIMEOUT is not defined at the same time as UTDI_UPDATE_TIMEOUT_MIN or UTDI_UPDATE_TIMEOUT_MAX
    if (
        'UTDI_UPDATE_TIMEOUT' in environ.keys() and
        ('UTDI_UPDATE_TIMEOUT_MIN' in environ.keys() or 'UTDI_UPDATE_TIMEOUT_MAX' in environ.keys())
    ):
        raise EnvironmentError(
            'The environment variables UTDI_UPDATE_TIMEOUT_MIN/UTDI_UPDATE_TIMEOUT_MAX and UTDI_UPDATE_TIMEOUT are all declared.'
            'Please choose between a random update time (UTDI_UPDATE_TIMEOUT_MIN/MAX) or fix update time (UTDI_UPDATE_TIMEOUT) : Not both at the same time.'
        )

    # Checking if UTDI_UPDATE_TIMEOUT is set
    if 'UTDI_UPDATE_TIMEOUT' in environ.keys():

        # Verifing if UTDI_UPDATE_TIMEOUT is not an empty string
        if not environ['UTDI_UPDATE_TIMEOUT']:
            raise EnvironmentError('The UTDI_UPDATE_TIMEOUT environment variable is set but its value is an empty string.')

        # Verifing if UTDI_UPDATE_TIMEOUT is an int
        try:
            int(environ['UTDI_UPDATE_TIMEOUT'])
        except Exception as exception:
            raise EnvironmentError('The UTDI_UPDATE_TIMEOUT environment variable is set but its value cannot be cast to integer') from exception

        timeout['fixed_duration'] = int(environ['UTDI_UPDATE_TIMEOUT'])

    # Checking if UTDI_UPDATE_TIMEOUT_MIN is set
    elif 'UTDI_UPDATE_TIMEOUT_MIN' in environ.keys():

        # Verifing if UTDI_UPDATE_TIMEOUT_MIN is not an empty string
        if not environ['UTDI_UPDATE_TIMEOUT_MIN']:
            raise EnvironmentError('The UTDI_UPDATE_TIMEOUT_MIN environment variable is set but its value is an empty string.')

        # Verifing if UTDI_UPDATE_TIMEOUT_MIN is an int
        try:
            int(environ['UTDI_UPDATE_TIMEOUT'])
        except Exception as exception:
            raise EnvironmentError('The UTDI_UPDATE_TIMEOUT environment variable is set but its value cannot be cast to integer') from exception

        timeout['min_duration'] = int(environ['UTDI_UPDATE_TIMEOUT_MIN'])

        # Checking if UTDI_UPDATE_TIMEOUT_MAX is set
        if not 'UTDI_UPDATE_TIMEOUT_MAX' in environ.keys():
            raise EnvironmentError('The UTDI_UPDATE_TIMEOUT_MAX is not set.')

        # Verifing if UTDI_UPDATE_TIMEOUT_MAX is not an empty string
        if not environ['UTDI_UPDATE_TIMEOUT_MAX']:
            raise EnvironmentError('The UTDI_UPDATE_TIMEOUT_MAX environment variable is set but its value is an empty string.')

        # Verifing if UTDI_UPDATE_TIMEOUT_MAX is an int
        try:
            int(environ['UTDI_UPDATE_TIMEOUT_MAX'])
        except Exception as exception:
            raise EnvironmentError('The UTDI_UPDATE_TIMEOUT_MAX environment variable is set but its value cannot be cast to integer') from exception

        timeout['max_duration'] = int(environ['UTDI_UPDATE_TIMEOUT_MAX'])

    else:
        raise EnvironmentError(
            'No UTDI_UPDATE_TIMEOUT_MIN/MAX or UTDI_UPDATE_TIMEOUT environment variables is declared.'
            'Please declare a kind of update time : random (MIN/MAX) or fixed.'
        )

    return timeout
