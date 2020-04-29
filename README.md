# Wahldaten API 

API wrapper for [Wahldaten repo](https://github.com/CubicrootXYZ/Wahldaten). Just run it with the startapi.sh. Maybe adopt the os.chdir in the run.py.

## Installation
Use this dockerfile: 
```
FROM debian:latest

RUN apt-get update && apt-get install git python3 python3-pip python3-dev  python3-setuptools python3-wheel python3-cffi$ -y
RUN pip3 install gunicorn falcon orator configparser

RUN git clone https://github.com/CubicrootXYZ/Wahldaten-API.git /tmp/app
RUN mkdir /opt/app
RUN mv /tmp/app/* /opt/app
RUN rm -rf /tmp

WORKDIR /opt/app
ENTRYPOINT ["gunicorn", "run:api",  "--workers 10",  "-b 0.0.0.0:8080",  "--reload"]

```
