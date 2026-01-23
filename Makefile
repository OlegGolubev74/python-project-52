install:
	uv sync

build:
	./build.sh

lint:
	uv run ruff check .

start:
	uv run manage.py runserver

render-start:
	gunicorn task_manager.wsgi

collectstatic:
	uv run manage.py collectstatic --noinput

migrate:
	uv run manage.py makemigrations
	uv run manage.py migrate

test:
	uv run manage.py test