# Network_Automation_Python
These scripts provide a simple network automation asynchronous framework for vendor-agnostic network

## BackupSwitchsConfig.py
### Script Description
Backup Network Switch Configurations

This Python script automates the process of backing up the configurations of multiple network switches using Telnet. The script reads the list of switch IP addresses from a file and logs into each switch using credentials stored in separate files. It then collects the running configuration of each switch and saves it to a file.

### Key Features:
Automated Backup: Automates the login and configuration retrieval process for multiple switches.
Credential Management: Reads the username and password from separate files for secure credential management.
Configuration Storage: Saves the configuration of each switch to a file named after the switch's IP address.
Telnet Connection: Utilizes Telnet for remote connection and command execution.
### Steps:
Read Credentials: Reads the username and password from username and password files, respectively.
Read IP Addresses: Reads the list of switch IP addresses from MySwitchs file.
Telnet Connection: Connects to each switch via Telnet.
Login: Logs into the switch using the provided credentials.
Retrieve Configuration: Enters privileged mode and retrieves the running configuration.
Save Configuration: Saves the retrieved configuration to a file named after the switch's IP address.
### Usage:
Ensure you have the username and password files containing the respective credentials.
Create a file named MySwitchs with a list of IP addresses of the switches you want to backup.
Run the script.
### Example Files:
username: Contains the username for the switches.
password: Contains the password for the switches.
MySwitchs: Contains the IP addresses of the switches, one per line.
### Example Output:
switch_192.168.1.1: Contains the configuration of the switch with IP 192.168.1.1.
