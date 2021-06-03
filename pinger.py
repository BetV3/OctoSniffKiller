import interfaces as inter
import scapy
from netaddr.ip import IPAddress

def get_bits(netmask):
    return IPAddress(netmask).netmask_bits()
def get_client(iface):
    ans, unans = scapy.layers.l2.arping()
