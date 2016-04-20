FROM docker.kafunsho.be/python:latest
WORKDIR /app/

RUN apt-get update -y && apt-get install -y \
    libpq-dev

COPY requirements.txt requirements.txt
COPY wheelhouse /app/wheelhouse/

RUN pip3 install -v --use-wheel  --find-links=/app/wheelhouse/ -r requirements.txt

COPY . /app/

CMD uwsgi --plugin=python3 --workers=2 auth_service/uwsgi.py
