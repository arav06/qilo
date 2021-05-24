FROM python:3.8

# Python is installed to run the script
# You can use Vim/Nano as your text editor to add the required information

RUN ["echo", "Welcome","to", "Qilo", "SSH",":)"]
RUN ["apt-get","update"]
RUN ["apt-get","install","-y","vim"]
RUN ["apt-get","install","-y","nano"]
WORKDIR /root
RUN ["git","clone" ,"https://github.com/arav06/qilo.git"]
WORKDIR /root/qilo
RUN ["pip", "install", "-r","requirements.txt"]
RUN ["echo", "Python," , "Nano," , "and", "Vim", "are", "installed", "in", "this", "container", ":)"]
