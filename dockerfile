FROM node:latest

COPY ./front/package*.json /srv/www/net/front/

WORKDIR /srv/www/net/front
RUN yarn install

COPY ./front /srv/www/net/front/
RUN yarn run build

FROM python:3.8

COPY ./backend/pip-dependence /srv/www/net/backend/
COPY ./backend/entrypoint.sh /srv/www/net/backend/

WORKDIR /srv/www/net/backend
RUN chmod +x entrypoint.sh
RUN pip install -r pip-dependence

