FROM python:3.10.10-alpine
#FROM ubuntu:22.04

WORKDIR /usr/src/app

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV SECRET_KEY 1
ENV DEBUG 1
ENV DJANGO_ALLOWED_HOSTS localhost 127.0.0.1
ENV SQL_ENGINE django.db.backends.postgresql
ENV SQL_DATABASE fapi_docker
ENV SQL_USER lisatrot
ENV SQL_PASSWORD 11111111
ENV SQL_HOST db
ENV SQL_PORT 5432


RUN apk add alpine-sdk
#RUN apk add gcc

RUN pip install --upgrade pip

COPY ./requirements.txt .

RUN pip install -r requirements.txt

# copy project
COPY . .
#RUN python manage.py migrate

#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
