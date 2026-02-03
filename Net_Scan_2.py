import scapy.all as scapy
import time

def scan_network_arp(ip_range):
    print(f"Scanning network range: {ip_range}")

    arp_request = scapy.ARP(pdst=ip_range)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request

    answered_list = scapy.srp(arp_request_broadcast, timeout=3, verbose=False)

    client_list = []
    for element in answered_list:
        client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        client_list.append(client_dict)
    
    print("IP Address\t\tMAC Address")
    print("--------------------------------------")

    for client in client_list:
        print(f"{client['ip']}\t\t{client['mac']}")
    return client_list

if __name__ == '__main__':
    target_range = "192.168.1.1/24"
    scan_network_arp(target_range)
