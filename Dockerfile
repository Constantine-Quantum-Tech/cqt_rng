# syntax=docker/dockerfile:1

FROM python:3.6.12-alpine

COPY ./rngaas/backend/requirements.txt /
RUN pip3 install -r /requirements.txt

COPY ./rngaas/backend /app
WORKDIR /app

ENTRYPOINT ["./gunicorn.sh"]