from curses import raw
import scapy.all as scapy

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

print("")

ip = raw_input("IpRange >  ")

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")    
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    
    clients_list = []
    for element in answered_list:
        client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        clients_list.append(client_dict)
    return clients_list  

def print_result(results_list):
    print("IP\t\t\tMAC ADDRESS\n-----------------------------------------------------------------------")
    for client in results_list:
        print(client["ip"] + "\t\t" + client["mac"])
        
       
scan_result = scan(ip)
print_result(scan_result)