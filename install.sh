#!/bin/bash

echo "Updating package lists..."
sudo apt update

echo "Installing Tor and Python3..."
sudo apt install -y tor python3 python3-pip --break-system-packages

echo "Installing required Python libraries..."
sudo pip3 install -r requirements.txt --break-system-packages

echo "Configuring Tor to allow control port access..."
sudo bash -c 'echo -e "\nControlPort 9051\nCookieAuthentication 1\nCookieAuthFile /run/tor/control.authcookie" >> /etc/tor/torrc'

echo "Restarting Tor service..."
sudo service tor restart 

echo "Installation complete!"
