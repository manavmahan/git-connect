# git-connect
Module to clone git repository using SSH on ephermal machines.

- Install gitpython using PIP
- Copy the code to clone.py and make it executable
```console
pip3 install gitpython
curl https://raw.githubusercontent.com/manavmahan/git-connect/main/connect.py > connect.py
chmod u+x connect.py
```
- Run clone.py to clone repository. Replace {ACTION}, {GIT_USERNAME}, and {GIT_REPOSITORY} as required
```console
./connect.py {ACTION: clone[e], push [u], or pull[d]} {GIT_USERNAME} {GIT_REPOSITORY}
