import subprocess

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
print("\n* https://www.youtube.com/techtronics101                          *")
print("\n****************************************************************")


interface = raw_input("Interface >  ")
new_mac = raw_input("New MAC >  ")


print("")
print ("[+]  Changing MAC ADDRESS for " + interface + " to " + new_mac )

subprocess.call("ifconfig " + interface + " down", shell=True)
subprocess.call("ifconfig " + interface + " hw ether " + new_mac, shell=True)
subprocess.call("ifconfig " + interface + " up", shell=True) 
print("")
subprocess.call("ifconfig " + interface , shell=True)

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