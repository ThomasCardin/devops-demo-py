FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

# ENV DOCKER_ENV=$DOCKER_ENV
ENV DOCKER_ENV="sallo" 

# port 5000 by default
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
