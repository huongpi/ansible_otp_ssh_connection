#!/bin/bash
VAULT_ADDR=$(python3 get_IP.py)
VAULT_TOKEN=root
UBUNTU_TOKEN=$(curl --silent --request POST  --data '{"password": "training"}' $VAULT_ADDR/v1/auth/userpass/login/huong | jq -r '.auth | .client_token')
TOKEN1=$(curl --silent --header "X-Vault-Token: $UBUNTU_TOKEN" --request POST --data '{"ip": "'"10.208.182.77"'"}' $VAULT_ADDR/v1/ssh/creds/otp_key_role | jq -r .data.key)
