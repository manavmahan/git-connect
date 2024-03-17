#! /usr/local/bin/python3
"""Module to clone git repository using SSH on ephermal machines."""

import os
import sys
from git import Repo

ID_FILE = "key"


def get_input(arg_index, key):
    if len(sys.argv) > arg_index and sys.argv[arg_index]:
        return sys.argv[arg_index]
    return input(f"Enter {key}")


ACTION = get_input(1, "Choose action from:\tclone[c], push[u], pull[d]...")
if len(ACTION)==1:
    if ACTION=='c':
        ACTION = "clone"
    elif ACTION=='u':
        ACTION = "push"
    elif ACTION=='d':
        ACTION = "pull"

assert (ACTION in ('clone', 'push', 'pull')), "Only clone, push, and pull actions are supported."

UNAME = get_input(2, "Enter GitHub Username:\t")
REPO = get_input(3, "Enter Repository Name:\t")

KEY = os.environ.get('GIT_KEY')
if KEY is None:
    KEY = ""
    print("Paste SSH Key to connect to GitHub...")
    while True:
        line = input()
        KEY += line + "\n"
        if not line:
            break

if __name__ == "__main__":
    with open(ID_FILE, 'w') as f:
        f.write(KEY)
    os.chmod(ID_FILE, 0o400)

    git_ssh_cmd = "ssh -i %s" % ID_FILE

    if ACTION == "clone":
        Repo.clone_from(f"git@github.com:{UNAME}/{REPO}.git",
                        REPO,
                        env=dict(GIT_SSH_COMMAND=git_ssh_cmd))
    elif ACTION == "push":
        r = Repo(REPO)
        origin = r.remote(name='origin')
        origin.push(env=dict(GIT_SSH_COMMAND=git_ssh_cmd))
    elif ACTION == "pull":
        r = Repo(REPO)
        origin = r.remote(name='origin')
        origin.pull(env=dict(GIT_SSH_COMMAND=git_ssh_cmd))
