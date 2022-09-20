#!/bin/bash

# Get vault server's address and export token
VAULT_ADDR=$(python3 get_IP.py)
VAULT_TOKEN=root

###SETUP THE SSH SECRETS ENGINE 

# Enable ssh secrets engine using /sys/mounts endpoint
curl --header "X-Vault-Token: $VAULT_TOKEN" \
       --request POST \
       --data '{"type":"ssh"}' \
       $VAULT_ADDR/v1/sys/mounts/ssh

# Create an API request payload containing the parameters to set a role
tee payload.json <<EOF
{
  "key_type": "otp",
  "default_user": "huong",
  "cidr_list": "10.208.180.0/22"
}
EOF

# Create a role using the ssh/roles/otp_key_role endpoint
curl --header "X-Vault-Token: $VAULT_TOKEN" \
       --request POST \
       --data @payload.json \
       $VAULT_ADDR/v1/ssh/roles/otp_key_role


###SETUP THE CLIENT AUTHENTICATION 

# Create an API request payload containing the stringified test policy
tee payload.json <<EOF
{
  "policy": "path \"ssh/creds/otp_key_role\" {\n capabilities = [ \"create\", \"read\", \"update\", \"list\" ]\n }"
}
EOF

# Create a policy named test with the policy defined in test.hcl
curl --header "X-Vault-Token: $VAULT_TOKEN" \
    --request PUT \
    --data @payload.json \
    $VAULT_ADDR/v1/sys/policies/acl/test

# Enable the userpass auth method
curl --header "X-Vault-Token: $VAULT_TOKEN" \
    --request POST \
    --data '{"type": "userpass"}' \
    $VAULT_ADDR/v1/sys/auth/userpass

# Create a user named ubuntu with the password "training" assigned the test policy
curl --header "X-Vault-Token: $VAULT_TOKEN" \
    --request POST \
    --data '{"password": "training", "policies": "test"}' \
    $VAULT_ADDR/v1/auth/userpass/users/huong
