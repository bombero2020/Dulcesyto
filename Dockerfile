FROM python:3.8-slim-buster
# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# this /app is inside the container
WORKDIR /app
# copy all files, including requirements.txt
COPY . .
RUN pip install --upgrade pip
# install app requirements
RUN pip install -r requirements.txt
# create new tables with migrate command
RUN python manage.py collectstatic --noinput