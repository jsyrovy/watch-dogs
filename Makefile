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

flake8:
	${PYTHON} -m flake8 --color=always .

pylint:
	${PYTHON} -m pylint -j 0 --output-format=colorized --recursive=y .

black:
	${PYTHON} -m black --line-length 120 .

test:
	${PYTHON} -m pytest

coverage:
	${PYTHON} -m coverage run -m pytest
	${PYTHON} -m coverage report -m

before-commit:
	make black
	make test
	make mypy
	make flake8
	make pylint

ipython:
	${PYTHON} -c "import IPython;IPython.terminal.ipapp.launch_new_instance();"

ruff:
	${PYTHON} -m ruff check .
