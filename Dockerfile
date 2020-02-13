FROM python:3.7.6-stretch

RUN pip install django

WORKDIR /root

COPY .

