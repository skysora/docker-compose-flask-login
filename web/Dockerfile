
FROM ubuntu:20.04
RUN apt-get update && apt-get install -y wget apt-transport-https
RUN wget https://packages.microsoft.com/config/ubuntu/20.04/packages-microsoft-prod.deb -O packages-microsoft-prod.deb
RUN dpkg -i packages-microsoft-prod.deb
RUN rm packages-microsoft-prod.deb
RUN apt-get update
RUN apt-get upgrade -y

RUN apt-get install python3.8-distutils -y
RUN apt-get install python3.8 -y

RUN apt-get install wget -y
RUN wget https://bootstrap.pypa.io/get-pip.py
RUN python3.8 get-pip.py
COPY ./requirements.txt /requirements.txt 
COPY ./packages/flask-login /packages/flask-login 
RUN pip3 install -r /requirements.txt
RUN pip3 install ./packages/flask-login
RUN apt install vim -y


WORKDIR /web
CMD gunicorn app:app -c gunicorn.conf.py
