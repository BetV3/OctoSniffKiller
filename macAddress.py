import requests
import scapy.layers.all
from scapy.sendrecv import srp
from scapy.layers.l2 import ARP, Ether
def get_vendors(mac_address):
    url = 'https://api.macvendors.com/'
    response = requests.get(url+mac_address)
    if response.status_code != 200:
        pass
    else:
        return response.content.decode()
def get_mac(ip):
    arp = ARP(pdst = ip)
    broadcast = Ether(dst='ff:ff:ff:ff:ff:ff')
    packet = broadcast / arp
    answered_list = srp(packet, timeout=5, verbose=False)[0]
    clients = []
    for sent, received in answered_list:
        clients.append({'ip': received.psrc, 'mac': received.hwsrc})
    return clients