"""Entry point of application"""

from time import sleep

from utils import get_env_var, get_time_to_wait


if __name__ == "__main__":

    #Getting the environment variables
    credential, group, timeout = get_env_var()

    while True:

        print("One Loop")

        sleep(get_time_to_wait(timeout))