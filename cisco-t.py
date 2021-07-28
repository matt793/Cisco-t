#!/usr/bin/python3
from time import sleep
from os import system

# Connect
print("""
░█████╗░██╗░██████╗░█████╗░░█████╗░░░░░░░████████╗
██╔══██╗██║██╔════╝██╔══██╗██╔══██╗░░░░░░╚══██╔══╝
██║░░╚═╝██║╚█████╗░██║░░╚═╝██║░░██║█████╗░░░██║░░░
██║░░██╗██║░╚═══██╗██║░░██╗██║░░██║╚════╝░░░██║░░░
╚█████╔╝██║██████╔╝╚█████╔╝╚█████╔╝░░░░░░░░░██║░░░
░╚════╝░╚═╝╚═════╝░░╚════╝░░╚════╝░░░░░░░░░░╚═╝░░░
Run cisco-t connect?

    If yes type '1'.
    If no type '2'.

""")

choice = str(input("Type choice here: "))

if choice == '1':
    # Show connection to USB driver
    system("sudo dmesg | grep 'ttyUSB'")
    sleep(1.5)    
    print("""

    Connecting in 3 seconds...
    """)
    sleep(.5)
    # Count down
    sleep(1)
    print("    ...3")
    sleep(1)
    print("        ...2")
    sleep(1)
    print("             ...1")
    sleep(.5)
    # Connecting to hardware via screen
    system("sudo screen /dev/ttyUSB0")

if choice == '2':
    exit()