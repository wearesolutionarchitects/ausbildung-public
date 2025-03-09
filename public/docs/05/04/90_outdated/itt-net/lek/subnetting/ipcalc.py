import ipaddress

def subnet_calculator(ip, mask):
    net = ipaddress.IPv4Network(f'{ip}/{mask}', strict=False)
    network_address = net.network_address
    broadcast_address = net.broadcast_address
    num_addresses = net.num_addresses
    num_hosts = num_addresses - 2  # Subtract network and broadcast addresses

    return {
        "network_address": str(network_address),
        "broadcast_address": str(broadcast_address),
        "num_addresses": num_addresses,
        "num_hosts": num_hosts
    }

ip = '192.168.1.0'
mask = 24
result = subnet_calculator(ip, mask)

print(f"Netzwerkadresse: {result['network_address']}")
print(f"Broadcast-Adresse: {result['broadcast_address']}")
print(f"Anzahl der Adressen: {result['num_addresses']}")
print(f"Anzahl der Hosts: {result['num_hosts']}")
