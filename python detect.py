import os
import subprocess

def ping_sweep(network):
    live_hosts = []
    for ip in range(1, 255):
        address = f"{network}.{ip}"
        res = subprocess.call(['ping', '-c', '1', address], stdout=subprocess.DEVNULL)
        if res == 0:
            live_hosts.append(address)
    return live_hosts

def main():
    network = input("Enter the first three octets of the network (e.g., 192.168.1): ")
    live_hosts = ping_sweep(network)
    print("Live hosts:")
    for host in live_hosts:
        print(host)

if __name__ == "__main__":
    main()