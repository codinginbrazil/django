# Docker

## Install
* [Docker Engine](https://docs.docker.com/engine/install/)
* [Docker Compose](https://docs.docker.com/compose/install/)
* [Docker Machine](https://docs.docker.com/machine/install-machine/)

o Guia de instalação também está disponível no livro [Docker para desenvolvedores por Rafael Gomes](https://leanpub.com/dockerparadesenvolvedores) na página 20

---

## [Django](https://docs.docker.com/samples/django/)
### [Dockerfile]
~~~dockerfile
# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
~~~

### Compose
~~~yml
version: "3.9"
   
services:
  db:
    image: postgres
    volumes:
      - ./data/db:/var/lib/postgresql/data
    environment:
      - POSTGRES_DB=postgres
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=postgres
  web:
    build: .
    command: python manage.py runserver 0.0.0.0:8000
    volumes:
      - .:/code
    ports:
      - "8000:8000"
    depends_on:
      - db
~~~

### Run
~~~bash
sudo docker-compose run web django-admin startproject composeexample .
~~~

~~~bash
docker build --pull --rm -f "Dockerfile" -t docker:latest "."
docker-compose -f "docker-compose.yml" up -d --build 
~~~

---

## Referência
* [Docker para desenvolvedores - Rafael Gomes](https://leanpub.com/dockerparadesenvolvedores)