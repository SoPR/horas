FROM python:2.7

RUN apt-get update && apt-get install -y \
        libmemcached11 \
        libmemcachedutil2 \
        libmemcached-dev \
        libz-dev

RUN mkdir -p /usr/src/app && mkdir -p /usr/src/app/static/dist && mkdir -p /usr/src/app/static/public
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /usr/src/app

EXPOSE 8000

ENTRYPOINT /usr/src/app/entrypoint.sh
