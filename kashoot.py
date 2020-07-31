import requests
from colorama import Fore, init
import random
import string
import platform
from subprocess import call
init()


def clear():
    if platform.system() == 'Windows':
        call(['cls'], shell=True)
    elif platform.system() == 'Linux':
        call(['clear'], shell=True)
    elif platform.system() == 'Darwin':
        call(['clear'], shell=True)


def main():
    clear()
    print(f'''
    ####################################
    #                                  #
    #   Kahoot Pin Bruteforce - {Fore.LIGHTRED_EX}Vito{Fore.RESET}   #
    #                                  #
    ####################################
    ''')
    print(f'[{Fore.CYAN}-{Fore.RESET}] Checking for valid kahoot pins!\n')
    while True:
        pin = ''.join((random.choice(string.digits) for i in range(6)))
        req = requests.get(f'https://kahoot.it/reserve/session/{pin}')
        if req.status_code == 200:
            print(f'[{Fore.LIGHTGREEN_EX}+{Fore.RESET}] Found valid pin! Pin: {pin}')
        else:
            pass

main()