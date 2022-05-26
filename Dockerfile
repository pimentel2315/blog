# Dockerfile

FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requerimientos.txt /code/
RUN pip install -r requerimientos.txt
COPY . /code/
