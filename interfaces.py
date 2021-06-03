import netifaces

def get_interfaces():
    count = 1
    ifaces = []
    for iface in netifaces.interfaces():
        iface_details = netifaces.ifaddresses(iface)
        if netifaces.AF_INET in iface_details:
            print('Interface {}:'.format(count), end=' ')
            print(iface_details[netifaces.AF_INET])
            ifaces.append(iface_details)
            count = count + 1
    return ifaces