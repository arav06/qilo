import os
import sys

banner = """

▒█▀▀█ ░▀░ █░░ █▀▀█ ▒█▀▀▀█ ▒█▀▀▀█ ▒█░▒█ 
▒█░▒█ ▀█▀ █░░ █░░█ ░▀▀▀▄▄ ░▀▀▀▄▄ ▒█▀▀█ 
░▀▀█▄ ▀▀▀ ▀▀▀ ▀▀▀▀ ▒█▄▄▄█ ▒█▄▄▄█ ▒█░▒█

"""
print(banner)
try:
    info = sys.argv[1]
except:
    print("python3 main.py FILE \nCreate a file containing the required information \n")
    print("In a txt file, add the IP, Port, Username and Password of the SSH server in this format")
    print("\nIP Port Username Password \n")
    print("Such as 192.168.13 22 admin password \nWhere the values are separated by ONLY 1 space")
	
    exit()
cmd = str(input("Command> "))
if cmd == "":
    print("Specify a command/module")
elif cmd =="ping":
    info = open(info,"r")
    f = info.read()
    lines = f.split("\n")
    print("\n")
    for line in lines:
        if line == "":
            continue
        else:
            words = line.split()
            ip = words[0]
            

            a = [str(os.system(f"ping {ip} -w 4"))]
            string = '' 
            for i in a:
                string += i   
            print(string)
    print("Thank you for using me :)")

    sys.exit()


else:
    info = open(info,"r")
    f = info.read()
    lines = f.split("\n")
    print("\n")
    for line in lines:
        if line == "":
            continue
        else:
            words = line.split()
            ip = words[0]
            port = words[1]
            user = words[2]
            passwd = words[3]
            

            print(f"[+]Details for {ip} \n")
            print(f"Port = {port}")
            print(f"Username = {user}")
            print(f"Password = {passwd}")
            print("\n")
    a = [str(os.system(cmd))]
    string = '' 
    for i in a:
        string += i   
    print(string)
    print("Thank you for using me :)")

    sys.exit()



