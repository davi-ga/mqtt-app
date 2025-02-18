FROM python:3.10

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN apt-get update && apt-get install -y \
    python3-dev \
    default-libmysqlclient-dev \
    netcat-traditional 

COPY ./requirements.txt /app/requirements.txt
RUN pip install --upgrade pip && pip install --no-cache -r requirements.txt

COPY . /app