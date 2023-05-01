import os
import requests
import time
import json

from textwrap import fill
from colorama import init, Fore


webhook_id = "WEBHOOK_ID"
webhook_token = "WEBHOOK_TOKEN"



while True:

    os.system('cls' if os.name=='nt' else 'clear')

    print(Fore.BLUE + "                                           /$$    /$$                    /$$   /$$                       /$$      /$$           /$$       /$$                           /$$      ")                                                        
    print(Fore.BLUE + "                                          | $$   | $$                   |__/  | $$                      | $$  /$ | $$          | $$      | $$                          | $$      ")
    print(Fore.BLUE + "                                          | $$   | $$ /$$$$$$  /$$$$$$$  /$$ /$$$$$$   /$$   /$$        | $$ /$$$| $$  /$$$$$$ | $$$$$$$ | $$$$$$$   /$$$$$$   /$$$$$$ | $$   /$$")
    print(Fore.BLUE + "                                          |  $$ / $$/|____  $$| $$__  $$| $$|_  $$_/  | $$  | $$ /$$$$$$| $$/$$ $$ $$ /$$__  $$| $$__  $$| $$__  $$ /$$__  $$ /$$__  $$| $$  /$$/")
    print(Fore.BLUE + "                                           \  $$ $$/  /$$$$$$$| $$  \ $$| $$  | $$    | $$  | $$|______/| $$$$_  $$$$| $$$$$$$$| $$  \ $$| $$  \ $$| $$  \ $$| $$  \ $$| $$$$$$/ ")
    print(Fore.BLUE + "                                            \  $$$/  /$$__  $$| $$  | $$| $$  | $$ /$$| $$  | $$        | $$$/ \  $$$| $$_____/| $$  | $$| $$  | $$| $$  | $$| $$  | $$| $$_  $$ ")
    print(Fore.BLUE + "                                             \  $/  |  $$$$$$$| $$  | $$| $$  |  $$$$/|  $$$$$$$        | $$/   \  $$|  $$$$$$$| $$$$$$$/| $$  | $$|  $$$$$$/|  $$$$$$/| $$ \  $$")
    print(Fore.BLUE + "                                              \_/    \_______/|__/  |__/|__/   \___/   \____  $$        |__/     \__/ \_______/|_______/ |__/  |__/ \______/  \______/ |__/  \__/")
    print(Fore.BLUE + "                                                                                       /$$  | $$                                                                                 ")
    print(Fore.BLUE + "                                                                                      |  $$$$$$/                                                                                 ")
    print(Fore.BLUE + "                                                       Made by 94ttt#2413              \______/                                                                                  \n")
    print(Fore.BLUE + "                                                                                                                                                                                  ")
    print(Fore.WHITE + "                                                                       ╔═══════════════════════════════════════════════════════════════════════════╗                             ")
    print(Fore.WHITE + "                                                                       ╬ (1)  Webhook Spammer       (2)  Webhook Checker       (3)  Credits        ╬                             ")
    print(Fore.WHITE + "                                                                       ╬ (4)  Webhook Deleter       (5)  pfp changer           (6)  Custom message ╬                             ")
    print(Fore.WHITE + "                                                                       ╬ (7)  soon                  (8)  soon                  (9)  soon           ╬                             ")
    print(Fore.WHITE + "                                                                       ╚═══════════════════════════════════════════════════════════════════════════╝                             ")
    print(Fore.WHITE + "                                                                                                                                        [-]  Page 1                              ")
    print("\n\n")

# Fore.BLUE + 
# Fore.WHITE + 
# Fore.RED + 

    select = input(Fore.RED + "-----------------------------------------------[+] Select an option: ")
    if select == "1":
        print("")

        os.system('cls' if os.name=='nt' else 'clear')

        print("!   Webhook Spammer   !")
        print("")
        print("")
        print("")
        webhook_url = input("[+] Webhook url: ")

        spamming = True
        
        if spamming == True:
            message = input("[+] Message to send: ")
            print("")
            while spamming == True:

                data = {
                    "content": message
                }

                response = requests.post(webhook_url, json=data)

            print("")
            print("[+] Messages send")
            print("")

        time.sleep(2)
        continue

    if select == "2":
        print("")

        time.sleep(0.5)

        os.system('cls' if os.name=='nt' else 'clear')

        print("!   Webhook Checker   !")
        print("")
        print("")
        print("")
        webhook_url = input("[+] Webhook url: ")

        data = {
            "content": "```Your Webhook is working!```"
        }
        response = requests.post(webhook_url, json=data)

        print("")
        print("[+] Message send!")

        time.sleep(2)
        continue

    if select == "3":
        print("")

        os.system('cls' if os.name=='nt' else 'clear')

        print("!    Credits    !")
        print("")
        print("")
        print("")
        print("[-]  Made by 94ttt#2413")
        print("")
        print("[-]  Join the Discord: [termed]")
        print("")
        print("")
        print("(0)  Go back")
        print("")
        print("")
        select = input("[+] Select an option: ")
        if select == "0":
            continue
    if select == "0":
        time.sleep(2)
        continue
    if select == "4":
        print("")

        os.system('cls' if os.name=='nt' else 'clear')

        print("!   Webhook Deleter   !")
        print("")
        print("")
        print("")

        webhook_url = input("[+] Webhook Url: ")
        response = requests.delete(webhook_url)

        if response.status_code == 204:
            print("Webhook deleted successfully")
        time.sleep(2)
        continue

    
    if select == "5":
        print("")

        os.system('cls' if os.name=='nt' else 'clear')

        print("!    Profile picture changer    !")
        print("")
        print("!          In Progress          !")
        print("")
        

    if select == "6":


        print("")

        os.system('cls' if os.name=='nt' else 'clear')

        print("!    Custom message    !")
        print("")
        print("")
        print("")
        webhook_url = input("[+] Webhook url: ")
        print("")
        custommessage = input("[+] Message you want to send: ")
        if webhook_url:
            data = {
                "content": custommessage
            }
            requests.post(webhook_url, json=data)

            print("\nmessage sent successfully!")
        else:
            print()

    time.sleep(3)
    continue

    # if select == 



        

# Btw why are you looking at the code?
