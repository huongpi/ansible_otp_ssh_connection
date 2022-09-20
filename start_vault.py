#!/usr/bin/env python
import subprocess 
from get_IP import *

def start_vault(IP):
    a_string = "vault server -dev -dev-root-token-id root -dev-listen-address :8200"
    index = a_string.find(':')
    a_string = a_string[:index] + IP + a_string[index:]
    os.system(a_string)
    # CMD = 'echo $(source start_vault.sh; echo $%s)' 
    # p = subprocess.Popen(CMD, stdout=subprocess.PIPE, shell=True, executable='/bin/bash')  
if __name__ == "__main__":
    start_vault(get_ip())

