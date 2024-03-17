# git-connect
Module to clone git repository using SSH on ephermal machines.

- Install gitpython using PIP
- Copy the code to clone.py and make it executable
```console
pip3 install gitpython
curl https://raw.githubusercontent.com/manavmahan/git-connect/main/clone.py > clone.py
chmod u+x clone.py
```
- Run clone.py to clone repository. Replace GIT_USERNAME and GIT_REPOSITORY as required
```console
./clone.py {GIT_USERNAME} {GIT_REPOSITORY}
