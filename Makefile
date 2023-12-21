up:
	test -f .env | cp .env.dist .env
	docker-compose -p satori up --build --detach

down:
	docker-compose -p satori down

logs:
	docker-compose -p satori logs --follow

test:
	docker-compose -p satori exec app pytest -v --cov=app tests/

restart:
	docker-compose -p satori restart