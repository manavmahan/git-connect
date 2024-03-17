#! /usr/local/bin/python3
"""Module to clone git repository using SSH on ephermal machines."""

import os
import sys
from git import Repo

ID_FILE = "id_rsa"

def get_input(arg_index):
    if sys.argv[arg_index]:
        return sys.argv[arg_index]
    return input(f"Enter {key}")

UNAME = get_input(1, "Enter GitHub Username:\t")
REPO = get_input(2, "Enter Repository Name:\t")

KEY = os.environ['GIT_KEY']
if KEY is None:
    KEY = input(f"Enter SSH Key to connect to GitHub\n")

if __name__ == "__main__":
    with open(ID_FILE, 'w') as f:
        f.write(KEY)
    os.chmod(ID_FILE, 0o400)

    git_ssh_cmd = "ssh -i %s" % ID_FILE
    Repo.clone_from(f"git@github.com:{UNAME}/{REPO}.git",
                    REPO,
                    env=dict(GIT_SSH_COMMAND=git_ssh_cmd))
