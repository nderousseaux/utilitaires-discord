"""Entry point of application"""

from time import sleep

from utils import get_env_var, get_time_to_wait
from discord_api import init_discord, set_token, update_group_name
from ra_pha_api import init_ra_pha, get_sentence


if __name__ == "__main__":

    print("Start utdi_server")

    #Getting the environment variables
    discord, timeout = get_env_var()

    #Setting the discord api
    init_discord(discord['base_url'])

    #Set token
    set_token(discord['credentials'])

    #Setting the ra_pha api
    init_ra_pha('http://ra_pha:3000')

    #Main program
    while True:
        newName = get_sentence()

        update_group_name(discord['id_group'], newName)

        print("Update group n" + discord['id_group'] + " with the new name : " + newName)

        sleep(get_time_to_wait(timeout))
