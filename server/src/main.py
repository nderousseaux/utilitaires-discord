"""Entry point of application"""

from time import sleep

from utils import get_env_var, get_time_to_wait
from discord_api import init, set_token, update_group_name

if __name__ == "__main__":

    #Getting the environment variables
    discord, timeout = get_env_var()

    #Setting the discord api
    init(discord['base_url'])

    #Set token
    set_token(discord['credentials'])


    #Main program
    while True:
        update_group_name(discord['id_group'], "new_name_3")

        sleep(get_time_to_wait(timeout))
