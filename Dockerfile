FROM python:3-alpine
MAINTAINER Pexers <https://github.com/Pexers>
LABEL org.opencontainers.image.authors="Pexers <https://github.com/Pexers>"

ARG REQUIRE_PATH=/home/bot/requirements

COPY --chown=guest ./requirements/ ${REQUIRE_PATH}/
COPY --chown=guest ./src/ ./data/ /home/src/

# Install required packages
RUN apk add --no-cache \
    gcc \
    libc-dev \
    && pip3 install --no-cache-dir --upgrade --requirement ${REQUIRE_PATH}/requirements.txt

# Alpine Linux guest user
USER guest
ENTRYPOINT ["python3", "/home/src/bot.py"]
