#!/bin/bash

echo "Updating package lists..."
sudo apt update

echo "Installing Tor and Python3..."
sudo apt install -y tor python3 python3-pip

echo "Installing required Python libraries..."
pip3 install -r requirements.txt

echo "Configuring Tor to allow control port access..."
sudo bash -c 'echo -e "\nControlPort 9051\nCookieAuthentication 1" >> /etc/tor/torrc'

echo "Restarting Tor service..."
sudo service tor restart

echo "Installation complete!"
