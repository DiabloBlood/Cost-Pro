## Env Setup
### Update Python3.5 to Python3.6
```bash
$ sudo add-apt-repository ppa:deadsnakes/ppa
$ sudo apt-get update
$ sudo apt-get install python3.6

$ wget https://bootstrap.pypa.io/get-pip.py
$ python3.6 get-pip.py
$ pip3 install virtualenv
$ virtualenv env --always-copy

$ rm get-pip.py
```
