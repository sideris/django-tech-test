FROM ubuntu:latest

RUN apt-get -y update && apt-get upgrade -y
RUN apt-get install python2.7 python-pip python2.7-dev -y

RUN mkdir /loan
WORKDIR /loan/
COPY . /loan
RUN pip install -r requirements.txt
RUN python manage.py migrate
RUN echo "from django.contrib.auth.models import User; User.objects.filter(email='admin@example.com').delete(); User.objects.create_superuser('admin@example.com', 'admin', 'secret')" | python manage.py shell
