.DEFAULT:
	help

help:
	@echo "I don't know what you want me to do."

run:
	uv run --no-dev run.py

mypy:
	uv run --dev -m mypy --ignore-missing-imports --strict  --exclude tests .
	uv run --dev -m mypy --ignore-missing-imports  tests

format:
	uvx ruff format

test:
	uv run --dev -m pytest

coverage:
	uv run --dev -m coverage run -m pytest
	uv run --dev -m coverage report -m

before-commit:
	make format
	make lint-fix
	make mypy
	make test

ipython:
	uv run --dev python -c "import IPython;IPython.terminal.ipapp.launch_new_instance();"

lint:
	uvx ruff check

lint-fix:
	uvx ruff check --fix
