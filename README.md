# <b>Qilo SSH v1.0</b>

## Control multiple Linux/Windows servers at once

### How to use
* Download the github repository

* In the same directory as the Qilo.py file, create a txt file such as info.txt

* In info.txt, follow this format to specify the required information
```
192.168.1.13 22 user pass
```
Where '192.168.1.13' is the IP of the server, '22' is the port on which SSH is running, 'user' is the username and 'pass' is the username's password
<br>
You can add more IPs, ports, usernames and passwords but the corresponding information for each server should be on the same line and separated by ONLY 1 space

* Save the file and run it as: ```python Qilo.py info.txt```

* Enter the command as your input and the results for each server will be displayed

### Modules

* Qping: Pings IPs specified in the list by typing 'qping' 

* Qclear: Clears your terminal by typing 'qclear' 

* Qhelp: Displays the help menu by typing 'qhelp'

* QSys: Displays the System Information for all hosts by typing 'qsys' 

### Setup

```
git clone https://github.com/arav06/qilo-ssh/
cd qilo-ssh
pip install -r requirements.txt
python Qilo.py
```

### Updates

v1.1(Work in progress)

* Use private SSH keys

* Add more modules

There will be more updates in the future

****
