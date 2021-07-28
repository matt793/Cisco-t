#!/usr/bin/python3
from time import sleep
from os import system

# Intro
print("""
Welcome to... 

░█████╗░██╗░██████╗░█████╗░░█████╗░░░░░░░████████╗
██╔══██╗██║██╔════╝██╔══██╗██╔══██╗░░░░░░╚══██╔══╝
██║░░╚═╝██║╚█████╗░██║░░╚═╝██║░░██║█████╗░░░██║░░░
██║░░██╗██║░╚═══██╗██║░░██╗██║░░██║╚════╝░░░██║░░░
╚█████╔╝██║██████╔╝╚█████╔╝╚█████╔╝░░░░░░░░░██║░░░
░╚════╝░╚═╝╚═════╝░░╚════╝░░╚════╝░░░░░░░░░░╚═╝░░░
                                            Setup.

Would you like to install dependencies?

                    Press 1 for yes.
                    Press 2 for no.

""")

# First menu
first = str(input("Type choice here: "))

if first == '2':
    exit()

if first == '1':
    sleep(1.5)
    print("""
    Choose your base Linux system:

            If you have a Debian based Linux enter 1.
            If you have a Arch based Linux enter 2.
            If you have a Fedora based Linux enter 3.

    """)

    # Second menu
    second = str(input("Type choice here: "))

    if second == '1':
        sleep(1)
        print("Installing for Debian...")
        sleep(1)
        system("sudo apt-get install util-linux -y && sudo apt-get install screen -y")
        exit()

    if second == '2':
        sleep(1)
        print("Installing for Arch...")
        sleep(1)
        system("sudo pacman -Syu util-linux && sudo pacman -Syu screen")
        exit()

    if second == '3':
        sleep(1)
        print("Installing for Fedora...")
        sleep(1)
        system("sudo dnf install util-linux -y && sudo dnf install screen -y")
        exit()    