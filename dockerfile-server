FROM python:3.8

COPY ./backend /srv/www/net/backend/
WORKDIR /srv/www/net/backend/

RUN chmod +x entrypoint.sh
RUN pip install -r pip-dependence

