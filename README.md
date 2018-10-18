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
### Install ODBC driver
```bash
$ sudo apt-get install python3.6-dev (Very Important!)
$ sudo su
$ curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
$ curl https://packages.microsoft.com/config/ubuntu/16.04/prod.list > /etc/apt/sources.list.d/mssql-release.list
$ exit
$ sudo apt-get update
$ sudo ACCEPT_EULA=Y apt-get install msodbcsql
$ sudo apt-get install unixodbc-dev
$ export ODBCINI=/etc/odbc.ini
$ export ODBCSYSINI=/etc
$ sudo touch /etc/odbc.ini (Create odbc.ini file in /etc if doesn't have one)
```