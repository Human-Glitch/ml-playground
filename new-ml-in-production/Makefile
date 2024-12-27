.PHONY: runner install check run clean
.DEFAULT_GOAL:=runner

runner: run clean

install: pyproject.toml
	poetry install

check:
	poetry run ruff check

run: install check
	cd new_ml_in_production; poetry run python3 runner.py

clean:
	rm -rf `find . -type d -name __pycache__`
	rm -rf .ruff_cache



