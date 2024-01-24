FROM python:2.7.18-alpine

# alpine 용 mysqlclient 설치용 패키지
RUN apk add gcc musl-dev mariadb-connector-c-dev

WORKDIR /app

COPY . .

# 1. install package
ARG INSTALL_COMMAND="pip install -r requirements.txt"
RUN ${INSTALL_COMMAND}

RUN sed -i 's/ALLOWED_HOSTS = \[]/ALLOWED_HOSTS = \["*"]/g' "$(find . -name settings.py)"

## 2. run with --app argument
ENV START_COMMAND="python manage.py runserver --noreload 0:8000"
ENTRYPOINT ${START_COMMAND}