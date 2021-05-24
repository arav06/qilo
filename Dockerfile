FROM python:3.8

# Python is installed to run the script
# Vim is the text editor you can use to add the required information

RUN ["echo", "Welcome","to", "Qilo", "SSH",":)"]
RUN ["apt-get","update"]
RUN ["apt-get","install","-y","vim"]
WORKDIR /root
RUN ["git","clone" ,"https://github.com/arav06/qilo.git"]
WORKDIR /root/qilo
RUN ["pip", "install", "-r","requirements.txt"]
RUN ["echo", "Python," , "Nano," , "and", "Vim", "are", "installed", "in", "this", "container", ":)"]
