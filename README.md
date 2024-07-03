# بسم الله الرحمن الرحيم


# Network_Automation_Python
These scripts provide a simple network automation asynchronous framework for vendor-agnostic network


**File Structure:**

1. **BackupSwitchsConfig.py**
    * **Function Description:** Backs up the running configuration of multiple switches using telnet. 
    * **Input:** 
        * `username`: A text file containing the username for telnet access.
        * `password`: A text file containing the password for telnet access.
        * `MySwitchs`: A text file containing a list of switch IP addresses, one per line.
    * **Output:** 
        * `switch IP`:  A separate text file created for each switch, containing the backed-up configuration.

2. **clearS.py**
    * **Function Description:** Removes all VLANs from 2 to 50 on multiple switches using telnet.
    * **Input:** 
        * `username`: A text file containing the username for telnet access.
        * `password`: A text file containing the password for telnet access.
        * `MySwitchs`: A text file containing a list of switch IP addresses, one per line.
    * **Output:**  
        * Outputs the command results from the telnet sessions to the console.

3. **confSwitchs.py**
    * **Function Description:** Creates VLANs from 2 to 5 on multiple switches using telnet.
    * **Input:** 
        * `username`: A text file containing the username for telnet access.
        * `password`: A text file containing the password for telnet access.
        * `MySwitchs`: A text file containing a list of switch IP addresses, one per line.
    * **Output:**  
        * Outputs the command results from the telnet sessions to the console.

4. **fw_conf.py**
    * **Function Description:**  Creates VLANs from 2 to 50 on multiple switches using telnet. Utilizes functions defined in `TelNetSwitchs.py`. 
    * **Input:** 
        * `username`: A text file containing the username for telnet access.
        * `password`: A text file containing the password for telnet access.
        * `MySwitchs`: A text file containing a list of switch IP addresses, one per line.
    * **Output:**  
        * Outputs the command results from the telnet sessions to the console.

5. **fw_Rmv.py**
    * **Function Description:** Removes VLANs from 2 to 50 on multiple switches using telnet. Utilizes functions defined in `TelNetSwitchs.py`. 
    * **Input:** 
        * `username`: A text file containing the username for telnet access.
        * `password`: A text file containing the password for telnet access.
        * `MySwitchs`: A text file containing a list of switch IP addresses, one per line.
    * **Output:**  
        * Outputs the command results from the telnet sessions to the console.

6. **FW_th_rmv.py**
    * **Function Description:** Removes VLANs from 2 to 50 on multiple switches using telnet and threading. Utilizes functions defined in `TelNetSwitchs.py`.
    * **Input:** 
        * `username`: A text file containing the username for telnet access.
        * `password`: A text file containing the password for telnet access.
        * `MySwitchs`: A text file containing a list of switch IP addresses, one per line.
    * **Output:**  
        * Outputs the command results from the telnet sessions to the console.

7. **importTelent.py**
    * **Function Description:** Connects to a Cisco IOS device via telnet and performs basic configuration.
    * **Input:** 
        * Username and password entered interactively.
    * **Output:**  
        * Outputs the command results from the telnet sessions to the console.

8. **mclearS.py**
    * **Function Description:** Removes VLANs from 2 to 50 on multiple switches using telnet. Utilizes functions defined in `TelNetSwitchs.py`. 
    * **Input:** 
        * `username`: A text file containing the username for telnet access.
        * `password`: A text file containing the password for telnet access.
        * `MySwitchs`: A text file containing a list of switch IP addresses, one per line.
    * **Output:**  
        * Outputs the command results from the telnet sessions to the console.

9. **mconfs.py**
    * **Function Description:** Creates VLANs from 2 to 50 on multiple switches using telnet. Utilizes functions defined in `TelNetSwitchs.py`.
    * **Input:** 
        * `username`: A text file containing the username for telnet access.
        * `password`: A text file containing the password for telnet access.
        * `MySwitchs`: A text file containing a list of switch IP addresses, one per line.
    * **Output:**  
        * Outputs the command results from the telnet sessions to the console.

10. **netmiko1.py**
    * **Function Description:**  Connects to a Cisco IOS device using Netmiko library and performs basic configuration and VLAN creation. 
    * **Input:** 
        * Hardcoded device credentials.
    * **Output:**  
        * Outputs the command results from the Netmiko sessions to the console.

11. **Netmiko2.py**
    * **Function Description:** Connects to a Cisco IOS device using Netmiko library and performs basic configuration and VLAN creation. 
    * **Input:** 
        * Hardcoded device credentials.
    * **Output:**  
        * Outputs the command results from the Netmiko sessions to the console.

12. **scon.py**
    * **Function Description:** Connects to a Cisco IOS device via telnet and creates VLANs. 
    * **Input:** 
        * Username and password entered interactively.
    * **Output:**  
        * Outputs the command results from the telnet sessions to the console.

13. **scons.py**
    * **Function Description:** Connects to multiple Cisco IOS devices via telnet and creates VLANs.
    * **Input:** 
        * `username`: A text file containing the username for telnet access.
        * `password`: A text file containing the password for telnet access.
        * `MySwitchs`: A text file containing a list of switch IP addresses, one per line.
    * **Output:**  
        * Outputs the command results from the telnet sessions to the console.

14. **telnet switch config.py**
    * **Function Description:**  Backs up the running configuration of multiple switches using telnet. 
    * **Input:** 
        * `username`: A text file containing the username for telnet access.
        * `password`: A text file containing the password for telnet access.
        * `MySwitchs`: A text file containing a list of switch IP addresses, one per line.
    * **Output:** 
        * `switch IP`:  A separate text file created for each switch, containing the backed-up configuration.

15. **TelNetSwitchs.py**
    * **Function Description:** A library file containing functions for telnet connectivity, VLAN creation, and VLAN removal.
    * **Input:**  
        * None (functions take arguments for username, password, IP, and VLAN range).
    * **Output:**  
        * Functions perform actions on connected devices.

16. **testdef.py**
    * **Function Description:** Simple example demonstrating function calls and timing with the `time` module. 
    * **Input:**  
        * None
    * **Output:**  
        * Prints outputs from function calls.

17. **threadingexample.py**
    * **Function Description:** Demonstrates basic threading in Python, creating multiple threads that execute a simple function.
    * **Input:**  
        * None
    * **Output:**  
        * Prints outputs from threads.


