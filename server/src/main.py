"""Entry point of application"""

from time import sleep
from datetime import datetime, timedelta

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

        now = datetime.now()
        
        wait = get_time_to_wait(timeout)


        #On affiche les logs
        print("\n")
        print(
            now.strftime("%d/%m/%Y %H:%M:%S"),
            ": Group n°", discord['id_group']
        )
        print("| New name : ", newName)
        print("| Wait for " + str(wait) + " seconds")
        print(
            "| Next update at ",
            (now + timedelta(seconds=wait)).strftime("%d/%m/%Y %H:%M:%S")
        )

        sleep(wait)
