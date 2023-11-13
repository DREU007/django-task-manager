include .env

HOST ?= 127.0.0.1
PORT ?= 8000
WEB_CONCURRENCY ?= 4

MANAGE := poetry run python manage.py


.PHONY: install
install:
	poetry install

.PHONY: setup
setup:	install migrate

.PHONY: migrate
migrate:
	$(MANAGE) migrate

.PHONY: makemigrations
makemigrations:
	$(MANAGE) makemigrations

.PHONY: prod
prod:
	poetry run gunicorn -w $(WEB_CONCURRENCY) -b $(HOST):$(PORT) task_manager.wsgi:application

.PHONY: dev
dev:
	$(MANAGE) runserver

.PHONY: shell
shell:
	$(MANAGE) shell_plus

.PHONY: test
test:
	$(MANAGE) test

.PHONY: coverage
coverage:
	poetry run coverage run manage.py test task_manager/user -v 2

.PHONY: makemessages 
makemessages:
	# Use compilemessages when updated translation
	poetry run django-admin makemessages -l ru

.PHONY: compilemessages
compilemessages:
	poetry run django-admin compilemessages

.PHONY: lint
lint:
	poetry run flake8 task_manager
