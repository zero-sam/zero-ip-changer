# Zero IP Changer

A command-line tool to dynamically change your IP address using Tor.

## Features

- Change IP address at regular intervals.
- Fetch and display IP and location information.
- Uses TOR Routers for Enhanced Privacy

## Requirements

- **Python 3.7 or higher**
- **Tor** (should be installed on the system)
- **Requests library** for HTTP requests
- **Stem library** for interacting with Tor
- WORKS ONLY ON LINUX
- WINDOWS UPDATE WILL BE GIVEN IN COUPLE MONTHS OR EARLY 2025


## Installation

To install the required software and dependencies, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/zero-sam/zero-ip-changer.git
   cd zero-ip-changer




2.**Run the installation script:

```bash
chmod +x install.sh
sudo bash install.sh
```

Start Tor: Before running the application, ensure that the Tor service is running. You can start it using:

```
sudo systemctl start tor
```
Usage
```
 python cli.py (OR)
 sudo python cli.py
```


---

### Troubleshooting

### IF THE BELOW PROBLEM PRESISTS AFTER FOLLOWING THE STEPS BELOW FEEL FREE TO CONTACT ME VIA 
LINKEDIN: https://www.linkedin.com/in/samuel-e-050636269/
INSTAGRAM: https://www.instagram.com/__.sam.___07/

#### 1. **Tor Service Not Running**
   - Ensure the Tor service is running, as the IP changer relies on it. Start the Tor service with:
     ```bash
     sudo systemctl start tor
     ```
   - To check if Tor is active, run:
     ```bash
     sudo systemctl status tor
     ```
   - If the service is inactive or not found, try reinstalling Tor:
     ```bash
     sudo apt update
     sudo apt install tor
     ```

#### 2. **Permission Denied Error**
   - If you encounter a permission error while running `cli.py`, try running it with `sudo`:
     ```bash
     sudo python3 cli.py
     ```
   - Ensure that the Tor control port (`9051` by default) is accessible. Double-check your `/etc/tor/torrc` file to confirm it has:
     ```bash
     ControlPort 9051
     CookieAuthentication 1
     ```

#### 3. **Missing Packages**
   - If you see errors related to missing Python packages (e.g., `requests` or `stem`), activate the virtual environment and reinstall the dependencies:
     ```bash
     source ~/zero-ip-changer-env/bin/activate
     pip install -r requirements.txt
     ```
   - If you are using system-wide Python packages, you can install the dependencies manually:
     ```bash
     pip install requests stem
     ```

#### 4. **Tor Not Changing IPs**
   - The Tor network may sometimes reuse IPs, depending on availability. Ensure the interval between IP changes is at least 10 seconds, as Tor requires time to establish new circuits.
   - You can test if Tor is configured correctly by checking your IP manually:
     ```bash
     curl --socks5 127.0.0.1:9050 http://ipinfo.io/json
     ```
   - If the IP isn’t changing, restart the Tor service to reset connections:
     ```bash
     sudo service tor restart
     ```

#### 5. **Testing Network Connectivity**
   - Ensure your network allows connections to the Tor network. Some networks may restrict Tor usage. To check connectivity:
     ```bash
     curl http://ipinfo.io/json
     ```
   - If you don’t receive an IP, verify your internet connection.

#### 6. **General Debugging**
   - If errors persist, try running `cli.py` in verbose mode to capture error messages:
     ```bash
     python3 -m trace -t cli.py
     ```
   - Or check the Tor log for possible issues:
     ```bash
     tail -f /var/log/tor/log


```





![ipchanger](https://github.com/user-attachments/assets/fbadaa0c-32e5-49c0-b3fd-78897e386b1c)









