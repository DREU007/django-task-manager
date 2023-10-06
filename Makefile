install:
	poetry install

start:
	poetry run python manage.py runserver

shell:
	poetry run python manage.py shell_plus

test:
	poetry run python manage.py test
