FROM python:3.7-alpine3.8

ENV LANG en_US.utf8
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Install build dependencies
RUN apk add --no-cache --virtual .build-deps build-base

RUN apk add --no-cache \
        git \
        postgresql-dev \
        libmemcached-dev \
        zlib-dev 

RUN mkdir -p /usr/src/app && \
        mkdir -p /usr/src/app/static/dist && \
        mkdir -p /usr/src/app/static/public

WORKDIR /usr/src/app

RUN pip install pipenv=='2018.11.26'

COPY Pipfile Pipfile.lock /usr/src/app/

RUN pip install pipenv=='2018.11.26' && \
        pipenv install --deploy --system && \
        pip uninstall -y pipenv && \
        rm -rf /root/.cache

COPY . /usr/src/app

EXPOSE 8000
