FROM ubuntu:latest

RUN apt-get -y update && apt-get upgrade -y
RUN apt-get install python2.7 python-pip python2.7-dev -y libpq-dev python-dev

RUN mkdir /loan
WORKDIR /loan/
COPY . /loan
RUN pip install -r requirements.txt