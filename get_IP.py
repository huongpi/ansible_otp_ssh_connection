#!/usr/bin/env python
import socket
import os
def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(0)
    try:
        s.connect(('10.254.254.254', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP
def get_link(IP):
    a_string = 'http://:8200'
    index = a_string.find(':8200')
    a_string = a_string[:index] + IP + a_string[index:]
    return a_string
if __name__ == "__main__":
    print(get_link(get_ip()))

