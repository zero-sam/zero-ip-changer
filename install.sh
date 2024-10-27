#!/bin/bash

# Update package lists
echo "Updating package lists..."
sudo apt update

# Install Tor and Python3
echo "Installing Tor and Python3..."
sudo apt install -y tor python3 python3-pip

# Install virtualenv if not already installed
echo "Installing virtualenv..."
sudo pip3 install virtualenv --break-system-packages

# Create a virtual environment
echo "Creating virtual environment..."
python3 -m venv ~/zero-ip-changer-env

# Activate the virtual environment
echo "Activating the virtual environment..."
source ~/zero-ip-changer-env/bin/activate

# Install required Python libraries within the virtual environment
echo "Installing required Python libraries..."
pip install -r requirements.txt --break-system-packages

# Configure Tor Control Port
echo "Configuring Tor to allow control port access..."
sudo bash -c 'echo -e "\nControlPort 9051\nCookieAuthentication 1\nCookieAuthFile /run/tor/control.authcookie" >> /etc/tor/torrc'

# Restart Tor service
echo "Restarting Tor service..."
sudo service tor restart 

# Add user to debian-tor group
echo "Adding user to debian-tor group..."
sudo usermod -aG debian-tor $(whoami)

# Change permissions for the script file
echo "Changing permissions for the script file..."
sudo chown $(whoami):$(whoami) /home/kali/zero-ip-changer/cli.py
sudo chmod 755 /home/kali/zero-ip-changer/cli.py

echo "Installation complete!"
