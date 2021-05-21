import os
import sys
# Paramiko SSH: https://www.kite.com/python/answers/how-to-ssh-using-paramiko-in-python
banner = """

▒█▀▀█ ░▀░ █░░ █▀▀█ ▒█▀▀▀█ ▒█▀▀▀█ ▒█░▒█ 
▒█░▒█ ▀█▀ █░░ █░░█ ░▀▀▀▄▄ ░▀▀▀▄▄ ▒█▀▀█ 
░▀▀█▄ ▀▀▀ ▀▀▀ ▀▀▀▀ ▒█▄▄▄█ ▒█▄▄▄█ ▒█░▒█

"""
print(banner)
try:
    info = sys.argv[1]
except:
    print("python3 main.py FILE")
    exit()
cmd = str(input("Command> "))
if cmd == "":
    print("Type a command")
else:
    info = open(info,"r")
    f = info.read()
    lines = f.split("\n")
    print("\n")
    for line in lines:
        if line == "":
            pass
        else:
            words = line.split()
            ip = words[0]
            port = words[1]
            user = words[2]
            passwd = words[3]

            print(f"Details for {ip} \n")
            print(f"Port = {port}")
            print(f"Username = {user}")
            print(f"Password = {passwd}")
            print("\n")
    a = os.system(cmd)
    print(str(a))
    print("Thank you for using me :)")

    exit()
    