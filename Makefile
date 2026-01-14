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