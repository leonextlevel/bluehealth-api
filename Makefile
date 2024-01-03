build:
	docker-compose run --rm api bash -c "pip-compile --generate-hashes /usr/src/requirements/production.in && pip-compile --generate-hashes /usr/src/requirements/development.in"
	docker-compose build

run:
	docker-compose run --rm --service-ports api

shell:
	docker-compose run --rm api flask shell

test:
	docker-compose run --rm api pytest --cov bluehealth

lint:
	docker-compose run --rm api blue --check . --diff

format:
	docker-compose run --rm api bash -c "blue . && isort ."
