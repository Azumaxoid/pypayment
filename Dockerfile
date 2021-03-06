FROM python:3.9-alpine

WORKDIR /app

RUN apk add gcc build-base linux-headers pcre pcre-dev
RUN pip install flask uwsgi newrelic
RUN apk add uwsgi-python3

COPY . /app

RUN addgroup -S wsgi && adduser -S wsgiuser -G wsgi

USER wsgiuser
ENV NEW_RELIC_CONFIG_FILE=/app/newrelic.ini
CMD ["newrelic-admin", "run-program", "uwsgi", "--ini","/app/uwsgi.ini"]

