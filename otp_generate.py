#!/usr/bin/env python
import json
import argparse
import subprocess 
import os

def get_OTP(varname):
    CMD = 'echo $(source get_otp_using_API.sh; echo $%s)' % varname
    p = subprocess.Popen(CMD, stdout=subprocess.PIPE, shell=True, executable='/bin/bash')
    return p.stdout.readlines()[0].strip()

def get_result():
    return json.dumps(inventory(get_OTP('TOKEN1').decode('ascii')), sort_keys=True, indent= 2)


def inventory(token):

    return {
    "_meta": {
        "hostvars": {
            "huong": {
                "ansible_host": "10.208.182.77",
                "ansible_ssh_pass": token
            }
        }
    },
    "all": {
        "children": [
            "ungrouped"
        ]
    },
    "ungrouped": {
        "hosts": [
            "huong"
        ]
    }
}
def get_empty_vars():
    return json.dumps({})

if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser(
        description=__doc__,
        prog=__file__
    )
    mandatory_options = arg_parser.add_mutually_exclusive_group()
    mandatory_options.add_argument(
        '--list',
        action='store',
        nargs="*",
        default="dummy",
        help="Show entirely inventory"
    )
    mandatory_options.add_argument(
        '--host',
        action='store',
        help="Display vars related to the host"
    )

    try:
        args = arg_parser.parse_args()
        if args.host:
            print(get_empty_vars())
        elif len(args.list) >= 0:
            print(get_result())
        else:
            raise ValueError("Expecting either --host $HOSTNAME or --list")

    except ValueError:
        raise
