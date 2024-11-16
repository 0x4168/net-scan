import socket
import requests
import random
from colorama import Fore as color
import save
import ftplib
import paramiko

class Scan():
    def __init__(self,ip=None,file=None):
        self.results = []
        self.ports = [
    4444, 1234, 31337, 9999, 6666, 6669, 1337, 9005, 9001, 8443, 2222, 1111, 5555, 
    4001, 8001, 8000, 1233, 1212, 12345, 3333, 4444, 7777, 8888, 9090, 8081, 6663, 
    5050, 2020, 2025, 2024, 1010, 3030, 2030, 4040, 6060, 7070, 9090, 1717, 1718, 
    2323, 2525, 3133, 3434, 4440, 5550, 6565, 6767, 7878, 8989, 9191, 9292, 9393, 
    9494, 9595, 9696, 9797, 9898, 1338, 1339, 1500, 1600, 1700, 1800, 1900, 1911, 
    2000, 2121, 2324, 2424, 2524, 2626, 2727, 2828, 2929, 3435, 3535, 3636, 3737, 
    3838, 3939, 4545, 4646, 4747, 4848, 4949, 5454, 5757, 5858, 5959, 6061, 6161, 
    6262, 6363, 6464, 6566, 6768, 6868, 6969, 7171, 7272, 7373, 7474, 7575, 7676, 
    7879, 7979, 8088, 8181, 8282, 8383, 8484, 8585, 8686, 8787, 8988, 9192, 9293, 
    9394, 9495, 9596, 9697, 9798, 9899, 9990, 10000, 11000, 12000, 13000, 14000, 
    15000, 16000, 17000, 18000, 19000, 20000, 21000, 22000, 23000, 24000, 25000, 
    26000, 27000, 28000, 29000, 30000, 31000, 32000, 33000, 34000, 35000, 36000, 
    37000, 38000, 39000, 40000, 41000, 42000, 43000, 44000, 45000, 46000, 47000, 
    48000, 49000, 50000, 51000, 52000, 53000, 54000, 55000, 56000, 57000, 58000, 
    59000, 60000, 61000, 62000, 63000, 64000, 65000
]
        self.default_passwords = {
    "ftp": [("admin", "admin"), ("anonymous", ""), ("root", "1234")],
    "smb": [("guest", ""), ("admin", "password"), ("user", "1234")],
    "mysql": [("root", ""), ("root", "root"), ("admin", "admin")],
    "ssh": [("root", ""), ("root", "root"), ("admin", "admin"), ("admin", ""), ("admin", "1234"), ("root", "1234")],
}
        self.results.clear()
        if file :
            for ip in open(file,"r").read().splitlines():
                self.scan_network(ip)
                print(f"\n{color.GREEN}[{color.WHITE}+{color.GREEN}]{color.WHITE}Next IP")
        self.scan_network(ip)
        

    def check_ssh_no_password(self,host, port=22):
        for username, password in self.default_passwords["ssh"]:
            try:
                client = paramiko.SSHClient()
                client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                client.connect(host, port=port, username=username, password=password, timeout=5)
                print(f"{color.RED}[{color.WHITE}+{color.RED}]{color.WHITE}  SSH login without password possible for user: {username}")
                self.results.append({"Default : True","Username : ",username,"Password : ",password})
                client.close()
                return True
            except paramiko.AuthenticationException:
                pass
            except Exception as e:
                print(f"[-] Error: {e}")
        print(f"{color.GREEN}[{color.WHITE}+{color.GREEN}]{color.WHITE}  No SSH login without password found.")
        return False

    def check_ftp_default(self,host, port=21):
        for username, password in self.default_passwords["ftp"]:
            try:
                ftp = ftplib.FTP()
                ftp.connect(host, port, timeout=5)
                ftp.login(username, password)
                print(f"{color.RED}[{color.WHITE}+{color.RED}]{color.WHITE} Default FTP login found: {username}:{password}")
                ftp.quit()
                return True
            except Exception as e:
                pass
        print(f"{color.GREEN}[{color.WHITE}+{color.GREEN}]{color.WHITE} No default FTP credentials found.")
        return False
#   -_-_-_-_-_-_--_-_-_-_-_-_--_-_-_-_-_-_--_-_-_-_-_-_--_-_-_-_-_-_--_-_-_-_-_-_--_-_-_-_-_-_--_-_-_-_-_-_--_-_-_-_-_-_-
    def get_banner(self, ip, port):
        try:
            s = socket.socket()
            s.settimeout(1)
            s.connect((ip, port))
            if port == 80:
                s.send(b"HEAD / HTTP/1.1\r\nHost: " + ip.encode() + b"\r\n\r\n")
            elif port == 21:
                s.send(b"HELP\r\n")
            banner = s.recv(1024).decode()
            s.close()
            return banner.strip()
        except:
            return None



#   -_-_-_-_-_-_--_-_-_-_-_-_--_-_-_-_-_-_--_-_-_-_-_-_--_-_-_-_-_-_--_-_-_-_-_-_--_-_-_-_-_-_--_-_-_-_-_-_--_-_-_-_-_-_-
    def search_nvd(self, keyword, port, ip):
        api_key = '50c51db8-3720-40c8-9941-61d9979f95ec'
        url = f'https://services.nvd.nist.gov/rest/json/cves/2.0?keywordSearch={keyword}'
        headers = {'apiKey': api_key, 'User-Agent': 'Mozilla/5.0'}
        prinT = [f"{color.YELLOW}[{color.WHITE}+{color.YELLOW}]{color.WHITE} I'm searching for vulnerabilities ..• ",
                 f"{color.YELLOW}[{color.WHITE}+{color.YELLOW}]{color.WHITE} I'm searching for vulnerabilities .•. ",
                 f"{color.YELLOW}[{color.WHITE}+{color.YELLOW}]{color.WHITE} I'm searching for vulnerabilities •.. "]
        print("\t↳" + random.choice(prinT))
        try:
            response = requests.get(url, headers=headers,timeout=5)
            if response.status_code == 200:
                data = response.json()
                if data["vulnerabilities"] != []:
                    print(f"\t\t{color.RED}[{color.WHITE}+{color.RED}]{color.WHITE} Found a vulnerabilitie ")
                    loop = 0
                    for item in data.get('vulnerabilities', []):
                        cve_id = item['cve']['id']
                        description = item['cve']['descriptions'][0]['value']
                        severity = item.get('cve', {}).get('metrics', {}).get('cvssMetricV2', [{}])[0].get('baseSeverity', 'N/A')
                        print(f"\n\t\t\t•{color.YELLOW}[{color.WHITE}+{color.YELLOW}]{color.WHITE} CVE ID : {cve_id} \n\t\t\t•{color.YELLOW}[{color.WHITE}+{color.YELLOW}]{color.WHITE} Description: {description} \n\t\t\t•{color.YELLOW}[{color.WHITE}+{color.YELLOW}] {color.WHITE}Severity: {severity}")
                        self.results.append({"IP": ip, "Port": port, "CVE ID": cve_id, "Description": description, "Severity": severity})
                        loop += 1
                        if loop == 7:
                            print(f"\n\t\t\t•{color.RED}[{color.WHITE}+{color.RED}]{color.WHITE} I found {len(data.get('vulnerabilities', []))} Exploits in port : {port} ")
                            break
                else:
                    print(f"\t\t↳{color.GREEN}[{color.WHITE}+{color.GREEN}]{color.WHITE} port {color.YELLOW}{port}{color.WHITE} is safe :)\n")
            else:
                print(f"{color.RED}[{color.WHITE}+{color.RED}]{color.WHITE}Error accessing NVD API")
        except Exception as e:
            print(f"{color.RED}[{color.WHITE}+{color.RED}]{color.WHITE}Error connecting to NVD API:", e)
        print("\n")


#   -_-_-_-_-_-_--_-_-_-_-_-_--_-_-_-_-_-_--_-_-_-_-_-_--_-_-_-_-_-_--_-_-_-_-_-_--_-_-_-_-_-_--_-_-_-_-_-_--_-_-_-_-_-_-
    def check_ports(self, ip):
        for port in range(0,65536):
            banner = self.get_banner(ip, port)
            if banner:
                print(f"{color.YELLOW}[{color.WHITE}+{color.YELLOW}]{color.WHITE} Port {port} is open ••• ")
                if int(port) in self.ports:
                    print(f"\t↳{color.RED}[{color.WHITE}+{color.RED}]{color.WHITE} Warning: Unusual port detected - {port}")
                banner = banner.lower()
                if port == 80:
                    if "server:" in banner:
                        server_info = banner.split("server: ")[1]
                        version = server_info.split("\n")[0]
                elif port == 21:
                    version1 = banner.split(" (")[1]
                    version = version1.split(")")[0]
                elif port == 22:
                    version = banner.split(" ")[0]
                else: 
                    version = banner
                print(f"\t↳{color.GREEN}[{color.WHITE}+{color.GREEN}]{color.WHITE} Version: " + version)
                if version:
                    self.search_nvd(version, port, ip)
            else:
                prinT = [f"{color.GREEN}[{color.WHITE}+{color.GREEN}]{color.WHITE} I'm still searching - port {port} ..• ",
                         f"{color.GREEN}[{color.WHITE}+{color.GREEN}]{color.WHITE} I'm still searching - port {port} .•.",
                         f"{color.GREEN}[{color.WHITE}+{color.GREEN}]{color.WHITE} I'm still searching - port {port} •.."]
                print(random.choice(prinT))


#   -_-_-_-_-_-_--_-_-_-_-_-_--_-_-_-_-_-_--_-_-_-_-_-_--_-_-_-_-_-_--_-_-_-_-_-_--_-_-_-_-_-_--_-_-_-_-_-_--_-_-_-_-_-_-
    def scan_network(self,ip):
        print(f"{color.GREEN}[{color.WHITE}+{color.GREEN}]{color.WHITE} Scanning device with IP: {ip}")
        self.check_ports(ip)
        save.save_results_csv(self.results)
        save.save_results_json(self.results)
        save.save_results_html(self.results)



        

