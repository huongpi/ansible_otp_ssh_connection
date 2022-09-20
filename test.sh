#!/bin/bash

gnome-terminal --tab --command="bash -c 'cd /etc; ls; $(source start_vault.sh; echo $%s)'"
