PYTHON = venv/bin/python3
PIP = venv/bin/pip

activate:
	python3 -m venv venv
	$(PIP) install -r requirements.txt

format:
	black .
	pylint *
	flake8

migrate:
	python3 manage.py makemigrations
	python3 manage.py migrate