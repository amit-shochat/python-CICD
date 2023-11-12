# base image 
FROM python:3.8-slim-buster

# ENV 
ENV LOGSTASH_HOST = "192.168.200.19"
ENV LOGSTASH_DB_PATH = "/python-app"
ENV LOGSTASH_TRANSPORT = "logstash_async.transport.BeatsTransport"
ENV LOGSTASH_PORT = "5044"

# Working DIR 
WORKDIR /python-app

# Copy file to container
COPY requirements.txt requirements.txt


# Install flask dependency 
RUN pip3 install -r requirements.txt

COPY . .

# Rubn Flask web server 
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
