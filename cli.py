import time
import requests
from stem import Signal
from stem.control import Controller
import argparse

# Constants
TOR_SOCKS_PORT = 9050
TOR_CONTROL_PORT = 9051
IP_CHECK_URL = "http://ipinfo.io/json"

def get_ip_info():
    """Get IP address details and location."""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'
    }
    proxies = {
        'http': f'socks5h://127.0.0.1:{TOR_SOCKS_PORT}',
        'https': f'socks5h://127.0.0.1:{TOR_SOCKS_PORT}',
    }
    try:
        response = requests.get(IP_CHECK_URL, headers=headers, proxies=proxies)
        response.raise_for_status()
        data = response.json()
        return f"IP: {data['ip']}, Location: {data['city']}, {data['region']} - {data['country']}"
    except requests.RequestException as e:
        return f"Error fetching IP info: {e}"

def change_ip():
    """Request a new IP from Tor."""
    try:
        with Controller.from_port(port=TOR_CONTROL_PORT) as controller:
            controller.authenticate()
            controller.signal(Signal.NEWNYM)
            time.sleep(10)  # Allow time for Tor to establish the new circuit
    except Exception as e:
        print(f"Error changing IP: {e}")

def run_ip_changer(interval):
    """Dynamically change IP every 'interval' seconds."""
    try:
        while True:
            print("\nZero is changing your IP...")
            change_ip()
            print(f"NEW IP INFO: {get_ip_info()}")
            print(f"Next change in {interval} seconds...\n")
            time.sleep(interval)
    except KeyboardInterrupt:
        print("\nZERO IP CHANGER STOPPED.")

def menu():
    """Display the menu."""
    while True:
        print("\n=== ZERO IP CHANGER ===")
        print("1. RUN IP CHANGER")
        print("2. QUIT")
        choice = input("Choose an option: ")

        if choice == "1":
            try:
                interval = int(input("Enter the seconds between IP changes (5-60): "))
                if 5 <= interval <= 60:
                    run_ip_changer(interval)
                else:
                    print("Please enter a value between 5 and 60.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == "2":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()
