import subprocess

interface = "eth0"  # Replace with your network interface name
new_mac = "69:69:69:69:69"  # Replace with your desired MAC address

def change_mac(interface, new_mac):

    print(f"Changing MAC address of {interface} to {new_mac}")

    subprocess.call(["sudo", "ifconfig", interface, "down"])
    subprocess.call(["sudo", "ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["sudo", "ifconfig", interface, "up"])

change_mac(interface, new_mac)

new_device_name = "new_device_name"  # Replace with your desired device name
def change_device_name(interface, new_device_name):
    print(f"Changing device name of {interface} to {new_device_name}")

    subprocess.call(["sudo", "ip", "link", "set", "dev", interface, "name", new_device_name])

print("MAC address and device name changed successfully.")

