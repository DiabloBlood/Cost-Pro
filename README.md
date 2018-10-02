# python3.5 update to python3.6
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt-get update
sudo apt-get install python3.6

wget https://bootstrap.pypa.io/get-pip.py
python3.6 get-pip.py
pip3 install virtualenv
virtualenv env --always-copy
