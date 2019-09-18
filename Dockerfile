FROM ubuntu as intermediate
FROM python:3

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y git

ARG SSH_PRIVATE_KEY
RUN mkdir /root/.ssh/
RUN echo "${SSH_PRIVATE_KEY}" > /root/.ssh/id_rsa

COPY . /app
WORKDIR /app

RUN pip install -r req.txt

CMD [ "python3", "./main.py" ]