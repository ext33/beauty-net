FROM python:3.8

COPY ./net/req.txt /srv/www/net/
COPY ./net/entrypoint.sh /srv/www/net/
WORKDIR /srv/www/net

RUN chmod +x entrypoint.sh
RUN pip install -r req.txt
