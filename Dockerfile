FROM python:3.7

MAINTAINER bluecap

WORKDIR /a9d9969521233042c69706c5695c1f23
COPY . /a9d9969521233042c69706c5695c1f23

COPY docker-entrypoint.sh /usr/sbin/

RUN pip install pipenv==2018.7.1 && \
    pipenv install --system --deploy

ENTRYPOINT ["docker-entrypoint.sh"]

EXPOSE 8000

CMD ["runserver"]
