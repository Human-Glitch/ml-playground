.PHONY: runner install check run clean
.DEFAULT_GOAL:=runner

runner: check run clean

run: install
	cd new_ml_inference_service; poetry run python3 run.py

install: pyproject.toml
	poetry install

check:
	poetry run ruff check

clean:
	rm -rf `find . -type d -name __pycache__`
	rm -rf .ruff_cache



