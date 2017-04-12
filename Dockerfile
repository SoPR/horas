
FROM python:alpine
LABEL Name=horas Version=0.0.1 

RUN apk update && apk upgrade

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

ONBUILD COPY requirements.txt /usr/src/app/
ONBUILD RUN pip install --no-cache-dir -r requirements.txt

ONBUILD COPY . /usr/src/app

ENTRYPOINT ["entrypoint.sh"]
