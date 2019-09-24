#!/usr/bin/python3

import os
import subprocess
from subprocess import PIPE

os.chdir("/var/log")


def messages():
    with open('/home/ken/myscripts/python-scripts/systemd_filtered.txt', 'w') as results:
        log_messages = subprocess.run("ls -al | cat messages | grep systemd", stdout=results, shell=True)
    return log_messages


messages()
