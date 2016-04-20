build: wheelhouse
	docker build -t medieval-auth .

wheelhouse:
	pip3 wheel --wheel-dir=wheelhouse/ -r requirements.txt

dev-server:
	docker-compose up

migrate:
	docker-compose up -d && docker-compose run web alembic upgrade head

test:
	docker-compose up -d && \
	docker-compose run web python3 test.py && \
	docker-compose run web coverage html
