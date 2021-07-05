"""Some useful functions for this app"""

from os import environ

def check_env_var():
    """Checking the consistency of environment variables"""

    check_env_authen()


def check_env_authen():
    """Checking the consistency of environment variables for authentification"""

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

    # Checking if UTDI_LOGIN is set
    elif 'UTDI_LOGIN' in environ.keys():

        # Verifing if UTDI_LOGIN is not an empty string
        if environ['UTDI_LOGIN']:

            # Checking if UTDI_PASSWORD is set
            if 'UTDI_PASSWORD' in environ.keys():

                # Verifing if UTDI_PASSWORD is not an empty string
                if not environ['UTDI_PASSWORD']:
                    raise EnvironmentError('The UTDI_PASSWORD environment variable is set but its value is an empty string.')

            else:
                raise EnvironmentError('The UTDI_PASSWORD is not set.')

        else:
            raise EnvironmentError('The UTDI_LOGIN environment variable is set but its value is an empty string.')

    else:
        raise EnvironmentError(
            'No UTDI_LOGIN/PASSWORD or UTDI_TOKEN environment variables is declared.'
            'Please declare a way of authentication: LOGIN/PASSWORD or TOKEN.'
        )
        