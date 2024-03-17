#! /usr/local/bin/python3
"""Module to clone git repository using SSH on ephermal machines."""

import os
from git import Repo

ID_FILE = "id_rsa"
REPO = "demo-gpt"
UNAME = "manavmahan"
KEY = os.environ['GIT_KEY']


if __name__ == "__main__":
    with open(ID_FILE, 'w') as f:
        f.write(KEY)
    os.chmod(ID_FILE, 0o400)

    git_ssh_cmd = "ssh -i %s" % ID_FILE
    Repo.clone_from(f"git@github.com:{UNAME}/{REPO}.git",
                    REPO,
                    env=dict(GIT_SSH_COMMAND=git_ssh_cmd))
