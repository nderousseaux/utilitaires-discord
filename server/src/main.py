"""Entry point of application"""

from utils import get_env_var

if __name__ == "__main__":

    #Getting the environment variables 
    credential, group, timeout = get_env_var()

    print('Done')
