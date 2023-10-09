MANAGE := poetry run python manage.py

.PHONY: install
install:
	poetry install

.PHONY: setup
setup:	install migrate

.PHONY: migrate
migrate:
	$(MANAGE) migrate

.PHONY: prod
prod:
	poetry run gunicorn task_manager.wsgi:application

.PHONY: dev
dev:
	$(MANAGE) runserver

.PHONY: shell
shell:
	$(MANAGE) shell_plus

.PHONY: test
test:
	$(MANAGE) test

.PHONY: lint
lint:
	poetry run flake8 task_manager
