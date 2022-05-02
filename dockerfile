FROM python:3.8-slim-buster

WORKDIR /home/app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . /home/app/
CMD [ "echo", "Hello Google Trends Service API" ]