# Importing Modules
import os
import sys
import paramiko
import getpass as gp
import random
import string
# Printing Banner

banner = """

▒█▀▀█ ░▀░ █░░ █▀▀█ ▒█▀▀▀█ ▒█▀▀▀█ ▒█░▒█ 
▒█░▒█ ▀█▀ █░░ █░░█ ░▀▀▀▄▄ ░▀▀▀▄▄ ▒█▀▀█ 
░▀▀█▄ ▀▀▀ ▀▀▀ ▀▀▀▀ ▒█▄▄▄█ ▒█▄▄▄█ ▒█░▒█

"""

print(banner)
print("\nWelcome to Qilo SSH, type 'qhelp' to display the help menu :) \n")

# Checking if the information file has been specified

try:
    info = sys.argv[1]
except:
    print("python3 Qilo.py FILE \nCreate a file containing the required information \n")
    print("In a txt file, add the IP, Port, Username and Password of the SSH server in this format")
    print("\nIP Port Username Password \n")
    print("Such as '192.168.13 22 admin password' \nWhere the values are separated by ONLY 1 space")
	
    exit()

# Creating the user's prompt
username = gp.getuser()
id = ''.join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase, k=5))
while True:
    cmd = str(input(f"{username}@qilo-{id}$ "))
    print("\n")

    # Checking if a command/module has been specified
    if cmd == "":
        print("Specify a command/module,type 'qhelp' to display the help menu\n")
        continue

    # Pings the IPs in the list
    elif cmd =="qping":
        info2 = open(info,"r")
        f = info2.read()
        lines = f.split("\n")
        print("\n")
        for line in lines:
            if line == "":
                continue
            else:
                words = line.split()
                ip = words[0]
                
                print(f"[+]Results for {ip}")
                a = [str(os.system(f"ping {ip} -w 4"))]
                string = '' 
                for i in a:
                    string += i   
                print(string)
        continue

    # Exits the program
    elif cmd == "exit" or cmd == "quit":
        print("[+]Bye :)\n")

        break
        exit()

    # Clears the user's terminal 
    elif cmd == "qclear":
        name = os.name
        if name == "nt":
            os.system("cls")
        elif name == "posix":
            os.system("clear")
        else:
            print("OS not supported :(")
        continue

    # Prints the help menu 
    elif cmd == "qhelp":
        print("Welcome to Qilo SSH, an SSH client that lets you control multiple Windows/Linux Servers at once :) \n")
        print("Developed by Arav Budhiraja(https://github.com/arav06) in 2021 \n")
        print("\nType any command/module in the prompt to control your servers \n")
        print("Modules: \n")
        print("* Qping: Pings IPs specified in the list by typing 'qping' in the input \n")
        print("* Qclear: Clears your terminal by typing 'qclear' \n")
        print("* Qhelp: Displays the help menu by typing 'qhelp' \n")
        print("* QSys: Displays the System Information for all hosts by typing 'qsys' \n")
        continue
    
    # Prints System Information for all hosts
    elif cmd == "qsys":
        info2 = open(info,"r")
        f = info2.read()
        lines = f.split("\n")
        
        for line in lines:
            if line == "":
                continue
            else:
                words = line.split()
                ip = words[0]
                port = words[1]
                user = words[2]
                passwd = words[3]
                ssh = paramiko.SSHClient()
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                ssh.connect(ip, port, user, passwd)
                command = "wmic os get Status, Caption, BuildNumber, OSArchitecture & uname -a"
                stdin, stdout, stderr = ssh.exec_command(command)
                output = stdout.readlines()
                output2 = stderr.readlines()
                string = '' 
                string2 = ''
                for i in output:
                    string += i 
                for j in output2:
                    string2 += j  
                print("\n") 
                print(f"[+]Results from {ip}\n")
                print(string)
                print(string2)
        continue

     # Executing commands on the servers
    else:
        info2 = open(info,"r")
        f = info2.read()
        lines = f.split("\n")
        for line in lines:
            if line == "":
                continue
            else:
                words = line.split()
                ip = words[0]
                port = words[1]
                user = words[2]
                passwd = words[3]
                ssh = paramiko.SSHClient()
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                ssh.connect(ip, port, user, passwd)
                stdin, stdout, stderr = ssh.exec_command(cmd)
                output = stdout.readlines()
                output2 = stderr.readlines()
                string = '' 
                string2 = '' 
                for i in output:
                    string += i   
                for j in output2:
                    string2 += j
                print(f"[+]Results from {ip} \n")
                print(string)
                print(string2)
                print("\n")
        continue
