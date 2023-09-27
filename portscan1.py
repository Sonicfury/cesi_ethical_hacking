#!/usr/bin/python

import requests
import socket


def get_public_ip():
    response = requests.get('https://api.ipify.org')
    return response.text


def portscanner(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    result = s.connect_ex((host, port))
    s.close()

    return f"Port ouvert {port}" if result == 0 else f"Port fermé {port}"


host = get_public_ip()

print(f"Scanning ports on {host}")

for i in range(1, 1024):
    print(portscanner(host, i))

