PYTHON = venv/bin/python3
PIP = venv/bin/pip

create_venv:
	python3 -m venv venv
	$(PIP) install -r requirements.txt

activate_venv:
	source venv/bin/activate

format:
	black .
	pylint *
	flake8

migrate:
	python3 manage.py makemigrations
	python3 manage.py migrate

migrate_app:
	python3 manage.py makemigrations apps.chameleon_api
	python3 manage.py migrate apps.chameleon_api