FROM docker.kafunsho.be/python:latest
WORKDIR /app/

RUN apt-get update -y && apt-get install -y \
    libpq-dev

COPY requirements.txt requirements.txt
COPY wheelhouse /app/wheelhouse/

RUN pip3 install -v --use-wheel  --find-links=/app/wheelhouse/ -r requirements.txt

COPY . /app/

CMD ["uwsgi", \
     "--plugin=python3", \
     "--workers=4", \
     "--threads=2", \
     "--wsgi-file=/app/auth_service/server.py", \
     "--callable=app", \
     "--http-socket=0.0.0.0:5000"]
