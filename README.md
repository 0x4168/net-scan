 # NeScan 
 NetSca is an advanced Python-based network scanning and default credential testing tool. It is designed to provide comprehensive insights into the security of networks by scanning open ports, identifying services, and testing for weak or default configurations. With its ability to save results in multiple formats, it is an essential tool for penetration testers, system administrators, and cybersecurity enthusiasts.
---
## Features
1. Comprehensive Port Scanning:
    - Scans all ports (1-65535) to detect open ports on the target.
    - Provides detailed information about services running on the detected ports.
 
 2. Host Scanning Options:
    - Single Host: Specify a single IP address or hostname for scanning.
    - Multiple Hosts: Provide a file containing a list of IP addresses to scan multiple systems.
 
 3. Default Credential Testing:
    - Attempts to login with common default credentials for:
      - FTP
      - SSH
      - SMB/Samba
      - MySQL
    - Detects weak SSH configurations, such as login without a password.
 
 4. Output Formats:
    - Generates results in the following formats:
      - CSV: Ideal for further analysis in spreadsheets.
      - JSON: Machine-readable format for integration into other tools or scripts.
      - HTML: Well-formatted, human-readable report.
 
 5. Lightweight and Flexible:
    - No external tools like Nmap are required.
    - Purely Python-based, making it lightweight and platform-independent.
 
 ---
 
 ## Installation
 
 1. Clone the repository:
   
    git clone https://github.com/0x4168/net-scan.git
    
 
 2. Navigate to the project directory:
   
    cd net-scan
    
 
 3. Install the required Python libraries:
   
    pip install -r requirements.txt
    
 
 ---
 
 ## Usage
 
 Run the tool using Python and provide the necessary arguments.
 
 ### Command-line Options
 | Option              | Description                                     | Example                        |
 |---------------------|-------------------------------------------------|--------------------------------|
 | -ho / --host    | Scan a single host (IP or hostname).            | python main.py -ho 192.168.1.1 |
 | -f / --file     | Scan multiple hosts listed in a file.           | python main.py -f targets.txt |
 
 ---
 
 ### Examples
 
 #### Scanning a Single Host

 python main.py -ho 192.168.1.100
 
 - Scans all ports on the specified host.
 - Detects services and tests for default credentials.
 
 #### Scanning Multiple Hosts

 python main.py -f targets.txt
 
 - Scans all IPs listed in the targets.txt file.
 - Outputs results for each host in the specified formats.
 
 ---
 
 ## Default Credential Testing
 
 The tool includes built-in default credentials for services like FTP, SSH, SMB, and MySQL. It automatically tests these credentials to identify weak configurations and outputs the results.
 
 #### Example Credentials Tested:
 - FTP:
   - guest:guest
   - anonymous:<empty>
 - SSH:
   - root:root
   - admin:admin
 - SMB/Samba:
   - guest:<empty>
   - admin:password
 - MySQL:
   - root:<empty>
   - root:root
 
 ---
 
 ## Output
 
 After scanning, the tool saves results in the following formats:
 1. CSV: A structured file containing detailed information about each host.
 2. JSON: A machine-readable file suitable for automation and integration.
 3. HTML: A human-readable report for quick analysis.
 
 The files are saved in the output directory by default.
 
 ---
 
 ## Use Cases
 - Identify open ports and running services in a network.
 - Test for weak default credentials across multiple services.
 - Generate reports for security assessments or penetration testing.
 - Automate network security scanning tasks.
 
 ---
 
 ## Planned Enhancements
 - Integration with CVE databases for vulnerability mapping.
 - Support for additional protocols and authentication mechanisms.
 - Subdomain enumeration for web application security testing.
 
 ---
 
 ## Contributions- 
 Contributions are welcome! If you have ideas for new features or improvements, feel free to open an issue.
 
 ---
 
 ## License
 This project is licensed under the MIT License. See the LICENSE file for more details.
 
 ---
 
 ## Contact
 - GitHub: [YourUsername](https://github.com/0x4168)
 - Telegram: [ZeroXyaser](https://t.me/ZeroXyaser)
