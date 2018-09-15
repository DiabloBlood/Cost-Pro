### 1. Lazy Connecting
"""
The Engine, when first returned by create_engine(), has not actually tried to connect to the database yet;
that happens only the first time it is asked to perform a task against the database.
"""
'''
$ sudo su
$ curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
Ubuntu Trusty:$ curl https://packages.microsoft.com/config/ubuntu/14.04/prod.list > /etc/apt/sources.list.d/mssql-release.list
Ubuntu Xenial:$ curl https://packages.microsoft.com/config/ubuntu/16.04/prod.list > /etc/apt/sources.list.d/mssql-release.list
Ubuntu Artful:$ curl https://packages.microsoft.com/config/ubuntu/17.10/prod.list > /etc/apt/sources.list.d/mssql-release.list
$ exit
$ sudo apt-get update
$ sudo ACCEPT_EULA=Y apt-get install msodbcsql
$ sudo apt-get install unixodbc-dev

⚠ If failed to install unixodbc-dev in Trusty via apt-get, build from source on your machine first,
then run the following command to set unixODBC default path in case environment variables
are set incorrectly.

$ export ODBCINI=/etc/odbc.ini
$ export ODBCSYSINI=/etc

Create odbc.ini file in /etc if doesn't have one

$ sudo touch /etc/odbc.ini

### very important!!!
$ sudo sudo apt-get install python3.6-dev
'''