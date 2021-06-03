import scapy.all
import netifaces
from scapy.all import *
from scapy.all import ARP
from scapy.layers.inet import IP
import netaddr
from netaddr.ip import IPAddress, IPNetwork
from scapy.layers.l2 import Ether
import requests
import argparse
import interfaces as inter
import macAddress as mac
import pinger as ping
import devices
import socket
import time

iface_chosen = 0
interfaces = inter.get_interfaces()   
try:
    iface_chosen = int(input('Choose what interface you would like to use. \n')) - 1
except ValueError as ve:
    print('You entered an invalid character')
if iface_chosen >= len(interfaces) or iface_chosen < 0:
    print('Invalid Interface Number. Please Try Again')
macAddr = interfaces[iface_chosen][netifaces.AF_LINK][0]['addr']
ipAddr = interfaces[iface_chosen][netifaces.AF_INET][0]['addr']
netmask = interfaces[iface_chosen][netifaces.AF_INET][0]['netmask']
netmask_bits = ping.get_bits(netmask)
net = '{}/{}'.format(ipAddr, netmask_bits)
network = IPNetwork(net)
target = '{}/{}'.format(network.network, netmask_bits)
clients = mac.get_mac(target)
if clients == 0:
    print('The network interface you choose has no connected devices. Are you hard wired into your console? y/n')
else:
    print('You chose the interface with MAC Address of {} and LAN IP of {}'.format(macAddr, ipAddr))
print('You have {} clients'.format(len(clients)))
count = 1
for client in clients:
    vendor = mac.get_vendors(client['mac'])
    if vendor == None:
        print('Client {}'.format(count), end=' ')
        print(str(client['mac'])+' -> {}'.format(client['ip']))
        count = count + 1
        continue
    print('Client {}'.format(count), end=' ')
    print(str(vendor)+ ' -> {}'.format(client['ip']))
    count = count + 1
    time.sleep(1)
router = devices.choose_router(clients)
console = devices.choose_console(clients)



