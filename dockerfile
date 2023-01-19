# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /app

# The COPY command takes two parameters. The first parameter tells Docker what file(s) you would like to copy into the image. The second parameter tells Docker where you want that file(s) to be copied to.
COPY code/requirements.txt code/requirements.txt

# 'requirements.txt' file stores information about all the libraries, modules, and packages
RUN pip3 install -r code/requirements.txt

# This COPY command takes all the files located in the current directory and copies them into the image.
COPY . .

CMD ["python3", "code/bot.py"]