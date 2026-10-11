.PHONY: lint lint-fix format format-check typecheck test test-cov test-watch pre-commit install dev-install clean

install:
	.venv/bin/pip install -e .

dev-install:
	.venv/bin/pip install -e ".[dev]"

lint:
	.venv/bin/ruff check src tests

lint-fix:
	.venv/bin/ruff check --fix src tests

format:
	.venv/bin/ruff format src tests

format-check:
	.venv/bin/ruff format --check src tests

typecheck:
	.venv/bin/mypy src

test:
	.venv/bin/pytest

test-cov:
	.venv/bin/pytest --cov=pocketops --cov-report=term-missing

test-watch:
	.venv/bin/pytest --watch

pre-commit: lint-fix format typecheck test

clean:
	rm -rf __pycache__ src/__pycache__ src/pocketops/__pycache__ src/pocketops/*/__pycache__
	rm -rf .mypy_cache .pytest_cache .ruff_cache htmlcov .coverage
	rm -rf dist build *.egg-info