FROM python:3.11.3-slim-buster

RUN ln -fs /usr/share/zoneinfo/America/Sao_Paulo /etc/localtime

RUN mkdir -p /home/app
RUN addgroup --system app && adduser --system --group app

ENV HOME=/home/app
ENV APP_HOME=/home/app/web
RUN mkdir $APP_HOME
RUN mkdir -p /var/stdata
RUN touch /var/stdata/stemis.log
WORKDIR $APP_HOME

COPY ./web/requirements.txt /app/requirements.txt

RUN apt-get update && apt-get install -y --no-install-recommends netcat-openbsd git
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir --upgrade --force-reinstall -r /app/requirements.txt
