import paramiko
host = "test.rebex.net"
port = 22
username = "demo"
password = "password"

command = "ls"

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host, port, username, password)

stdin, stdout, stderr = ssh.exec_command(command)
lines = stdout.readlines()

string = '' 
for i in lines:
    string += i   
print(string)
