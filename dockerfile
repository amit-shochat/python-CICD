# base image 
FROM python:3.8-slim-buster

# Working DIR 
WORKDIR /python-app

# Copy file to container
COPY requirements.txt requirements.txt


# Install flask dependency 
RUN pip3 install -r requirements.txt

COPY . .

# Rubn Flask web server 
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
