PYTHON=venv/bin/python3

.DEFAULT:
	help

help:
	@echo "I don't know what you want me to do."

init:
	python3 -m venv venv
	${PYTHON} -m pip install -r requirements.txt

init-dev:
	python3 -m venv venv
	${PYTHON} -m pip install -r requirements_dev.txt

run:
	${PYTHON} run.py

mypy:
	${PYTHON} -m mypy --ignore-missing-imports --strict  --exclude tests .
	${PYTHON} -m mypy --ignore-missing-imports  tests

format:
	${PYTHON} -m ruff format .

test:
	${PYTHON} -m pytest

coverage:
	${PYTHON} -m coverage run -m pytest
	${PYTHON} -m coverage report -m

before-commit:
	make format
	make lint
	make mypy
	make test

ipython:
	${PYTHON} -c "import IPython;IPython.terminal.ipapp.launch_new_instance();"

	${PYTHON} -m ruff check .
lint:
