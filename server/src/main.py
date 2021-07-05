"""Entry point of application"""

from utils import check_env_var

if __name__ == "__main__":

    #Checking the consistency of environment variables
    check_env_var()

    print("Hello world")
